import time
from . import api_blueprint
from flask import request, jsonify
from app.services import openai_service, pinecone_service, scraping_service
from app.utils.helper_functions import chunk_text, build_prompt
from app.models import *
from sqlalchemy import delete
from flask import render_template
from flask import Blueprint
import json
from app.routes import authenticate

# Sample index name since we're only creating a single index
PINECONE_INDEX_NAME = 'bob7'

user_interface = Blueprint('user_interface', __name__)

@user_interface.route('/user-interface', methods=['GET'])
def user_interface_route():
    return render_template('index.html')


@api_blueprint.route('/handle-query', methods=['POST'])
@authenticate
def handle_query():
    # Extract user_id and question from the request JSON payload
    user_id = request.json['user_id']
    question = request.json['question']

    # Fetch the most similar chunks of context for the question
    context_chunks = pinecone_service.get_most_similar_chunks_for_query(question, PINECONE_INDEX_NAME)
    prompt = build_prompt(question, context_chunks)

    # Get the answer from OpenAI service
    answer = openai_service.get_llm_answer(prompt)

    # Convert the answer JSON string to a dictionary
    api_response = json.loads(answer)

    # Clear data in tables specific to the provided user_id
    db.session.execute(delete(Equipment).where(Equipment.user_id == user_id))
    db.session.execute(delete(Ingredient).where(Ingredient.user_id == user_id))
    db.session.execute(delete(Session).where(Session.user_id == user_id))
    db.session.execute(delete(Menu).where(Menu.user_id == user_id))

    # Commit the deletion
    db.session.commit()

    # Update the user's objective
    objective = api_response.get('objective', '')
    user = User.query.get(user_id)
    if user:
        user.objective = objective
        db.session.add(user)

    # Handle training sessions and exercises for the specific user
    training_sessions = api_response.get('training_sessions_day_by_day', {})

    for day, exercises in training_sessions.items():
        # Create session entry for the specific user
        session = Session(user_id=user_id, day=day, programme=str(exercises))
        db.session.add(session)

    # Handle equipment for the specific user
    equipment = api_response.get('equipment', {})
    for equipment_description in equipment:
        new_equipment = Equipment(user_id=user_id, description=equipment_description)
        db.session.add(new_equipment)

    # Handle meals for the specific user
    meals = api_response.get('meals', {})
    ingredients = api_response.get('ingredients', [])

    for ingredient_name in ingredients:
        # Check if the ingredient already exists for this user
        ingredient = Ingredient.query.filter_by(name=ingredient_name, user_id=user_id).first()
        if not ingredient:
            ingredient = Ingredient(name=ingredient_name, user_id=user_id)
            db.session.add(ingredient)

    for day, meals_info in meals.items():
        for meal_time, meal_name in meals_info.items():
            # Create menu entry for the specific user
            menu = Menu(user_id=user_id, name=meal_name, day=day, type=meal_time)
            db.session.add(menu)

            # Here you can handle menu-ingredient associations if needed
            # For example, associating ingredients with each meal for the specific user

    # Commit all changes to the database
    db.session.commit()

    # Return response
    return jsonify({"question": question, "answer": answer, "status": "Data saved to database successfully"})


@api_blueprint.route('/get-user-data/<int:user_id>', methods=['GET'])
def get_user_data(user_id):
    # Récupérer les données spécifiques à l'utilisateur
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    # Récupérer les sessions d'entraînement pour l'utilisateur
    sessions = Session.query.filter_by(user_id=user_id).all()

    # Récupérer l'équipement pour l'utilisateur
    equipment = Equipment.query.filter_by(user_id=user_id).all()

    # Récupérer les menus pour l'utilisateur
    menus = Menu.query.filter_by(user_id=user_id).all()

    # Récupérer les ingrédients pour l'utilisateur
    ingredients = Ingredient.query.filter_by(user_id=user_id).all()

    # Convertir les données en dictionnaires
    sessions_data = [session.to_dict() for session in sessions]
    equipment_data = [equip.to_dict() for equip in equipment]
    menus_data = [menu.to_dict() for menu in menus]
    ingredients_data = [ingredient.to_dict() for ingredient in ingredients]

    # Préparer la réponse JSON
    response_data = {
        "user": user.to_dict(),
        "sessions": sessions_data,
        "equipment": equipment_data,
        "menus": menus_data,
        "ingredients": ingredients_data
    }

    # Renvoyer la réponse sous forme de JSON
    return jsonify(response_data)





