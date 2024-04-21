from flask_marshmallow import Marshmallow
from app.models import *

# Initialize Marshmallow
ma = Marshmallow()

# Define Marshmallow Schemas here...

"""
=============
Schema classes
=============
"""

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'weight', 'height', 'contact', 'address')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class SessionSchema(ma.ModelSchema):
    class Meta:
        model = Session
        fields = ('id', 'user_id', 'programme','day')


session_schema = SessionSchema()
sessions_schema = SessionSchema(many=True)


class EquipmentSchema(ma.ModelSchema):
    class Meta:
        model = Equipment
        fields = ('id', 'user_id', 'description')


equipment_schema = EquipmentSchema()
equipments_schema = EquipmentSchema(many=True)


class MenuSchema(ma.ModelSchema):
    class Meta:
        model = Menu
        fields = ('id', 'user_id', 'name','day','type')
    #menu_ingredients_relation = ma.Nested('MenuIngredientSchema', many=True)

class IngredientSchema(ma.ModelSchema):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')
    #menu_ingredients_relation = ma.Nested('MenuIngredientSchema', many=True)




menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)

ingredient_schema = IngredientSchema()
ingredients_schema = IngredientSchema(many=True)

#class MenuIngredientSchema(ma.ModelSchema):
  #  class Meta:
   #     model = MenuIngredient
    #    fields = ('id', 'menu_id', 'ingredient_id')

#menu_ingredient_schema = MenuIngredientSchema()
#menu_ingredients_schema = MenuIngredientSchema(many=True)
