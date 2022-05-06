# Native Imports
from flask import Blueprint, render_template, request

# Created Imports
from modules.users.controllers.user_controller import check_login_password, get_all_users
from resources.py.token.token_manager import token_authentication

user_blueprint = Blueprint('user', __name__,
                           template_folder='templates',
                           static_folder='static')


@user_blueprint.route('/', methods=['GET', 'POST'])
@token_authentication
def user():
    if request.method == 'GET':
        return get_all_users()
    elif request.method == 'POST':
        return {'...': 'true'}


@user_blueprint.route('/authentication', methods=['GET', 'POST'])
def user_authentication():
    if request.method == 'GET':
        return render_template('user_authentication.html'), 200
    elif request.method == 'POST':
        return check_login_password(request.json), 200


@user_blueprint.route('/manager', methods=['GET'])
@token_authentication
def user_manager():
    if request.method == 'GET':
        return render_template('user_manager.html'), 200
