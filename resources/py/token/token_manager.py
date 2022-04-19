# Imports Native
from functools import wraps
import jwt
import datetime
from flask import request, redirect
from random import *

# Created Imports
from configuration.configuration import Configuration


def token_generator(userid: int) -> dict:
    """
    Função geradora do TOKEN JWT de acesso do usuário

    :param userid: ID - Identificação do usuário
    :return: Dicionário contendo TOKEN de acesso no formato {"token": foo}
    """

    payload = {
        "id": userid,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=Configuration.TIME_EXP_TOKEN)
    }
    token = jwt.encode(payload, Configuration.SECRET_KEY)
    return {"token": token}


def refresh_token(token: str) -> bool:
    """
    Função para gerar um novo TOKEN JWT caso o TOKEN em uso esteja próximo de expirar

    :param token: TOKEN JWT do usuário
    :return: True ou False
    """

    decode = jwt.decode(token, Configuration.SECRET_KEY, algorithms=["HS256"])

    time_exp = decode['exp']

    time_limit = datetime.datetime.fromtimestamp(int(time_exp)) - datetime.timedelta(
        minutes=Configuration.LIMIT_EXP_TOKEN)
    time_now = datetime.datetime.now()

    if time_now >= time_limit:
        return True
    else:
        return False


def token_authentication(function):
    """
    Esta função faz a proteção de uma rota através da validação do TOKEN JWT de acesso

    :param function: Função da rota de acesso que deseja proteger
    :return: Function() ou Diconário com erro encontrado na validação
    """

    @wraps(function)
    def wrapper(*args, **kwargs):

        try:
            token_name = Configuration.TOKEN_NAME
            token_from_cookie = request.cookies.get(token_name)
            token_no_bearer = token_from_cookie

        except:
            return redirect('/'), 302

        if token_from_cookie is None:
            return redirect('/'), 302

        try:
            decode = jwt.decode(token_no_bearer, Configuration.SECRET_KEY, algorithms=["HS256"])
            # user_id = decode['id']
            #
            # # if refresh_token(token_no_bearer):
            # #     return token_generator(user_id)

        except:
            return redirect('/'), 302
        return function()

    return wrapper


def user_id_from_token():
    """
    Esta função retorna o ID do usuário que esta solicitando alguma requisição através do seu TOKEN JWT

    :return: Id do usuário ou Dicionário contendo o error
    """

    try:
        token_from_cookie = request.cookies.get('alan_access_token')
        token_no_bearer = token_from_cookie
    except:
        return redirect('/'), 302

    if token_from_cookie is None:
        return redirect('/'), 302

    try:
        decode = jwt.decode(token_no_bearer, Configuration.SECRET_KEY, algorithms=["HS256"])
        user_id = decode['id']
        return user_id

    except:
        return redirect('/'), 302


def mail_token_generate() -> int:
    """
    Esta função gera uma sequência aleatória de 6 números
    :return: sequência de números
    """
    token = randrange(100000, 999999, 2)
    return token
