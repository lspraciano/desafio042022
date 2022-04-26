# Native Imports
from datetime import datetime

# Created Imports
from database.database import create_session
from error.error import get_error_msg
from modules.transaction.controllers.transaction_log_controller import save_transaction_log
from modules.transaction.models.transaction_model import Transaction

session = create_session()


def validate_transaction_list(transactions_list: list) -> bool:
    """
    Essa função é responsável por realizar a validação da lista de transações recebidas. Se a lista for
    considerada válida, será retornado "True", caso contrário "False". A formatação da lista deve
    seguir esta ordem de valores:

    [Banco origem, Agência origem, Conta origem, Banco destino, Agência destino, Conta destino,
    Valor da transação, Data e hora da transação]

    :param transactions_list: lista de transações
    :return: true ou false
    """
    try:
        transactions_date = transactions_list[0][-1][0:10]

        for transaction in transactions_list:
            if transaction[-1][0:10] != transactions_date or '' in transaction:
                return False
        return True

    except:
        return False


def save_transactions_list(transactions_list: list) -> dict:
    """
    Esta função salva uma lista de transações no banco SQL e retorna um dicionário contendo a chave "success", caso
    tudo ocorra com esperado ou  retorna um diconário com a chave erro, caso algo inesperado ocorra. No caso de sucesso
    dentro da chave "success" teremos o número de linhas inseridas.

    :param transactions_list: lista de transações
    :return: No caso de sucesso: { 'success': { 'transactions': número de linhas } }
     ||| No caso de erro: { 'error': erro ocorrido }
    """

    try:

        if not validate_transaction_list(transactions_list):
            return {'error': 'Invalid data'}

        transactions = []
        transaction_date = datetime.strptime(transactions_list[0][7], "%Y-%m-%dT%H:%M:%S")

        for transaction in transactions_list:
            row = Transaction(transaction_home_bank=str(transaction[0]),
                              transaction_home_branch=int(transaction[1]),
                              transaction_home_account=str(transaction[2]),
                              transaction_destination_bank=str(transaction[3]),
                              transaction_destination_branch=int(transaction[4]),
                              transaction_destination_account=str(transaction[5]),
                              transaction_amount=float(transaction[6]),
                              transaction_date_time=transaction_date)
            transactions.append(row)

        transaction_log = save_transaction_log(transaction_date)
        if 'success' not in transaction_log.keys():
            session.rollback()
            return {'error': transaction_log}

        session.add_all(transactions)
        session.commit()
        session.close()
        return {'success': {'transactions': len(transactions)}}

    except:
        session.rollback()
        return get_error_msg()
