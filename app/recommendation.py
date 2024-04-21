import time
from . import api_blueprint
from flask import request, jsonify
from app.services import openai_service, pinecone_service, scraping_service
from app.utils.helper_functions import chunk_text, build_prompt
from app.models import *

# Sample index name since we're only creating a single index
PINECONE_INDEX_NAME = 'bob7'

from flask import render_template
from flask import Blueprint
import json

user_interface = Blueprint('user_interface', __name__)

@user_interface.route('/user-interface', methods=['GET'])
def user_interface_route():
    return render_template('index.html')


@api_blueprint.route('/handle-query', methods=['POST'])
def handle_query():
    # Handle user's query and get the response
    question = request.json['question']
    context_chunks = pinecone_service.get_most_similar_chunks_for_query(question, PINECONE_INDEX_NAME)
    prompt = build_prompt(question, context_chunks)
    answer = openai_service.get_llm_answer(prompt)

    with open("test2.txt", "w") as my_file:
        my_file.write(answer)

    # Convert the answer JSON string to a dictionary
    api_response = json.loads(answer)

    user_id = 1

    # Objective
    objective = api_response.get('objective', '')
    user = User.query.get(user_id)
    if user:
        user.objective = objective
        db.session.add(user)

    # Training Sessions and Exercises
    training_sessions = api_response.get('training_sessions_day_by_day', {})


    for day, exercises in training_sessions.items():
        # Check if the session already exists
        session_exists = Session.query.filter_by(user_id=user_id, day=day, programme=str(exercises)).first()
        if not session_exists:
            # Create session entry
            session = Session(user_id=user_id, day=day, programme=str(exercises))
            db.session.add(session)

    equipment = api_response.get('equipment', {})
    for i in equipment:
        # Check if the equipment already exists
        equipment_exists = Equipment.query.filter_by(user_id=user_id, description=i).first()
        if not equipment_exists:
            equipment = Equipment(user_id=user_id, description=i)
            db.session.add(equipment)

    # Meals
    meals = api_response.get('meals', {})
    ingredients = api_response.get('ingredients', [])  # Get all ingredients

    for ingredient_name in ingredients:
        # Check if the ingredient already exists
        ingredient_exists = Ingredient.query.filter_by(name=ingredient_name).first()
        if not ingredient_exists:
            # Create ingredient entry
            ingredient = Ingredient(name=ingredient_name)
            db.session.add(ingredient)

    for day, meals_info in meals.items():
        for meal_time, meal_name in meals_info.items():
            # Check if the menu already exists
            menu_exists = Menu.query.filter_by(user_id=user_id, name=meal_name, day=day, type=meal_time).first()
            if not menu_exists:
                # Create menu entry
                menu = Menu(user_id=user_id, name=meal_name, day=day, type=meal_time)
                db.session.add(menu)

                # Store ingredients for each meal
                # meal_ingredients = ingredients  # Get ingredients for this meal
                # for ingredient_name in meal_ingredients:
                #     # Create ingredient entry
                #     ingredient = Ingredient(name=ingredient_name)
                #     db.session.add(ingredient)
                #     db.session.commit()  # Commit here to get the ingredient id
                #
                #     # Create MenuIngredient entry
                #     menu_ingredient = MenuIngredient(menu_id=menu.id, ingredient_id=ingredient.id)
                #     db.session.add(menu_ingredient)

    # Commit changes to the database
    db.session.commit()

    # Return response
    return jsonify({"question": question, "answer": answer, "status": "Data saved to database successfully"})




