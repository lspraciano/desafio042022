# Native Imports
from datetime import datetime

from flask import Blueprint, render_template, request

# Created Imports
from modules.transaction.controllers.transaction_controller import save_transactions_list, get_transactions_list_by_date
from modules.transaction.controllers.transaction_log_controller import get_all_logs
from resources.py.token.token_manager import token_authentication

transaction_blueprint = Blueprint('transaction', __name__,
                                  template_folder='templates',
                                  static_folder='static')


@transaction_blueprint.route('/', methods=['GET', 'POST'])
@token_authentication
def transactions():
    if request.method == 'GET':
        return get_transactions_list_by_date(request)
    elif request.method == 'POST':
        return save_transactions_list(request.json)


@transaction_blueprint.route('/import', methods=['GET', ])
@token_authentication
def import_csv():
    return render_template('import_transaction.html')


@transaction_blueprint.route('/log', methods=['GET', ])
@token_authentication
def audit_transaction():
    return render_template('transaction_log.html')


@transaction_blueprint.route('/log/get-log', methods=['GET', ])
@token_authentication
def audit_transaction_data():
    return get_all_logs(), 200
