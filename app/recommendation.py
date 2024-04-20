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

    #print(f"Type of answer: {type(answer)}")

    # Convert the answer JSON string to a dictionary
    api_response = json.loads(answer)

    print(api_response)

    # Parse the API response
    user_id = 1  # Assuming user_id is known or can be determined from the context

    # Objective
    objective = api_response.get('objective', '')
    user = User.query.get(user_id)
    if user:
        user.objective = objective
        db.session.add(user)

    # Training Sessions and Exercises
    training_sessions = api_response.get('training_sessions_day_by_day', {})
    how_to_perform_exercises = api_response.get('how_to_perform_exercises', {})

    for day, exercises in training_sessions.items():
        # Create session entry
        session = Session(user_id=user_id, programme=day)
        db.session.add(session)

        # Create equipment entries and descriptions
        for exercise in exercises:
            description = how_to_perform_exercises.get(exercise, '')
            equipment = Equipment(user_id=user_id, description=description)
            db.session.add(equipment)

    # Meals
    meals = api_response.get('meals', {})
    how_to_prepare_meals = api_response.get('how_to_prepare_meals', {})

    for day, meals_info in meals.items():
        for meal_time, meal_name in meals_info.items():
            # Create menu entry
            how_to_prepare = how_to_prepare_meals.get(meal_name, '')
            menu = Menu(user_id=user_id, name=meal_name, how_to_prepare=how_to_prepare)
            db.session.add(menu)

            # Assuming you also want to store the ingredients for each meal
            # Assuming ingredients can be determined and are in a list form

            ingredients = api_response.get('ingredients', {})

            for ingredient_name in ingredients:
                ingredient = Ingredient(menu_id=menu.id, name=ingredient_name)
                db.session.add(ingredient)

    # Commit changes to the database
    db.session.commit()

    # Return response
    return jsonify({"question": question, "answer": answer, "status": "Data saved to database successfully"})

