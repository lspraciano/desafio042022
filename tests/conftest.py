# Imports Native
import pytest

# Created Imports
from run import run_server


@pytest.fixture(scope="module")
def app():
    """
    Esta função cria uma instancia do app flask

    :return: app flask
    """
    app = run_server()
    return app


@pytest.fixture
def client(app):
    return app.test_client()
