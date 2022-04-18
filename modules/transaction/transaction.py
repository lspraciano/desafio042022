# Native Imports
from flask import Blueprint, render_template, request

# Created Imports


transaction_blueprint = Blueprint('transaction', __name__,
                                  template_folder='templates',
                                  static_folder='static')


@transaction_blueprint.route('/', methods=['GET', ])
def transaction_():
    if request.method == 'GET':
        return render_template('import_transaction.html'), 200
    if request.method == 'POST':
        return {'Em desenvolvimento': 'TRUE'}
