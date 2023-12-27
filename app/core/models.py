from app import app, db
from datetime import datetime
from app.user.models import User
from app.core.utils import gen_cell_code

user_connected = db.Table('user_connected',
                          db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                          db.Column('cell_id', db.Integer, db.ForeignKey('cell.id')),
                          )


class Cell(db.Model):
    __tablename__ = 'cells'
    id = db.Column(db.Integer, primary_key=True)
    # code = db.Column(db.String, )
    name = db.Column(db.String(80), unique=True, nullable=False)
    creator = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=True)
    usercount = db.Column(db.Integer, nullable=True, default=0)
    user_limit = db.Column(db.Integer, nullable=True, default=100)
    connected_users = db.relationship('User', secondary=user_connected, backref='cells')
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    
    # For authorized user
    custom_name = db.Column(db.String(80), nullable=True)
    is_permanent = db.Column(db.Boolean, nullable=False, default=False)
    is_anonymous = db.Column(db.Boolean, nullable=False, default=False)
    is_history = db.Column(db.Boolean, nullable=False, default=False)
    
        
