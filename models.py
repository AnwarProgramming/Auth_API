from database import db
from flask_security import UserMixin, RoleMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String(200), unique = True, nullable = False)
    email = db.Column(db.String(200), unique = True, nullable = False)
    password = db.Column(db.String(150), nullable = False)
    active = db.Column(db.Boolean(), default = True)

    fs_token_uniquifier = db.Column(db.String(300), unique = True, nullable = False)
    fs_uniquifier = db.Column(db.String(300), unique =True, nullable = False)

    roles = db.relationship('Roles', secondary = 'user_roles', backref = db.backref('users', lazy = 'dynamic'))

class Roles(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(300), unique = True, nullable = False)
    description = db.Column(db.String(300), nullable = False)

class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable = False)

class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(300), nullable = False)
    description = db.Column(db.String(300), nullable = False)
    price = db.Column(db.Float, nullable = False)
    stock = db.Column(db.Integer, nullable = False)

