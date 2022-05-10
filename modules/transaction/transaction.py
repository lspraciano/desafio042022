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
        transactions_date = request.args.get('date')
        transactions_date = datetime.strptime(transactions_date, '%d/%m/%Y')
        return get_transactions_list_by_date(transactions_date)
    elif request.method == 'POST':
        transactions_list = request.json
        return save_transactions_list(transactions_list)


@transaction_blueprint.route('/import-csv', methods=['GET', ])
@token_authentication
def import_csv():
    return render_template('import_transaction.html'), 200


@transaction_blueprint.route('/log', methods=['GET', ])
@token_authentication
def audit_transaction():
    return render_template('transaction_log.html'), 200


@transaction_blueprint.route('/log/get-log', methods=['GET', ])
@token_authentication
def audit_transaction_data():
    return get_all_logs(), 200
