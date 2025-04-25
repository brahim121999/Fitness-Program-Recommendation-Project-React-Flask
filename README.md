# 🏋️‍♂️ **Training & Meal Recommendation System** 🍽️

## Overview
This project is a **training and meal recommendation system** designed for people who go to the gym or those looking to improve their overall health. Built with **Flask** (Python) for the backend and **ReactJS** for the frontend, this web application provides users with personalized workout routines and meal plans based on their goals and preferences. Additionally, the system integrates **RAG (Retrieve and Generate)** techniques using the **ChatGPT API** and **Pincone**, a vector database, to enhance the recommendation system.

## Features
- **💪 Personalized Workout Routines**: Based on the user's fitness level, goals, and available equipment, the system generates a personalized workout plan.
- **🍏 Meal Recommendations**: The application provides healthy meal suggestions based on the user's dietary preferences and fitness goals.
- **🧑‍🤝‍🧑 User Profiles**: Users can create profiles, input personal data (age, weight, fitness goals), and track progress.
- **💬 ChatGPT Integration**: **RAG (Retrieve and Generate)** techniques are used with the **ChatGPT API** to dynamically generate personalized workout tips, nutrition advice, and motivational content based on user input.
- **🔍 Pincone Integration**: **Pincone** is used to store and manage relevant user data (such as fitness preferences, previous interactions, and other context) as vector embeddings. The **ChatGPT API** retrieves this stored data to ensure that each response is highly personalized and contextually relevant to the user's needs.

## Tech Stack
- **Frontend**: ReactJS
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Vector Database**: Pincone (used to store and manage user data in vector format for retrieval in RAG)
- **APIs**: Custom API for handling workout and meal recommendations
- **RAG Techniques**: The **ChatGPT API** is used for real-time, AI-driven recommendations. In the **RAG (Retrieve and Generate)** technique, **Pincone** acts as a vector database to store relevant user data (such as fitness preferences, goals,historical interactions and some important informations about sport and meals in general) in vector embeddings. When a user interacts with the system, the ChatGPT API retrieves contextually relevant data from Pincone to generate personalized responses. This process ensures that the system provides highly tailored, context-aware recommendations for workouts, nutrition, and overall wellness.
