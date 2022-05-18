# Imports Native
import jwt

# Created Imports
from resources.py.token.token_manager import token_generator, token_authentication, user_id_from_token, \
    mail_token_generate


def test_token_generator_with_valid_parameter_int(app):
    expected_user_id = 1
    dict_token_jwt = token_generator(user_id=expected_user_id)
    token_from_dict = dict_token_jwt['token']
    decode = jwt.decode(token_from_dict, app.config['SECRET_KEY'], algorithms=["HS256"])
    assert expected_user_id == decode['id']


def test_token_generator_with_invalid_parameter_str(app):
    expected_user_id = '1'
    dict_token_jwt = token_generator(user_id=expected_user_id)
    if 'error' in dict_token_jwt:
        assert True
    else:
        assert False


def test_token_generator_with_invalid_parameter_float(app):
    expected_user_id = 1.5
    dict_token_jwt = token_generator(user_id=expected_user_id)
    if 'error' in dict_token_jwt:
        assert True
    else:
        assert False


def test_token_generator_with_invalid_parameter_none(app):
    expected_user_id = None
    dict_token_jwt = token_generator(user_id=expected_user_id)
    if 'error' in dict_token_jwt:
        assert True
    else:
        assert False
