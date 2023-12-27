from flask.blueprints import Blueprint

user_bp = Blueprint('user', __name__, template_folder='../templates', static_folder='../static')

from . import models
from . import routes
from . import sock
from . import utils
