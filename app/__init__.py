from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.api import api_blueprint
from config import Config
from flask import Blueprint
from flask_cors import CORS


app = Flask(__name__)


# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import and register routes Blueprint
from app.recommendation import user_interface
app.register_blueprint(api_blueprint)
app.register_blueprint(user_interface)

# Load app configuration
app.config.from_object(Config)
from app import routes, models