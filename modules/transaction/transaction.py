# Native Imports
from flask import Blueprint, render_template, request

# Created Imports
from resources.py.token.token_manager import token_authentication

transaction_blueprint = Blueprint('transaction', __name__,
                                  template_folder='templates',
                                  static_folder='static')


@transaction_blueprint.route('/', methods=['GET', ])
@token_authentication
def transaction_():
    if request.method == 'GET':
        return render_template('import_transaction.html'), 200
    if request.method == 'POST':
        return {'Em desenvolvimento': 'TRUE'}
