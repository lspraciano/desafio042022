import os


class Configuration:
    HOST = '0.0.0.0'
    PORT = 5001
    TEMPLATES_AUTO_RELOAD = True
    SECRET_KEY = 'eb_54okkma5t_=z3z%tazp!xutgfif+3b76(apf-acr6m@71#$'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TOKEN_NAME = 'new_app'
    TIME_EXP_TOKEN = 30  # Time in minutes of JWT token
    LIMIT_EXP_TOKEN = 1  # Time in minutes of JWT token to expire


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
