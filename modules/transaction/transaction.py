# Native Imports
from flask import Blueprint, render_template, request

# Created Imports
from modules.transaction.controllers.transaction_controller import save_transactions_list
from resources.py.token.token_manager import token_authentication

transaction_blueprint = Blueprint('transaction', __name__,
                                  template_folder='templates',
                                  static_folder='static')


@transaction_blueprint.route('/', methods=['GET', 'POST'])
@token_authentication
def transactions():
    if request.method == 'GET':
        return {'Em desenvolvimento': 'TRUE'}
    if request.method == 'POST':
        transactions_list = request.json
        return save_transactions_list(transactions_list)


@transaction_blueprint.route('/import-csv', methods=['GET', ])
@token_authentication
def import_csv():
    return render_template('import_transaction.html'), 200
