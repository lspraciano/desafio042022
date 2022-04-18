import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import sqlalchemy.ext.declarative
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine

__engine: Optional[Engine] = None
ModelBase = sqlalchemy.ext.declarative.declarative_base()


def create_engine(app) -> Engine:
    """
    Função para configurar a conexão ao banco de dados.
    """
    global __engine

    conn_str = app.config.get('SQLALCHEMY_DATABASE_URI')
    __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    """
    Função para criar sessão de conexao ao banco de dados.
    """
    global __engine

    if not __engine:
        create_engine()

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session


def init_db() -> None:
    global __engine

    if not __engine:
        create_engine()
