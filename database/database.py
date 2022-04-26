# Native Imports
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.future.engine import Engine
from sqlalchemy.ext.declarative import declarative_base

# Created Imports
from configuration.configuration import app_configuration, app_active

__engine = None
ModelBase = declarative_base()


def create_engine() -> Engine:
    """
    Função para configurar a conexão ao banco de dados.
    """
    global __engine

    configuration = app_configuration[app_active]
    conn_str = configuration.SQLALCHEMY_DATABASE_URI
    __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    """
    Função para criar sessão de conexão ao banco de dados.
    """
    global __engine

    if not __engine:
        create_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session = __session()

    return session
