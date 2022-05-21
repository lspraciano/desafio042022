# Imports Native
from flask import json


# Created Imports


def test_import_transaction_template_with_valid_token(app, client_admin_authenticaded, captured_templates):
    response = client_admin_authenticaded.get("transaction/import-csv")
    template, context = captured_templates[0]

    assert response.status_code == 200
    assert len(captured_templates) == 1
    assert template.name == "import_transaction.html"


def test_import_transaction_template_without_token(client):
    response = client.get("transaction/import-csv")
    assert response.status_code == 401



