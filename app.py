# Native Imports
from flask import Flask

# BluePrints Imports
from modules.transaction.transaction import transaction_blueprint


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    _register_blueprint(app)

    return app


def _register_blueprint(app: Flask) -> None:
    app.register_blueprint(transaction_blueprint, url_prefix='/transaction')
