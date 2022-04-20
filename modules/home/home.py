# Native Imports
from flask import Blueprint, render_template

# Created Imports
from resources.py.token.token_manager import token_authentication

home_blueprint = Blueprint('home', __name__,
                           template_folder='templates',
                           static_folder='static')


@home_blueprint.route('/')
@token_authentication
def home_page():
    return render_template('home.html'), 200
