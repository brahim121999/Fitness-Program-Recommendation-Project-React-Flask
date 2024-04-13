from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)

    if os.environ.get('FLASK_ENV') == 'development':
        # Enable CORS for all routes
        CORS(app)

    from app.api.routes import api_blueprint
    from app.api.views import user_interface  # Import the new route

    app.register_blueprint(api_blueprint)
    app.register_blueprint(user_interface)  # Register the new route

    return app
