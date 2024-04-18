import time
from . import api_blueprint
from flask import request, jsonify
from app.services import openai_service, pinecone_service, scraping_service
from app.utils.helper_functions import chunk_text, build_prompt

# Sample index name since we're only creating a single index
PINECONE_INDEX_NAME = 'bob7'

from flask import render_template
from flask import Blueprint

user_interface = Blueprint('user_interface', __name__)

@user_interface.route('/user-interface', methods=['GET'])
def user_interface_route():
    return render_template('index.html')

@api_blueprint.route('/handle-query', methods=['POST'])
def handle_query():
    # handles embedding the user's question,
    # finding relevant context from the vector database,
    # building the prompt for the LLM,
    # and sending the prompt to the LLM's API to get an answer.

    start_time = time.time()

    question = request.json['question']

    context_chunks = pinecone_service.get_most_similar_chunks_for_query(question, PINECONE_INDEX_NAME)

    prompt = build_prompt(question, context_chunks)

    answer = openai_service.get_llm_answer(prompt)

    end_time = time.time()

    execution_time = end_time - start_time

    print(f"Execution time: {execution_time} seconds")

    with open("test2.txt", "w") as my_file:
      my_file.write(answer)

    return jsonify({"question": question, "answer": answer})
