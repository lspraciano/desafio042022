# Imports Native
import pytest

# Created Imports
from database.database import create_session
from run import run_server


@pytest.fixture(scope="module")
def app():
    """
    Esta função retorna uma instancia do app flask

    :return: app flask
    """
    app = run_server()
    return app


@pytest.fixture
def client(app):
    """
    Esta função retorna um cliente HTTP para ser usado durante os teste desta aplicação

    :param app: app flask
    :return: client HTTP
    """
    return app.test_client()


@pytest.fixture()
def session(app):
    """
    Esta função retorna uma sessão do SQLAlchemy

    :param app: app flask
    :return: session
    """
    with app.app_context():
        return create_session()
