# Native Imports
from werkzeug.security import check_password_hash, generate_password_hash

# Created Imports
from configuration.configuration import Configuration
from database.database import create_session
from error.error import get_error_msg
from modules.users.models.user_model import User
from modules.users.serializers.user_seriallizer import UserBasicSchema
from resources.py.password.password_manager import generate_password
from resources.py.token import token_manager
from resources.py.email.email_manager import validate_email, send_email_password_new_user
from resources.py.token.token_manager import user_id_from_token

session = create_session()

UserBasicSchema = UserBasicSchema(many=True)


def get_user_by_id(user_id: int) -> User:
    """
    Esta função retorna um usuário do banco sql através do seu ID

    :param user_id: ID do usuário
    :return: Objeto usuário contendo as informações do usuário consultado
    """

    user = session.query(User).filter_by(user_id=user_id).first()
    session.close()
    return user


def get_user_by_username(username: str) -> User:
    """
    Esta função retorna um usuário do banco sql através do seu nome

    :param username: Nome do usuário
    :return: Objeto usuário contendo as informações do usuário consultado
    """

    user = session.query(User).filter_by(user_name=username).first()
    session.close()
    return user


def get_user_by_email(email: str) -> User:
    """
    Esta função retorna um usuário do banco sql através do seu email

    :param email: Nome do email
    :return: Objeto usuário contendo as informações do usuário consultado
    """

    user = session.query(User).filter_by(user_email=email).first()
    session.close()
    return user


def check_login_password(login_request: dict) -> dict:
    """
    Função para autenticar o usuário e caso ele seja aceito, esta função ira registrar no REDIS o perfil de exames
    para este usuário e carregar os exames gerais usados pelo modelo

    :param login_request: Request realizado pelo usuário
    :return: Dicionário contendo um TOKEN para relizar futuras transações
    """
    try:
        username = login_request['username'].upper()
        password = login_request['password']

        user = get_user_by_username(username)
        # print(generate_password_hash('senha_para_gerar_hash', method='sha256'))

        if user is None:
            return {"error": "access denied"}

        if user.user_status == 0:
            return {"error": "access denied"}

        if not check_password_hash(user.user_password, password):
            return {"error": "access denied"}

        return token_manager.token_generator(user.user_id)

    except:
        return get_error_msg()


def get_all_users() -> dict:
    """
    Esta função retorna todos os usuários do banco sql com exceção do usuário administrador

    :return: Dicionário contendo uma lista de usuários
    """

    user = session.query(User).filter(User.user_id != Configuration.ADMIN_USER_ID).all()
    session.close()

    return {'users': UserBasicSchema.dump(user)}


def check_username_email(username: str = None, email: str = None):
    """
    Esta função realiza a validação do username e email, verificando no banco de dados se já estão previamente
    cadastrados, bem como, realiza a validação do email através de uma REGEX

    :param username: nome do usuário
    :param email: email do usuário
    :return: Em caso de sucesso será retornado {'success': 'ok'} e em caso de não sucesso será retornado
     {'error': foo}
    """
    if username == '' or email == '':
        return {'error': 'invalid username or email'}

    if email:
        user_by_email = get_user_by_email(email)
        if user_by_email or not validate_email(email):
            return {'error': 'invalid email'}

    if username:
        user_by_username = get_user_by_username(username)
        if user_by_username:
            return {'error': 'invalid username'}

    return {'success': 'ok'}


def create_new_user(user_name: str,
                    user_email: str,
                    user_status: int = 1,
                    user_password: str = '') -> dict:
    """
    Esta função insere no banco SQL um usuário. Antes de inserir é verificado a existência do email ou username. Caso
    não seja informado um password será gerada uma senha com 8 carácteres para este usuário.

    :param user_name: nome do usuário
    :param user_email:  email do usuário
    :param user_status: status do usuário
    :param user_password: senha do usuário
    :return: em caso de sucesso será retornado {'user': user} ou em caso de não sucesso {'error': foo}
    """

    validate_username_and_email = check_username_email(username=user_name,
                                                       email=user_email)

    if 'error' in validate_username_and_email.keys():
        return validate_username_and_email

    if user_password == '':
        user_password = generate_password()

    user = User(
        user_name=user_name.upper(),
        user_password=generate_password_hash(user_password, method='sha256'),
        user_email=user_email.upper(),
        user_status=user_status,
        user_last_modification_user_id=user_id_from_token()
    )

    session.add(user)
    session.commit()
    session.close()

    validate_send_email = send_email_password_new_user(email=user_email,
                                                       password=user_password)

    if 'error' in validate_send_email.keys():
        return validate_send_email

    return {'user': UserBasicSchema.dump([user])}


def update_user(user_cod: int,
                user_name: str,
                user_email: str,
                user_status: bool,
                user_password: str = '',
                user_token: str = '') -> dict:
    if not user_cod:
        return {'error': 'invalid cod'}

    user = get_user_by_id(user_cod)

    if not user:
        return {'error': 'non-existing user'}

    if int(user_cod) == user_id_from_token() and user_status is False:
        return {'error': 'you cannot disable your access'}

    if user.user_name != user_name:
        validate_username = check_username_email(username=user_name)
        if 'error' in validate_username.keys():
            return validate_username
        user.user_name = user_name

    if user.user_email != user_email:
        validate_user_email = check_username_email(email=user_email)
        if 'error' in validate_user_email.keys():
            return validate_user_email
        user.user_email = user_email

    if user_status is True:
        user.user_status = 1
    elif user_status is False:
        user.user_status = 0
    else:
        return {'error': 'invalid status'}

    if user_password != '':
        user.user_password = user_password

    if user_token != '':
        user.user_token = user_token

    user.user_last_modification_user_id = user_id_from_token()

    session.add(user)
    session.commit()
    session.close()

    return {'user': UserBasicSchema.dump([user])}
