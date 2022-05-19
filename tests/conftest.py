# Imports Native
import pytest

# Created Imports
from flask import template_rendered

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


@pytest.fixture(scope="function")
def client(app):
    """
    Esta função retorna um cliente HTTP para ser usado durante os teste desta aplicação

    :param app: app flask
    :return: client HTTP
    """
    return app.test_client()


@pytest.fixture(scope="function")
def session(app):
    """
    Esta função retorna uma sessão do SQLAlchemy

    :param app: app flask
    :return: session
    """
    with app.app_context():
        return create_session()


@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)
