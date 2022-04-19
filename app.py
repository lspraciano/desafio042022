# Native Imports
from flask import Flask

# BluePrints Imports
from modules.root.rootRoutes import root_blueprint
from modules.transaction.transaction import transaction_blueprint
from resources.resources import resources_blueprint
from modules.users.user import user_blueprint


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    _register_blueprint(app)

    return app


def _register_blueprint(app: Flask) -> None:
    app.register_blueprint(root_blueprint, url_prefix='/')
    app.register_blueprint(transaction_blueprint, url_prefix='/transaction')
    app.register_blueprint(resources_blueprint, url_prefix='/resources')
    app.register_blueprint(user_blueprint, url_prefix='/user')
