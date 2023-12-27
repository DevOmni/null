#!/usr/bin/env python
import os
def load_env():
    from dotenv import load_dotenv
    load_dotenv()

try:
    load_env()
except (ImportError, ModuleNotFoundError):
    os.system(f'{"pip" if os.name == "nt" else "pip3"} install dotenv')
    load_env()



# Find the absolute file path to the top level project directory
basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database')

class Config:
    """
    Base configuration class. Contains default configuration settings + configuration settings applicable to all environments.
    """
    # Default settings
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True

    # Settings applicable to all environments
    SECRET_KEY = os.getenv('SECRET_KEY', default='A very terrible secret key.')
    
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 465
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = True
    # MAIL_USERNAME = os.getenv('MAIL_USERNAME', default='InterDotNet@gmail.com')
    # MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', default='password')
    # MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME', default='InterDotNet')
    # MAIL_SUPPRESS_SEND = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    # RESULT_BACKEND = os.getenv('RESULT_BACKEND')
    

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'dev.db')

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    MAIL_SUPPRESS_SEND = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(os.path.join(basedir, 'test'), 'test.db')

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI', default="sqlite:///" + os.path.join(basedir, 'prod.db'))
