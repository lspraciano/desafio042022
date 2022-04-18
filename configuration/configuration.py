import os


class Configuration:
    HOST = '0.0.0.0'
    PORT = 5001
    SECRET_KEY = 'eb_54okkma5t_=z3z%tazp!xutgfif+3b76(apf-acr6m@71#$'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class DevelopmentConfig(Configuration):
    ...


class ProductionConfig(Configuration):
    ...


app_configuration = {
    'development': DevelopmentConfig(),
    'production': ProductionConfig(),
    'default': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV') or 'default'
