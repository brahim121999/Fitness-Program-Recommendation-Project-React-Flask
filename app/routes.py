from flask import Blueprint, request, jsonify, make_response
from app.models import db, User, Session, Equipment, Menu, Ingredient
from app.schema import user_schema, session_schema, sessions_schema, equipment_schema, equipments_schema, menu_schema, \
    ingredient_schema, users_schema
from . import app
from functools import wraps
from flask import request, jsonify
from flask_mail import Mail, Message

api_blueprint = Blueprint('api', __name__)
mail = Mail()


# Fonction pour envoyer un e-mail de réinitialisation de mot de passe
def send_password_reset_email(user):
    # Générez un lien de réinitialisation de mot de passe unique
    # Ceci est un exemple, vous pouvez utiliser une méthode différente pour générer le lien
    reset_link = f"http://yourwebsite.com/reset-password?token={user.password_reset_token}"

    # Créez un message e-mail
    msg = Message("Password Reset Request", recipients=[user.email])

    # Corps de l'e-mail
    msg.body = f"Bonjour {user.username},\n\nPour réinitialiser votre mot de passe, veuillez suivre ce lien : {reset_link}\n\nCordialement,\nVotre équipe de support"

    # Envoyez l'e-mail
    mail.send(msg)

class User(db.Model):
    def check_password(self, password):
        # Comparez le mot de passe hashé stocké dans la base de données avec le mot de passe fourni
        # Vous pouvez utiliser une méthode de hachage sécurisée comme bcrypt pour cela
        # Assurez-vous d'installer bcrypt avec pip install bcrypt
        return password == self.password

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Vérifiez les identifiants de connexion, par exemple :
    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        # Créez une session de connexion ou un token JWT et renvoyez-le comme réponse
        # Exemple :
        # session_token = generate_session_token(user)
        # return jsonify({'message': 'Login successful!', 'status': 200, 'session_token': session_token})
        return make_response(jsonify({'message': 'Login successful!', 'status': 200}))

    # Si les identifiants sont incorrects
    return make_response(jsonify({'message': 'Invalid email or password!', 'status': 401}))

# Endpoint for forgot password
@app.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.json
    email = data.get('email')

    # Vérifiez si l'email existe dans la base de données
    user = User.query.filter_by(email=email).first()

    if user:
        # Générez et envoyez un lien de réinitialisation de mot de passe par e-mail
        # Exemple :
        # send_password_reset_email(user)
        return make_response(jsonify({'message': 'Password reset instructions sent to your email!', 'status': 200}))

    # Si l'email n'existe pas dans la base de données
    return make_response(jsonify({'message': 'Email not found!', 'status': 404}))


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username and auth.password:
            user = User.query.filter_by(username=auth.username).first()
            if user and user.password==auth.password:
                return func(*args, **kwargs)
        return jsonify({'message': 'Unauthorized', 'status': 401}), 401

    return wrapper


@app.route("/user", methods=["GET"])
@authenticate
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return make_response(jsonify({'message': 'All Users!', 'status': 200, 'data': result}))

# Endpoint to CREATE user
@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    result = user_schema.dump(new_user)
    return make_response(jsonify({'message': 'New User Created!', 'status': 201, 'data': result}))

@app.route("/user/<int:id>", methods=["GET"])
@authenticate
def get_user(id):
    user = User.query.get(id)
    if user:
        result = user_schema.dump(user)
        return make_response(jsonify({'message': 'User Info!', 'status': 200, 'data': result}))
    else:
        return make_response(jsonify({'message': 'Invalid User ID!', 'status': 404}))


@app.route("/user/<int:id>", methods=["PATCH"])
@authenticate
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


@app.route("/user/<int:id>", methods=["DELETE"])
@authenticate
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return make_response(jsonify({'message': 'User Deleted!', 'status': 200}))
    else:
        return make_response(jsonify({'message': 'Invalid User ID!', 'status': 404}))


@app.route("/session", methods=["POST"])
@authenticate
def create_session():
    data = request.json
    new_session = Session(**data)
    db.session.add(new_session)
    db.session.commit()
    result = session_schema.dump(new_session)
    return make_response(jsonify({'message': 'New Session Created!', 'status': 201, 'data': result}))


@app.route("/session", methods=["GET"])
@authenticate
def get_sessions():
    all_sessions = Session.query.all()
    result = sessions_schema.dump(all_sessions)
    return make_response(jsonify({'message': 'All Sessions!', 'status': 200, 'data': result}))


@app.route("/session/<int:id>", methods=["GET"])
@authenticate
def get_session(id):
    session = Session.query.get(id)
    if session:
        result = session_schema.dump(session)
        return make_response(jsonify({'message': 'Session Info!', 'status': 200, 'data': result}))
    else:
        return make_response(jsonify({'message': 'Invalid Session ID!', 'status': 404}))


@app.route("/session/<int:id>", methods=["PATCH"])
@authenticate
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


@app.route("/session/<int:id>", methods=["DELETE"])
@authenticate
def delete_session(id):
    session = Session.query.get(id)
    if session:
        db.session.delete(session)
        db.session.commit()
        return make_response(jsonify({'message': 'Session Deleted!', 'status': 200}))
    else:
        return make_response(jsonify({'message': 'Invalid Session ID!', 'status': 404}))


@app.route("/equipment", methods=["POST"])
@authenticate
def create_equipment():
    data = request.json
    new_equipment = Equipment(**data)
    db.session.add(new_equipment)
    db.session.commit()
    result = equipment_schema.dump(new_equipment)
    return make_response(jsonify({'message': 'New Equipment Created!', 'status': 201, 'data': result}))


@app.route("/equipment", methods=["GET"])
@authenticate
def get_equipments():
    all_equipments = Equipment.query.all()
    result = equipments_schema.dump(all_equipments)
    return make_response(jsonify({'message': 'All Equipments!', 'status': 200, 'data': result}))


@app.route("/equipment/<int:id>", methods=["GET"])
@authenticate
def get_equipment(id):
    equipment = Equipment.query.get(id)
    if equipment:
        result = equipment_schema.dump(equipment)
        return make_response(jsonify({'message': 'Equipment Info!', 'status': 200, 'data': result}))
    else:
        return make_response(jsonify({'message': 'Invalid Equipment ID!', 'status': 404}))


@app.route("/equipment/<int:id>", methods=["PATCH"])
@authenticate
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


@app.route("/equipment/<int:id>", methods=["DELETE"])
@authenticate
def delete_equipment(id):
    equipment = Equipment.query.get(id)
    if equipment:
        db.session.delete(equipment)
        db.session.commit()
        return make_response(jsonify({'message': 'Equipment Deleted!', 'status': 200}))
    else:
        return make_response(jsonify({'message': 'Invalid Equipment ID!', 'status': 404}))


@app.route("/menu", methods=["POST"])
@authenticate
def create_menu():
    data = request.json
    new_menu = Menu(**data)

    if 'ingredients' in data:
        for ingredient_id in data['ingredients']:
            ingredient = Ingredient.query.get(ingredient_id)
            if ingredient:
                new_menu.ingredients.append(ingredient)

    db.session.add(new_menu)
    db.session.commit()
    result = menu_schema.dump(new_menu)
    return make_response(jsonify({'message': 'New Menu Created!', 'status': 201, 'data': result}))


@app.route("/menu/<int:id>", methods=["PATCH"])
@authenticate
def update_menu(id):
    menu = Menu.query.get(id)
    if menu:
        data = request.json

        for key, value in data.items():
            setattr(menu, key, value)

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


@app.route("/menu/<int:id>", methods=["DELETE"])
@authenticate
def delete_menu(id):
    menu = Menu.query.get(id)
    if menu:
        db.session.delete(menu)
        db.session.commit()
        return make_response(jsonify({'message': 'Menu Deleted!', 'status': 200}))
    else:
        return make_response(jsonify({'message': 'Invalid Menu ID!', 'status': 404}))


@app.route("/ingredient", methods=["POST"])
@authenticate
def create_ingredient():
    data = request.json
    new_ingredient = Ingredient(**data)

    if 'menus' in data:
        for menu_id in data['menus']:
            menu = Menu.query.get(menu_id)
            if menu:
                new_ingredient.menus.append(menu)

    db.session.add(new_ingredient)
    db.session.commit()
    result = ingredient_schema.dump(new_ingredient)
    return make_response(jsonify({'message': 'New Ingredient Created!', 'status': 201, 'data': result}))


@app.route("/ingredient/<int:id>", methods=["PATCH"])
@authenticate
def update_ingredient(id):
    ingredient = Ingredient.query.get(id)
    if ingredient:
        data = request.json

        for key, value in data.items():
            setattr(ingredient, key, value)

        if 'menus' in data:
            ingredient.menus.clear()
            for menu_id in data['menus']:
                menu = Menu.query.get(menu_id)
                if menu:
                    ingredient.menus.append(menu)

        db.session.commit()
        result = ingredient_schema.dump(ingredient)
        return make_response(jsonify({'message': 'Ingredient Info Edited!', 'status': 200, 'data': result}))
    else:
        return make_response(jsonify({'message': 'Invalid Ingredient ID!', 'status': 404}))


@app.route("/ingredient/<int:id>", methods=["DELETE"])
@authenticate
def delete_ingredient(id):
    ingredient = Ingredient.query.get(id)
    if ingredient:
        db.session.delete(ingredient)
        db.session.commit()
        return make_response(jsonify({'message': 'Ingredient Deleted!', 'status': 200}))
    else:
        return make_response(jsonify({'message': 'Invalid Ingredient ID!', 'status': 404}))
