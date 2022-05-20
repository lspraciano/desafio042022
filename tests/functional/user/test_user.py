# Imports Native
from flask import json

# Created Imports
from werkzeug.security import check_password_hash

from modules.users.controllers.user_controller import get_user_by_id


def test_redirect_to_login(client):
    response = client.get("/")
    assert response.status_code == 302


def test_user_authentication_template(client, captured_templates):
    response = client.get("user/authentication")
    template, context = captured_templates[0]

    assert response.status_code == 200
    assert len(captured_templates) == 1
    assert template.name == "user_authentication.html"


def test_user_authentication_valid(client, app):
    data = {
        "user_name": app.config["ADMIN_USER_NAME"],
        "user_password": app.config["ADMIN_PASSWORD"]
    }

    response = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    assert response.status_code == 200
    assert "token" in response.json


def test_user_authentication_invalid_credentials(client):
    data = {
        "user_name": 'test',
        "user_password": 'test'
    }

    response = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    assert response.status_code == 401
    assert "error" in response.json


def test_user_authentication_invalid_json_user_name_field(client):
    data = {
        "user_naame": 'test',
        "user_password": 'test'
    }

    response = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    assert response.status_code == 415
    assert "error" in response.json


def test_user_authentication_invalid_json_user_password_field(client):
    data = {
        "user_name": 'test',
        "user_paassword": 'test'
    }

    response = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    assert response.status_code == 415
    assert "error" in response.json


def test_user_authentication_json_user_name_value_not_string(client):
    data = {
        "user_name": 123,
        "user_password": 'test'
    }

    response = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    assert response.status_code == 415
    assert "error" in response.json


def test_user_authentication_json_user_password_value_not_string(client):
    data = {
        "user_name": 'test',
        "user_password": 123
    }

    response = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    assert response.status_code == 415
    assert "error" in response.json


def test_user_manager_template_with_valid_token(app, client, captured_templates):
    data = {
        "user_name": app.config["ADMIN_USER_NAME"],
        "user_password": app.config["ADMIN_PASSWORD"]
    }

    response_authentication = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    cookie_name = app.config["TOKEN_NAME"]
    cookie_value = response_authentication.json["token"]
    client.set_cookie('localhost', cookie_name, cookie_value)

    response = client.get("user/manager")
    template, context = captured_templates[0]

    assert response.status_code == 200
    assert len(captured_templates) == 1
    assert template.name == "user_manager.html"


def test_create_user_without_jwt_token(client):
    data = {
        "user_name": 'TEST',
        "user_email": 'TEST@GMAIL.COM'
    }

    response = client.post(
        "user/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 401
    assert 'error' in response.json


def test_create_new_valid_user(client, app):
    data = {
        "user_name": app.config["ADMIN_USER_NAME"],
        "user_password": app.config["ADMIN_PASSWORD"]
    }

    response_authentication = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    cookie_name = app.config["TOKEN_NAME"]
    cookie_value = response_authentication.json["token"]
    client.set_cookie('localhost', cookie_name, cookie_value)

    data = {
        "user_name": 'TEST',
        "user_email": 'TEST@GMAIL.COM'
    }

    response = client.post(
        "user/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 201
    assert "user" in response.json
    assert response.json["user"][0]["user_name"] == data["user_name"]
    assert response.json["user"][0]["user_email"] == data["user_email"]
    assert response.json["user"][0]["user_status"] == 1
    assert response.json["user"][0]["user_last_modification_user_id"] == app.config["ADMIN_USER_ID"]


def test_create_duplicate_user(client, app):
    data = {
        "user_name": app.config["ADMIN_USER_NAME"],
        "user_password": app.config["ADMIN_PASSWORD"]
    }

    response_authentication = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    cookie_name = app.config["TOKEN_NAME"]
    cookie_value = response_authentication.json["token"]
    client.set_cookie('localhost', cookie_name, cookie_value)

    data = {
        "user_name": 'TEST',
        "user_email": 'TEST@GMAIL.COM'
    }

    response = client.post(
        "user/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_create_user_with_json_field_user_name_wrong(client, app):
    data = {
        "user_name": app.config["ADMIN_USER_NAME"],
        "user_password": app.config["ADMIN_PASSWORD"]
    }

    response_authentication = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    cookie_name = app.config["TOKEN_NAME"]
    cookie_value = response_authentication.json["token"]
    client.set_cookie('localhost', cookie_name, cookie_value)

    data = {
        "user_naame": 'TEST2',
        "user_email": 'TEST2@GMAIL.COM'
    }

    response = client.post(
        "user/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 415
    assert "error" in response.json


def test_create_user_with_json_field_user_email_wrong(client, app):
    data = {
        "user_name": app.config["ADMIN_USER_NAME"],
        "user_password": app.config["ADMIN_PASSWORD"]
    }

    response_authentication = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    cookie_name = app.config["TOKEN_NAME"]
    cookie_value = response_authentication.json["token"]
    client.set_cookie('localhost', cookie_name, cookie_value)

    data = {
        "user_name": 'TEST2',
        "user_eemail": 'TEST2@GMAIL.COM'
    }

    response = client.post(
        "user/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 415
    assert "error" in response.json


def test_create_user_with_json_value_user_name_not_string(client, app):
    data = {
        "user_name": app.config["ADMIN_USER_NAME"],
        "user_password": app.config["ADMIN_PASSWORD"]
    }

    response_authentication = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    cookie_name = app.config["TOKEN_NAME"]
    cookie_value = response_authentication.json["token"]
    client.set_cookie('localhost', cookie_name, cookie_value)

    data = {
        "user_name": 123,
        "user_email": 'TEST2@GMAIL.COM'
    }

    response = client.post(
        "user/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 415
    assert "error" in response.json


def test_create_user_with_json_value_user_email_not_string(client, app):
    data = {
        "user_name": app.config["ADMIN_USER_NAME"],
        "user_password": app.config["ADMIN_PASSWORD"]
    }

    response_authentication = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    cookie_name = app.config["TOKEN_NAME"]
    cookie_value = response_authentication.json["token"]
    client.set_cookie('localhost', cookie_name, cookie_value)

    data = {
        "user_name": 'TEST2',
        "user_email": 123
    }

    response = client.post(
        "user/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 415
    assert "error" in response.json


def test_create_user_with_blank_user_name(client, app):
    data = {
        "user_name": app.config["ADMIN_USER_NAME"],
        "user_password": app.config["ADMIN_PASSWORD"]
    }

    response_authentication = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    cookie_name = app.config["TOKEN_NAME"]
    cookie_value = response_authentication.json["token"]
    client.set_cookie('localhost', cookie_name, cookie_value)

    data = {
        "user_name": '',
        "user_email": 'TESTE2@GMAIL.COM'
    }

    response = client.post(
        "user/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 415
    assert "error" in response.json


def test_create_user_with_invalid_user_email(client, app):
    data = {
        "user_name": app.config["ADMIN_USER_NAME"],
        "user_password": app.config["ADMIN_PASSWORD"]
    }

    response_authentication = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    cookie_name = app.config["TOKEN_NAME"]
    cookie_value = response_authentication.json["token"]
    client.set_cookie('localhost', cookie_name, cookie_value)

    data = {
        "user_name": 'TEST2',
        "user_email": 'abc'
    }

    response = client.post(
        "user/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 400
    assert "error" in response.json


def test_create_user_with_blank_user_email(client, app):
    data = {
        "user_name": app.config["ADMIN_USER_NAME"],
        "user_password": app.config["ADMIN_PASSWORD"]
    }

    response_authentication = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    cookie_name = app.config["TOKEN_NAME"]
    cookie_value = response_authentication.json["token"]
    client.set_cookie('localhost', cookie_name, cookie_value)

    data = {
        "user_name": 'TEST2',
        "user_email": ''
    }

    response = client.post(
        "user/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    assert response.status_code == 415
    assert "error" in response.json


def test_update_user_with_valid_json(app, client):
    data = {
        "user_name": app.config["ADMIN_USER_NAME"],
        "user_password": app.config["ADMIN_PASSWORD"]
    }

    response_authentication = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    cookie_name = app.config["TOKEN_NAME"]
    cookie_value = response_authentication.json["token"]
    client.set_cookie('localhost', cookie_name, cookie_value)

    data = {"user_id": 2,
            "user_name": 'FOO',
            "user_password": 'FOO123',
            "user_email": 'FOO@GMAIL.COM',
            "user_token": 'FOO123',
            "user_status": 1
            }

    response = client.patch(
        "user/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    user_from_db = get_user_by_id(data["user_id"])

    assert response.status_code == 200
    assert "user" in response.json
    assert response.json["user"][0]["user_id"] == data["user_id"]
    assert response.json["user"][0]["user_name"] == data["user_name"]
    assert response.json["user"][0]["user_email"] == data["user_email"]
    assert response.json["user"][0]["user_status"] == data["user_status"]
    assert response.json["user"][0]["user_last_modification_user_id"] == app.config["ADMIN_USER_ID"]
    assert user_from_db.user_token == data["user_token"]
    assert check_password_hash(user_from_db.user_password, data["user_password"])


def test_update_user_with_valid_json_and_only_user_name_updated(app, client):
    data = {
        "user_name": app.config["ADMIN_USER_NAME"],
        "user_password": app.config["ADMIN_PASSWORD"]
    }

    response_authentication = client.post(
        "user/authentication",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"})

    cookie_name = app.config["TOKEN_NAME"]
    cookie_value = response_authentication.json["token"]
    client.set_cookie('localhost', cookie_name, cookie_value)

    data = {"user_id": 2,
            "user_name": 'BOO',
            "user_password": None,
            "user_email": None,
            "user_token": None,
            "user_status": 1
            }

    user_from_db_before_update = get_user_by_id(data["user_id"])

    response = client.patch(
        "user/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"
                 })

    user_from_db_after_update = get_user_by_id(data["user_id"])

    assert response.status_code == 200
    assert "user" in response.json
    assert response.json["user"][0]["user_id"] == data["user_id"]
    assert response.json["user"][0]["user_name"] == data["user_name"]
    assert response.json["user"][0]["user_email"] == user_from_db_before_update.user_email
    assert response.json["user"][0]["user_status"] == data["user_status"]
    assert response.json["user"][0]["user_last_modification_user_id"] == app.config["ADMIN_USER_ID"]
    assert user_from_db_before_update.user_token == user_from_db_after_update.user_token
    assert user_from_db_before_update.user_password == user_from_db_after_update.user_password
