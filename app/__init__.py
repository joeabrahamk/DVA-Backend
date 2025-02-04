from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os
from dotenv import load_dotenv
from flask_migrate import Migrate

# Load environment variables
load_dotenv()

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    # Database Configuration
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL is not set in the environment variables")

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url  # Ensure it's properly set
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize Extensions
    db.init_app(app)
    bcrypt.init_app(app)
    CORS(app)

    # Import and register Blueprints
    from app.routes import bp  
    app.register_blueprint(bp)
    Migrate(app,db)

    return app
