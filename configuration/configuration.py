import os


class Configuration:
    HOST = '0.0.0.0'
    PORT = 5001
    SECRET_KEY = 'eb_54okkma5t_=z3z%tazp!xutgfif+3b76(apf-acr6m@71#$'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TIME_EXP_TOKEN = 30  # minutes
    LIMIT_EXP_TOKEN = 1  # minutes


class DevelopmentConfig(Configuration):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Vish_123123@127.0.0.1:5432/desafio042022'


class ProductionConfig(Configuration):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Vish_123123@127.0.0.1:5432/desafio042022'


app_configuration = {
    'development': DevelopmentConfig(),
    'production': ProductionConfig(),
    'default': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV') or 'default'
