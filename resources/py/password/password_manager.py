import random


def generate_password(length: int = 8) -> str:
    """
    Esta função gera uma senha com número X de caracteres. Caso não informado durante a chamada da função
    o número inicial será de 8.

    :param length: número de caracteres que se deseja a senha
    :return: senha
    """
    char_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    password = ''

    for len in range(length):
        random_char = random.choice(char_seq)
        password += random_char

    list_pass = list(password)
    random.shuffle(list_pass)
    final_password = ''.join(list_pass)
    return final_password
