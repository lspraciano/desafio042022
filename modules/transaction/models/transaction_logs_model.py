# Native Imports
from database.database import ModelBase
from sqlalchemy import Column, Integer, DateTime, UniqueConstraint


class TransactionLog(ModelBase):
    __tablename__ = "tbtransactions_logs"

    transactions_log_id = Column(Integer, primary_key=True, index=True)
    transactions_log_transactions_datetime = Column(DateTime, nullable=False)
    transactions_log_datetime = Column(DateTime, nullable=False)
    transactions_log_user_id = Column(Integer, nullable=False)
    UniqueConstraint('transactions_log_transactions_datetime')

    def __repr__(self) -> str:
        return str({
            'transactions_log_id': self.transactions_log_id,
            'transactions_log_transactions_datetime': self.transactions_log_transactions_datetime,
            'transactions_log_datetime': self.transactions_log_datetime,
            'transactions_log_user_id': self.transactions_log_user_id
        })
