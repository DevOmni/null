import datetime

from flask import Flask, render_template, url_for, session, current_app, request
from flask_login import current_user, login_required, confirm_login
from app import sio, db
from app.api import api_bp
from app.core.utils import gen_cell_code
from app.core.models import Cell
from app.core.sock import join_room


@api_bp.route('/create_cell', methods=['POST'])
def create_cell():
    if request.base_url != current_app.root_path:
        return 403
    data = request.data   
    user_limit = data.get('cellUserLimit', None)
    password = data.get('cellPassword', None)
    
    cell_name = ''
    while not Cell.query.filter_by(name=cell_name):
        cell_name = gen_cell_code()
        
    if not current_user.is_authenticated:
        if is_permanent or is_anonymous or is_history or custom_name:
            resp = {
                'cell': None,
                'message': 'Please Login to use all features',
                'error': 'Login required!',
            }
            return resp
        cell = Cell(name=cell_name, creator=current_user)
    else:
        custom_name = data.get('cellCustomName', None)
        is_permanent = data.get('cellLifeState', False)
        is_anonymous = data.get('cellAnonymity', False)
        is_history = data.get('cellHistoryState', False)
        cell = Cell(name=cell_name, password=password, creator=current_user, custom_name=custom_name, 
                    is_permanent=is_permanent, is_anonymous=is_anonymous, is_history=is_history)

    db.session.add(cell)
    db.session.commit()
    cell.usercount += 1
    join_room(cell.name)
    resp = {
        'cell': cell.name,
        'message': 'cell created Successfully',
    }
    return resp


@api_bp.route('/join_cell', methods=['POST'])
def join_cell():
    if request.base_url != current_app.root_path or not request.form:
        return 403
    
    if not current_user.is_authenticated:
        
    resp = {
        'cell': cell.name,
        'message': 'cell joined Successfully',
    }
    return resp
