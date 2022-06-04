# Imports Native
from datetime import datetime

from flask import json

# Created Imports
from modules.transaction.controllers.transaction_controller import get_transaction_by_date, \
    get_suspects_transactions_report


def test_import_transaction_template_with_valid_token(app, client_admin_authenticaded, captured_templates):
    response = client_admin_authenticaded.get("transaction/import")
    template, context = captured_templates[0]

    assert response.status_code == 200
    assert len(captured_templates) == 1
    assert template.name == "import_transaction.html"


def test_import_transaction_template_without_token(client):
    response = client.get("transaction/import")
    assert response.status_code == 401


def test_import_one_transaction_with_valid_json(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    transactions_by_date = get_transaction_by_date(
        datetime.strptime(data[0]['transaction_date_time'], "%Y-%m-%dT%H:%M:%S")
    )

    assert response.status_code == 201
    assert "success" in response.json
    assert 'transactions' in transactions_by_date
    assert len(transactions_by_date['transactions']) == len(data)
    for idx, transaction in enumerate(transactions_by_date['transactions']):
        assert transaction['transaction_home_bank'] == data[idx]['transaction_home_bank']
        assert transaction['transaction_home_branch'] == data[idx]['transaction_home_branch']
        assert transaction['transaction_home_account'] == data[idx]['transaction_home_account']
        assert transaction['transaction_destination_bank'] == data[idx]['transaction_destination_bank']
        assert transaction['transaction_destination_account'] == data[idx]['transaction_destination_account']
        assert transaction['transaction_amount'] == data[idx]['transaction_amount']
        assert transaction['transaction_date_time'] == data[idx]['transaction_date_time']


def test_import_one_transaction_already_existing_data(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_home_bank(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bankk": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_home_branch(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branchh": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_home_account(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_accountt": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_destination_bank(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bankk": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_destination_branch(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branchh": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_destination_account(app,
                                                                                        client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_accountt": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_amount(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amountt": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_field_transaction_date_time(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_timee": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_home_bank(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_home_branch(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": "1",
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_home_account(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_destination_bank(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_destination_branch(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": "2",
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_destination_account(app,
                                                                                        client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_amount(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": "240.5",
        "transaction_date_time": "2022-05-22T06:10:45"
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_one_transaction_with_invalid_json_value_transaction_date_time(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_timee": ""
    }, ]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_import_two_transactions_with_valid_json(app, client_admin_authenticaded):
    data = [{
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 240.5,
        "transaction_date_time": "2022-05-24T06:10:45"
    }, {
        "transaction_home_bank": "TEST",
        "transaction_home_branch": 1,
        "transaction_home_account": "00223",
        "transaction_destination_bank": "TEST2",
        "transaction_destination_branch": 2,
        "transaction_destination_account": "00214",
        "transaction_amount": 550.5,
        "transaction_date_time": "2022-05-24T06:10:45"
    }]

    response = client_admin_authenticaded.post(
        "transaction/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    transactions_by_date = get_transaction_by_date(
        datetime.strptime(data[0]['transaction_date_time'], "%Y-%m-%dT%H:%M:%S")
    )

    assert response.status_code == 201
    assert "success" in response.json
    assert 'transactions' in transactions_by_date
    assert len(transactions_by_date['transactions']) == len(data)
    for idx, transaction in enumerate(transactions_by_date['transactions']):
        assert transaction['transaction_home_bank'] == data[idx]['transaction_home_bank']
        assert transaction['transaction_home_branch'] == data[idx]['transaction_home_branch']
        assert transaction['transaction_home_account'] == data[idx]['transaction_home_account']
        assert transaction['transaction_destination_bank'] == data[idx]['transaction_destination_bank']
        assert transaction['transaction_destination_account'] == data[idx]['transaction_destination_account']
        assert transaction['transaction_amount'] == data[idx]['transaction_amount']
        assert transaction['transaction_date_time'] == data[idx]['transaction_date_time']