# Imports Native
import pytest

# Created Imports
from run import run_server
from configuration.configuration import Configuration


@pytest.fixture(scope="module")
def app():
    """
    Esta função cria uma instancia do app flask

    :return: app flask
    """
    app = run_server()
    return app
