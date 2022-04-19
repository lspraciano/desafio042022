# Native Imports
from werkzeug.security import check_password_hash, generate_password_hash

# Created Imports
from database.database import create_session
from error.error import get_error_msg
from modules.users.models.user_model import User
from resources.py.token import token_manager

session = create_session()


def get_user_by_username(username: str) -> User:
    """
    Esta função retorna um usuário do banco sql através do seu nome

    :param username: Nome do usuário
    :return: Objeto usuário contendo as informações do usuário consultado
    """

    user = session.query(User).filter_by(user_name=username).first()
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
        # print(generate_password_hash('Abcd@321', method='sha256'))

        if user is None:
            return {"error": "access denied"}

        if user.user_status == 0:
            return {"error": "access denied"}

        if not check_password_hash(user.user_password, password):
            return {"error": "access denied"}

        return token_manager.token_generator(user.user_id)

    except:
        return get_error_msg()
