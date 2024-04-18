from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from flask import Blueprint
from flask_cors import CORS

api_blueprint = Blueprint('api', __name__)
CORS(api_blueprint)
app = Flask(__name__)


# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import and register routes Blueprint
from app.views import user_interface
app.register_blueprint(api_blueprint)
app.register_blueprint(user_interface)

# Load app configuration
app.config.from_object(Config)
