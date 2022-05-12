# Native Imports
import re
from datetime import datetime

from flask import request, make_response
from sqlalchemy import extract

# Created Imports
from database.database import create_session
from error.error import get_error_msg
from modules.transaction.controllers.transaction_log_controller import save_transaction_log
from modules.transaction.json_schema.transactions_json import json_validate_transaction
from modules.transaction.models.transaction_model import Transaction
from modules.transaction.serializers.transaction_schema import TransactionSchema

session = create_session()
TransactionSchema = TransactionSchema(many=True)


def get_transaction_by_date(transactions_date: datetime) -> dict:
    if not isinstance(transactions_date, datetime):
        return {'error': 'invalid date'}

    transactions = session.query(Transaction).filter(
        extract('month', Transaction.transaction_date_time) == transactions_date.month,
        extract('year', Transaction.transaction_date_time) == transactions_date.year,
        extract('day', Transaction.transaction_date_time) == transactions_date.day).all()

    session.close()

    return {'transactions': TransactionSchema.dump(transactions)}


def validate_transaction_list(transactions_list: list) -> dict:
    """
    Essa função é responsável por realizar a validação da lista de transações recebidas. Se a lista for
    considerada válida, será retornado "True", caso contrário "False". A formatação da lista deve
    seguir esta ordem de valores:

    [Banco origem, Agência origem, Conta origem, Banco destino, Agência destino, Conta destino,
    Valor da transação, Data e hora da transação]

    :param transactions_list: lista de transações
    :return: em caso de sucesso será retornado {'success': 'ok'} ou em caso de não sucesso
     { 'error': foo }
    """
    try:
        transactions_date = transactions_list[0]['transaction_date_time']
        transactions_date = datetime.strptime(transactions_date, "%Y-%m-%dT%H:%M:%S")

        check_transactions = get_transaction_by_date(transactions_date)

        if check_transactions['transactions']:
            return {'error': 'file with this date already exists'}

        for transaction in transactions_list:
            current_transaction_date = datetime.strptime(transaction['transaction_date_time'], "%Y-%m-%dT%H:%M:%S")
            if current_transaction_date.date() != transactions_date.date() or '' in transaction.values():
                return {'error': 'there are records other than the file date'}
        return {'success': 'ok'}

    except:
        return get_error_msg()


def get_transactions_list_by_date(transaction_request: request) -> make_response:
    """
    Esta função retorna um dicionário contendo todas as transações para uma determinada data. A data deve ser informada
    como parâmentro de entrada no formato datetime.

    :param transaction_request: requisição do usuário
    :return: em caso de sucesso será retornado {'transactions': [ { transações }, ]  ou em caso de erro inesperado
     { 'error' : foo }
    """

    try:
        transactions_date = transaction_request.args.get('date')
        try:
            transactions_date = datetime.strptime(transactions_date, '%d/%m/%Y')
        except:
            return make_response({'error': 'invalid date'}, 400)

        transactions = get_transaction_by_date(transactions_date)

        if 'error' in transactions.keys():
            return make_response(transactions, 400)
        return make_response(transactions, 200)

    except:
        return get_error_msg()


def save_transactions_list(transaction_request: list) -> make_response:
    """
    Esta função salva uma lista de transações no banco SQL e retorna um dicionário contendo a chave "success", caso
    tudo ocorra com esperado ou  retorna um diconário com a chave erro, caso algo inesperado ocorra. No caso de sucesso
    dentro da chave "success" teremos o número de linhas inseridas.  A formatação da lista deve seguir esta ordem
    de valores:

    [[Banco origem, Agência origem, Conta origem, Banco destino, Agência destino, Conta destino,
    Valor da transação, Data e hora da transação]]


    :param transaction_request: lista de transações
    :return: No caso de sucesso: { 'success': { 'transactions': número de linhas } }
     ||| No caso de erro: { 'error': erro ocorrido }
    """

    try:
        if not json_validate_transaction(transaction_request):
            return make_response({'error': 'invalid json'}, 415)

        check_transactions = validate_transaction_list(transaction_request)

        if 'error' in check_transactions:
            return make_response(check_transactions, 400)

        transactions = []
        transaction_date = ""

        for transaction in transaction_request:
            transaction_date = datetime.strptime(transaction['transaction_date_time'], "%Y-%m-%dT%H:%M:%S")
            row = Transaction(transaction_home_bank=transaction['transaction_home_bank'],
                              transaction_home_branch=transaction['transaction_home_branch'],
                              transaction_home_account=transaction['transaction_home_account'],
                              transaction_destination_bank=transaction['transaction_destination_bank'],
                              transaction_destination_branch=transaction['transaction_destination_branch'],
                              transaction_destination_account=transaction['transaction_destination_account'],
                              transaction_amount=transaction['transaction_amount'],
                              transaction_date_time=transaction_date)
            transactions.append(row)

        transaction_log = save_transaction_log(transaction_date)

        if 'success' not in transaction_log.keys():
            session.rollback()
            return make_response({'error': transaction_log}, 400)

        session.add_all(transactions)
        session.commit()
        session.close()
        return make_response({'success': {'transactions': len(transactions)}}, 201)

    except:
        session.rollback()
        return get_error_msg()
