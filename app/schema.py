from app import app

from app.models import *
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

"""
=============
Schema classes
=============
"""


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')  # Fields to expose


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class SessionSchema(ma.ModelSchema):
    class Meta:
        model = Session
        fields = ('id', 'user_id', 'date', 'objectives', 'equipments', 'programs')  # Fields to expose


session_schema = SessionSchema()
sessions_schema = SessionSchema(many=True)


class ObjectiveSchema(ma.ModelSchema):
    class Meta:
        model = Objective
        fields = ('id', 'session_id', 'type')  # Fields to expose


objective_schema = ObjectiveSchema()
objectives_schema = ObjectiveSchema(many=True)


class EquipmentSchema(ma.ModelSchema):
    class Meta:
        model = Equipment
        fields = ('id', 'session_id', 'description', 'type')  # Fields to expose


equipment_schema = EquipmentSchema()
equipments_schema = EquipmentSchema(many=True)


class ProgramSchema(ma.ModelSchema):
    class Meta:
        model = Program
        fields = ('id', 'session_id', 'details')  # Fields to expose


program_schema = ProgramSchema()
programs_schema = ProgramSchema(many=True)


class DishSchema(ma.ModelSchema):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'category', 'objectives')  # Fields to expose


dish_schema = DishSchema()
dishes_schema = DishSchema(many=True)


class MenuSchema(ma.ModelSchema):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'dishes')  # Fields to expose


menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)


class IngredientSchema(ma.ModelSchema):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'calories', 'carbohydrates', 'fats', 'proteins', 'menu_id')  # Fields to expose


ingredient_schema = IngredientSchema()
ingredients_schema = IngredientSchema(many=True)
