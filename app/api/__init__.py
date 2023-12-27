from flask.blueprints import Blueprint

api_bp = Blueprint('api', __name__, subdomain='api', template_folder='../templates', static_folder='../static')
