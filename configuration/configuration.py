import os
from dotenv import load_dotenv

load_dotenv()


class Configuration:
    HOST = '0.0.0.0'
    PORT = 5001
    TEMPLATES_AUTO_RELOAD = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TOKEN_NAME = 'new_app'  # Name of Cookie to set to the browser
    TIME_EXP_TOKEN = 30  # Time in minutes of JWT token
    LIMIT_EXP_TOKEN = 1  # Time in minutes of JWT token to expire
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')


class DevelopmentConfig(Configuration):
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_SQLALCHEMY_DATABASE_URI')


class ProductionConfig(Configuration):
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_SQLALCHEMY_DATABASE_URI')


app_configuration = {
    'development': DevelopmentConfig(),
    'production': ProductionConfig(),
    'default': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV') or 'default'
