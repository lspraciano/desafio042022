# Native Imports
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.future.engine import Engine
from sqlalchemy.ext.declarative import declarative_base

# Created Imports
from werkzeug.security import generate_password_hash

from configuration.configuration import app_configuration, app_active

__engine = None
ModelBase = declarative_base()


def create_engine() -> Engine:
    """
    Função para configurar a conexão ao banco de dados.

    :return: engine
    """
    global __engine

    configuration = app_configuration[app_active]
    conn_str = configuration.SQLALCHEMY_DATABASE_URI
    __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    """
    Função para criar sessão de conexão ao banco de dados.

    :return: Session()
    """
    global __engine

    if not __engine:
        create_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session = __session()

    return session


def create_db() -> None:
    """
    Função destinada para criação do banco de dados requisitado pela aplicação

    :return: None
    """

    from modules.transaction.models import transaction_model, transaction_logs_model
    from modules.users.models import user_model

    global __engine

    if not __engine:
        create_engine()

    # ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
    create_admin_user(user_model)


def create_admin_user(model) -> None:
    """
    Esta função é destinada a criar o usuário inicial da aplicação, ou seja, o usuário administrador. Caso ele já
    exista, não será gerado um novo usuário administrador.

    :return: None
    """
    session = create_session()

    user = session.query(model.User).filter_by(user_name='LUCAS PRACIANO').first()

    if not user:
        user = model.User(
            user_name='LUCAS PRACIANO',
            user_password=generate_password_hash('Abcd@123', method='sha256'),
            user_email='LUSKCCT@GMAIL.COM',
            user_status=1,
        )

        session.add(user)
        session.commit()

    session.close()
