# Native Imports
from flask import Blueprint, render_template, request

# Created Imports
from modules.users.controllers.user_controller import check_login_password

user_blueprint = Blueprint('user', __name__,
                           template_folder='templates',
                           static_folder='static')


@user_blueprint.route('/authentication', methods=['GET', 'POST'])
def user_authentication():
    if request.method == 'GET':
        return render_template('user_authentication.html'), 200
    elif request.method == 'POST':
        return check_login_password(request.json), 200
    else:
        return {'Em desenvolvimento': 'TRUE'}
