# Native Imports
from flask import Blueprint, render_template

# Created Imports

user_blueprint = Blueprint('user', __name__,
                           template_folder='templates',
                           static_folder='static')


@user_blueprint.route('/')
def login():
    return render_template('user_authentication.html'), 200

