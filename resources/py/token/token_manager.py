# Imports Native
from functools import wraps
import jwt
import datetime
from flask import request, redirect, make_response, url_for
from random import *

# Created Imports
from configuration.configuration import Configuration


def token_generator(userid: int) -> dict:
    """
    Função geradora do TOKEN JWT de acesso do usuário. Este TOKEN deve ser armazenado nos cookies como local
    padrão

    :param userid: ID - identificação do usuário
    :return: dicionário contendo TOKEN de acesso no formato {"token": foo}
    """

    payload = {
        "id": userid,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=Configuration.TIME_EXP_TOKEN)
    }
    token = jwt.encode(payload, Configuration.SECRET_KEY)
    return {"token": token}


def token_authentication(function):
    """
    Esta função faz a proteção de uma rota através da validação do TOKEN JWT de acesso.

    :param function: função da rota de acesso que deseja proteger
    :return: Function() ou Diconário com erro encontrado na validação
    """

    @wraps(function)
    def wrapper(*args, **kwargs):

        try:
            token_name = Configuration.TOKEN_NAME
            token_from_cookie = request.cookies.get(token_name)
            token_no_bearer = token_from_cookie

        except:
            return make_response(redirect(url_for('user.user_authentication')), 302)

        if token_from_cookie is None:
            return make_response(redirect(url_for('user.user_authentication')), 302)

        try:
            decode = jwt.decode(token_no_bearer, Configuration.SECRET_KEY, algorithms=["HS256"])
        except:
            return make_response(redirect(url_for('user.user_authentication')), 302)
        return function()

    return wrapper


def user_id_from_token():
    """
    Esta função retorna o ID do usuário que esta solicitando alguma requisição através do seu TOKEN JWT

    :return: ID do usuário ou Dicionário contendo o error
    """

    try:
        token_name = Configuration.TOKEN_NAME
        token_from_cookie = request.cookies.get(token_name)
        token_no_bearer = token_from_cookie

        if token_from_cookie is None:
            return make_response(redirect(url_for('user.user_authentication')), 302)

        decode = jwt.decode(token_no_bearer, Configuration.SECRET_KEY, algorithms=["HS256"])
        user_id = decode['id']
        return user_id

    except:
        return make_response(redirect(url_for('user.user_authentication')), 302)


def mail_token_generate() -> int:
    """
    Esta função gera uma sequência aleatória de 6 números que pode variar entre 100000 e 999999

    :return: número
    """
    token = randrange(100000, 999999, 2)
    return token
