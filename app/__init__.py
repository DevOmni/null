from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

sio = SocketIO()
db = SQLAlchemy()
login_m = LoginManager()

from . import core
from . import api
from . import user

from .core import core_bp
from .api import api_bp
from .user import user_bp


# Application Factory #
def create_app():
    # Configure the flask app instance
    # CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    # app.config.from_object(CONFIG_TYPE)

    # Register blueprints
    register_blueprints(app)

    # Initialize flask extension objects
    initialize_extensions(app)

    # Configure logging
    configure_logging(app)

    # Register error handlers
    register_error_handlers(app)

    return sio, app


# Helper Functions #
def register_blueprints(app):
    app.register_blueprint(core_bp, url_prefix='/')
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(user_bp, url_prefix='/users')


def initialize_extensions(app):
    # mail.init_app(app)
    sio.init_app(app)
    db.init_app(app)
    login_m.init_app(app)


def register_error_handlers(app):
    pass


def configure_logging(app):
    pass
