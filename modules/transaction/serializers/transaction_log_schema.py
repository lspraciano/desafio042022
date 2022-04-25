# Native Imports
from marshmallow import Schema, fields

# Created Imports


class TransactionLogSchema(Schema):
    transactions_log_id = fields.Integer()
    transactions_log_transactions_datetime = fields.DateTime()
    transactions_log_datetime = fields.DateTime()
    transactions_log_user_id = fields.Integer()
