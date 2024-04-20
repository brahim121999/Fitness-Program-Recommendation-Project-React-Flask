import requests
from openai import OpenAI
import json
import os
from dotenv import load_dotenv


def chunk_text(text, chunk_size=200):
    # Split the text by sentences to avoid breaking in the middle of a sentence
    sentences = text.split('. ')
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        # Check if adding the next sentence exceeds the chunk size
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += sentence + '. '
        else:
            # If the chunk reaches the desired size, add it to the chunks list
            chunks.append(current_chunk)
            current_chunk = sentence + '. '
    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(current_chunk)
    return chunks


PROMPT_LIMIT = 999999


def build_prompt(query, context_chunks):
    # create the start and end of the prompt
    prompt_start = (
        # "Answer the question based on the context below. \n\n"+
        # "Context:\n"
        "Based on the provided list of materials, ingredients, training objectives, and the specified number of"
        "training"
        "sessions per week and using the data i provided you via pincone, "
        "please create a detailed training program, the training program should respect exactly the "
        "given number of training times per week, the sessions should contain  multiple and variated exercises (at least"
        "three per session) "
        "that must be realised only using the list "
        "of materials given. "
        "Include the specific names of exercises"
        "along with the recommended frequency of training per week, aligned with the overall objective. "
        "Additionally,"
        "develop a meal plan for each day of the week (exactly 3 meals for each day of the 7 days of the"
        "week from monday to sunday) the meals should be different for the 7 days and can be prepared only using the list of ingredients "
        "given."
        "And ensure that the meals align with the fitness objective. Lastly, provide instructions on how to prepare each meal."
        "Give me the whole answer in json format put only the json data dont write json at the begining : {objective : the objective given as input by the user }, {training_sessions_day_by_day : ...}, {how_to_perform_exercises : ...}, "
        "{meals : ...},{how_to_prepare_meals:....}, {ingredients : the ingredients chosen by the user}"
    )
    prompt_end = (
        f"\n\nQuestion: {query}\nAnswer:"
    )

    # append context chunks until we hit the
    # limit of tokens we want to send to the prompt.
    prompt = ""
    for i in range(1, len(context_chunks)):
        if len("\n\n---\n\n".join(context_chunks[:i])) >= PROMPT_LIMIT:
            prompt = (
                    prompt_start +
                    "\n\n---\n\n".join(context_chunks[:i - 1]) +
                    prompt_end
            )
            break
        elif i == len(context_chunks) - 1:
            prompt = (
                    prompt_start +
                    "\n\n---\n\n".join(context_chunks) +
                    prompt_end
            )
    return prompt
