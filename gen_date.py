import random

def create_random_email():
    random_email = f'nikita_ermakov_17_{random.randint(100,999)}@yandex.ru'
    return random_email

def create_random_password():
    random_password = f'{random.randint(100000, 999999)}'
    return random_password