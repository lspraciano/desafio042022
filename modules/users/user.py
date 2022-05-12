# Native Imports
from flask import Blueprint, render_template, request

# Created Imports
from modules.users.controllers.user_controller import check_login_password, get_all_users, create_new_user, update_user
from resources.py.token.token_manager import token_authentication

user_blueprint = Blueprint('user', __name__,
                           template_folder='templates',
                           static_folder='static')


@user_blueprint.route('/', methods=['GET', 'POST', 'UPDATE'])
@token_authentication
def user():
    if request.method == 'GET':
        return get_all_users()
    elif request.method == 'POST':
        created_user = create_new_user(request.json)
        return created_user
    elif request.method == 'UPDATE':
        updated_user = update_user(request.json)
        return updated_user


@user_blueprint.route('/authentication', methods=['GET', 'POST'])
def user_authentication():
    if request.method == 'GET':
        return render_template('user_authentication.html')
    elif request.method == 'POST':
        return check_login_password(request.json)


@user_blueprint.route('/manager', methods=['GET'])
@token_authentication
def user_manager():
    if request.method == 'GET':
        return render_template('user_manager.html')
