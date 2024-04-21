from flask import Blueprint, request, jsonify, make_response
from app.models import db, User, Session, Equipment, Menu, Ingredient
from app.schema import user_schema, users_schema, session_schema, sessions_schema, equipment_schema, equipments_schema, \
    menu_schema, menus_schema, ingredient_schema, ingredients_schema
from . import app
#from werkzeug.security import generate_password_hash, check_password_hash
#from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api_blueprint = Blueprint('api', __name__)

"""
===========================
Endpoints for User CRUD
===========================
"""


# Endpoint to CREATE user
@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    result = user_schema.dump(new_user)
    return make_response(jsonify({'message': 'New User Created!', 'status': 201, 'data': result}))


# Endpoint to GET all users
@app.route("/user", methods=["GET"])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return make_response(jsonify({'message': 'All Users!', 'status': 200, 'data': result}))


# Endpoint to GET user detail by id
@app.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    if user:
        result = user_schema.dump(user)
        return make_response(jsonify({'message': 'User Info!', 'status': 200, 'data': result}))
    else:
        return make_response(jsonify({'message': 'Invalid User ID!', 'status': 404}))


# Endpoint to UPDATE user
@app.route("/user/<int:id>", methods=["PATCH"])
def update_user(id):
    user = User.query.get(id)
    if user:
        data = request.json
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        result = user_schema.dump(user)
        return make_response(jsonify({'message': 'User Info Edited!', 'status': 200, 'data': result}))
    else:
        return make_response(jsonify({'message': 'Invalid User ID!', 'status': 404}))


# Endpoint to DELETE user
@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return make_response(jsonify({'message': 'User Deleted!', 'status': 200}))
    else:
        return make_response(jsonify({'message': 'Invalid User ID!', 'status': 404}))


"""
===========================
Endpoints for Session CRUD
===========================
"""


# Endpoint to CREATE session
@app.route("/session", methods=["POST"])
def create_session():
    data = request.json
    new_session = Session(**data)
    db.session.add(new_session)
    db.session.commit()
    result = session_schema.dump(new_session)
    return make_response(jsonify({'message': 'New Session Created!', 'status': 201, 'data': result}))


# Endpoint to GET all sessions
@app.route("/session", methods=["GET"])
def get_sessions():
    all_sessions = Session.query.all()
    result = sessions_schema.dump(all_sessions)
    return make_response(jsonify({'message': 'All Sessions!', 'status': 200, 'data': result}))


# Endpoint to GET session detail by id
@app.route("/session/<int:id>", methods=["GET"])
def get_session(id):
    session = Session.query.get(id)
    if session:
        result = session_schema.dump(session)
        return make_response(jsonify({'message': 'Session Info!', 'status': 200, 'data': result}))
    else:
        return make_response(jsonify({'message': 'Invalid Session ID!', 'status': 404}))


# Endpoint to UPDATE session
@app.route("/session/<int:id>", methods=["PATCH"])
def update_session(id):
    session = Session.query.get(id)
    if session:
        data = request.json
        for key, value in data.items():
            setattr(session, key, value)
        db.session.commit()
        result = session_schema.dump(session)
        return make_response(jsonify({'message': 'Session Info Edited!', 'status': 200, 'data': result}))
    else:
        return make_response(jsonify({'message': 'Invalid Session ID!', 'status': 404}))


# Endpoint to DELETE session
@app.route("/session/<int:id>", methods=["DELETE"])
def delete_session(id):
    session = Session.query.get(id)
    if session:
        db.session.delete(session)
        db.session.commit()
        return make_response(jsonify({'message': 'Session Deleted!', 'status': 200}))
    else:
        return make_response(jsonify({'message': 'Invalid Session ID!', 'status': 404}))


# Other CRUD endpoints for Equipment, Menu, Ingredient, etc. can be similarly defined here...

# Other CRUD endpoints for Equipment, Menu, Ingredient, etc. can be similarly defined here...

"""
===========================
Endpoints for Equipment CRUD
===========================
"""


# Endpoint to CREATE equipment
@app.route("/equipment", methods=["POST"])
def create_equipment():
    data = request.json
    new_equipment = Equipment(**data)
    db.session.add(new_equipment)
    db.session.commit()
    result = equipment_schema.dump(new_equipment)
    return make_response(jsonify({'message': 'New Equipment Created!', 'status': 201, 'data': result}))


# Endpoint to GET all equipments
@app.route("/equipment", methods=["GET"])
def get_equipments():
    all_equipments = Equipment.query.all()
    result = equipments_schema.dump(all_equipments)
    return make_response(jsonify({'message': 'All Equipments!', 'status': 200, 'data': result}))


# Endpoint to GET equipment detail by id
@app.route("/equipment/<int:id>", methods=["GET"])
def get_equipment(id):
    equipment = Equipment.query.get(id)
    if equipment:
        result = equipment_schema.dump(equipment)
        return make_response(jsonify({'message': 'Equipment Info!', 'status': 200, 'data': result}))
    else:
        return make_response(jsonify({'message': 'Invalid Equipment ID!', 'status': 404}))


# Endpoint to UPDATE equipment
@app.route("/equipment/<int:id>", methods=["PATCH"])
def update_equipment(id):
    equipment = Equipment.query.get(id)
    if equipment:
        data = request.json
        for key, value in data.items():
            setattr(equipment, key, value)
        db.session.commit()
        result = equipment_schema.dump(equipment)
        return make_response(jsonify({'message': 'Equipment Info Edited!', 'status': 200, 'data': result}))
    else:
        return make_response(jsonify({'message': 'Invalid Equipment ID!', 'status': 404}))


# Endpoint to DELETE equipment
@app.route("/equipment/<int:id>", methods=["DELETE"])
def delete_equipment(id):
    equipment = Equipment.query.get(id)
    if equipment:
        db.session.delete(equipment)
        db.session.commit()
        return make_response(jsonify({'message': 'Equipment Deleted!', 'status': 200}))
    else:
        return make_response(jsonify({'message': 'Invalid Equipment ID!', 'status': 404}))


# Endpoint to CREATE menu
@app.route("/menu", methods=["POST"])
def create_menu():
    data = request.json
    new_menu = Menu(**data)

    # If ingredients are provided, associate them with the menu
    if 'ingredients' in data:
        for ingredient_id in data['ingredients']:
            ingredient = Ingredient.query.get(ingredient_id)
            if ingredient:
                new_menu.ingredients.append(ingredient)

    db.session.add(new_menu)
    db.session.commit()
    result = menu_schema.dump(new_menu)
    return make_response(jsonify({'message': 'New Menu Created!', 'status': 201, 'data': result}))

# Endpoint to UPDATE menu
@app.route("/menu/<int:id>", methods=["PATCH"])
def update_menu(id):
    menu = Menu.query.get(id)
    if menu:
        data = request.json

        # Update menu fields
        for key, value in data.items():
            setattr(menu, key, value)

        # Handle ingredients association
        if 'ingredients' in data:
            menu.ingredients.clear()  # Clear existing associations
            for ingredient_id in data['ingredients']:
                ingredient = Ingredient.query.get(ingredient_id)
                if ingredient:
                    menu.ingredients.append(ingredient)

        db.session.commit()
        result = menu_schema.dump(menu)
        return make_response(jsonify({'message': 'Menu Info Edited!', 'status': 200, 'data': result}))
    else:
        return make_response(jsonify({'message': 'Invalid Menu ID!', 'status': 404}))

# Endpoint to DELETE menu
@app.route("/menu/<int:id>", methods=["DELETE"])
def delete_menu(id):
    menu = Menu.query.get(id)
    if menu:
        db.session.delete(menu)
        db.session.commit()
        return make_response(jsonify({'message': 'Menu Deleted!', 'status': 200}))
    else:
        return make_response(jsonify({'message': 'Invalid Menu ID!', 'status': 404}))

# Endpoint to CREATE ingredient
@app.route("/ingredient", methods=["POST"])
def create_ingredient():
    data = request.json
    new_ingredient = Ingredient(**data)

    # If menus are provided, associate the ingredient with them
    if 'menus' in data:
        for menu_id in data['menus']:
            menu = Menu.query.get(menu_id)
            if menu:
                new_ingredient.menus.append(menu)

    db.session.add(new_ingredient)
    db.session.commit()
    result = ingredient_schema.dump(new_ingredient)
    return make_response(jsonify({'message': 'New Ingredient Created!', 'status': 201, 'data': result}))

# Endpoint to UPDATE ingredient
@app.route("/ingredient/<int:id>", methods=["PATCH"])
def update_ingredient(id):
    ingredient = Ingredient.query.get(id)
    if ingredient:
        data = request.json

        # Update ingredient fields
        for key, value in data.items():
            setattr(ingredient, key, value)

        # Handle menus association
        if 'menus' in data:
            ingredient.menus.clear()  # Clear existing associations
            for menu_id in data['menus']:
                menu = Menu.query.get(menu_id)
                if menu:
                    ingredient.menus.append(menu)

        db.session.commit()
        result = ingredient_schema.dump(ingredient)
        return make_response(jsonify({'message': 'Ingredient Info Edited!', 'status': 200, 'data': result}))
    else:
        return make_response(jsonify({'message': 'Invalid Ingredient ID!', 'status': 404}))

# Endpoint to DELETE ingredient
@app.route("/ingredient/<int:id>", methods=["DELETE"])
def delete_ingredient(id):
    ingredient = Ingredient.query.get(id)
    if ingredient:
        db.session.delete(ingredient)
        db.session.commit()
        return make_response(jsonify({'message': 'Ingredient Deleted!', 'status': 200}))
    else:
        return make_response(jsonify({'message': 'Invalid Ingredient ID!', 'status': 404}))


# Endpoint for user login
#@app.route("/login", methods=["POST"])
#def login():
 #   data = request.json
  #  email = data.get('email')
   # password = data.get('password')

    #user = User.query.filter_by(email=email).first()

    #if user and check_password_hash(user.password, password):
     #   access_token = create_access_token(identity=email)
      #  return make_response(jsonify({'access_token': access_token}), 200)
    #else:
     #   return make_response(jsonify({'message': 'Invalid email or password'}), 401)

# Protected route example
#@app.route("/protected", methods=["GET"])
#@jwt_required()
#def protected():
#   current_user = get_jwt_identity()
 #   return jsonify(logged_in_as=current_user), 200