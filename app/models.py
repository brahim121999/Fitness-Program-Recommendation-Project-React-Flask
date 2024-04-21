from app import db
from sqlalchemy_utils import ChoiceType

from uuid import uuid4
import datetime, enum


# method to generate uuid
def generate_uuid():
    return str(uuid4())


class BaseModel(db.Model):
    __abstract__ = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)


class User(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    contact = db.Column(db.String(100))
    address = db.Column(db.String(255))
    sessions = db.relationship('Session', backref='user', lazy=True)
    equipments = db.relationship('Equipment', backref='user', lazy=True)
    menus = db.relationship('Menu', backref='user', lazy=True)

    def __init__(self, name, email, password, weight=None, height=None, contact=None, address=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.password = password
        self.weight = weight
        self.height = height
        self.contact = contact
        self.address = address


class Session(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    programme = db.Column(db.Text)

    def __init__(self, user_id, programme=None, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
        self.programme = programme


class Equipment(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(255))

    def __init__(self, user_id, description, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
        self.description = description


class Menu(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100))
    how_to_prepare = db.Column(db.Text)
    ingredients = db.relationship('Ingredient', backref='menu', lazy=True)

    def __init__(self, user_id, name, how_to_prepare=None, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
        self.name = name
        self.how_to_prepare = how_to_prepare


class Ingredient(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    name = db.Column(db.String(100))

    def __init__(self, menu_id, name, **kwargs):
        super().__init__(**kwargs)
        self.menu_id = menu_id
        self.name = name