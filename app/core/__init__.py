from flask.blueprints import Blueprint

core_bp = Blueprint('core', __name__,  template_folder='../templates', static_folder='../static')

from . import models
from . import routes
from . import sock
from . import utils
