# cd venv/scripts && activate && cd ../..
# from app import sio
from flask import Flask, render_template, url_for, session, current_app, request
from app import db
from app.core import core_bp
from app.core.utils import gen_cell_code
from app.user.models import User
from flask_login import current_user, login_required, confirm_login


# @main_bp.route('/yo')
@core_bp.route('/')
def home():
    # if current_user.is_authenticated or True:
    #     print(session , current_user, 'Not authenticated')
    return render_template('home.html')

