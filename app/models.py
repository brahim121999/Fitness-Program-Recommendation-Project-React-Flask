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
    sessions = db.relationship('Session', backref='user', lazy=True)

    def __init__(self, name, email, password, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.password = password


class Session(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date)
    objectives = db.relationship('Objective', backref='session', lazy=True)
    equipments = db.relationship('Equipment', backref='session', lazy=True)
    programs = db.relationship('Program', backref='session', lazy=True)

    def __init__(self, user_id, date, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
        self.date = date


class Objective(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    type = db.Column(db.String(100))

    def __init__(self, session_id, type, **kwargs):
        super().__init__(**kwargs)
        self.session_id = session_id
        self.type = type


class Equipment(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    description = db.Column(db.String(255))
    type = db.Column(db.String(100))

    def __init__(self, session_id, description, type, **kwargs):
        super().__init__(**kwargs)
        self.session_id = session_id
        self.description = description
        self.type = type


class Program(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    details = db.Column(db.String(255))

    def __init__(self, session_id, details, **kwargs):
        super().__init__(**kwargs)
        self.session_id = session_id
        self.details = details


class Dish(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    objectives = db.relationship('Objective', secondary='dish_objectives', backref='dishes', lazy='dynamic')

    def __init__(self, name, category, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.category = category


dish_objectives = db.Table('dish_objectives',
                           db.Column('dish_id', db.Integer, db.ForeignKey('dish.id')),
                           db.Column('objective_id', db.Integer, db.ForeignKey('objective.id'))
                           )


class Menu(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    dishes = db.relationship('Dish', secondary='menu_dishes', backref='menus', lazy='dynamic')

    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name


menu_dishes = db.Table('menu_dishes',
                       db.Column('menu_id', db.Integer, db.ForeignKey('menu.id')),
                       db.Column('dish_id', db.Integer, db.ForeignKey('dish.id'))
                       )


class Ingredient(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    calories = db.Column(db.Float)
    carbohydrates = db.Column(db.Float)
    fats = db.Column(db.Float)
    proteins = db.Column(db.Float)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))

    def __init__(self, name, calories, carbohydrates, fats, proteins, menu_id, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.calories = calories
        self.carbohydrates = carbohydrates
        self.fats = fats
        self.proteins = proteins
        self.menu_id = menu_id
