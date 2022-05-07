# Native Imports
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

# Created Imports
from sqlalchemy.orm import relationship

from database.database import ModelBase


class UserAudit(ModelBase):
    __tablename__ = "tbusers_audit"

    user_audit_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_audit_user_id = Column(Integer, nullable=False)
    user_audit_user_name = Column(String, unique=True, nullable=False)
    user_audit_user_password = Column(String, nullable=False)
    user_audit_user_email = Column(String, unique=True, nullable=False)
    user_audit_user_token = Column(String, nullable=True)
    user_audit_user_status = Column(Integer, nullable=False)
    user_audit_last_modification_user_id = Column(Integer, ForeignKey('tbusers.user_id'), nullable=False)
    user_audit_transaction_type = Column(String, nullable=False)
    user_audit_transaction_date_time = Column(DateTime(timezone=False), nullable=False)
    user_audit_user_rl = relationship('User', lazy='joined')

    def __repr__(self) -> str:
        return f'User(id={self.user_audit_id}, user_id={self.user_audit_user_id})'
