# Native Imports
from datetime import datetime

# Created Imports
from database.database import create_session
from error.error import get_error_msg
from modules.transaction.models.transaction_logs_model import TransactionLog
from resources.py.token.token_manager import user_id_from_token

session = create_session()


def save_transaction_log(log_date: datetime):
    """
    Essa função salva a data que as transações serão salvas, com intuito de gerar um log de atividade. Ela recebe a
    data que as transações foram realizadas e registra no banco SQL.

    :param log_date: data das transações
    :return: No caso de sucesso: { 'success': 'log saved' } ||| No caso de erro: { 'error': erro ocorrido }
    """

    try:
        transaction_log = TransactionLog(
            transactions_log_transactions_datetime=log_date,
            transactions_log_datetime=datetime.now(),
            transactions_log_user_id=user_id_from_token())

        session.add(transaction_log)
        session.commit()
        return {'success': 'log saved'}

    except:
        session.rollback()
        return get_error_msg()


def get_all_logs():
    logs = session.query(TransactionLog).all()
    return {'logs': 'teste'}
