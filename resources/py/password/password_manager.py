import random

char_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


def generate_password(length: int = 8) -> str:
    password = ''
    for len in range(length):
        random_char = random.choice(char_seq)
        password += random_char

    # print(password)
    list_pass = list(password)
    random.shuffle(list_pass)
    final_password = ''.join(list_pass)
    return final_password
