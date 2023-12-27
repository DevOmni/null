from app import app, db, login_m
from datetime import datetime
from flask_login import UserMixin


@login_m.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=user_id)
    return user


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

