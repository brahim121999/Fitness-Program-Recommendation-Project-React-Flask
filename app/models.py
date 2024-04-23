from app import db
from sqlalchemy_utils import ChoiceType
from flask_login import UserMixin

from uuid import uuid4
from werkzeug.security import check_password_hash, generate_password_hash


# method to generate uuid
def generate_uuid():
    return str(uuid4())


class BaseModel(db.Model):
    __abstract__ = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)

class User(UserMixin,BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    contact = db.Column(db.String(100))
    address = db.Column(db.String(255))
    objective = db.Column(db.String(255))
    sessions = db.relationship('Session', backref='user', lazy=True)
    equipments = db.relationship('Equipment', backref='user', lazy=True)
    menus = db.relationship('Menu', backref='user', lazy=True)

    def __init__(self, name,username, email, password, weight=None, height=None, contact=None, address=None, objective=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.username=username
        self.email = email
        self.password = password
        self.weight = weight
        self.height = height
        self.contact = contact
        self.address = address
        self.objective = objective

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return self.password == password


class Session(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    programme = db.Column(db.Text)
    day = db.Column(db.Text)

    def __init__(self, user_id, programme=None,day=None, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
        self.programme = programme
        self.day = day


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
    #how_to_prepare = db.Column(db.Text)
    #menu_ingredients_relation = db.relationship('MenuIngredient', backref='menu', lazy=True)
    day = db.Column(db.Text)
    type = db.Column(db.Text) #breakfast or lunch or dinner
    def __init__(self, user_id, name, how_to_prepare=None,day=None,type=None, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
        self.name = name
        self.day = day
        self.type = type



class Ingredient(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #menu_ingredients_relation = db.relationship('MenuIngredient', backref='ingredient', lazy=True)

    def __init__(self, name,user_id, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.user_id = user_id


#class MenuIngredient(BaseModel):
 #   __tablename__ = 'menu_ingredient'
  #  id = db.Column(db.Integer, primary_key=True)
   # menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'), nullable=False)
    #ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)

    #menu_relation = db.relationship('Menu', backref=db.backref('menu_ingredients', cascade='all, delete-orphan'))
    #ingredient_relation = db.relationship('Ingredient', backref=db.backref('menu_ingredients', cascade='all, delete-orphan'))

