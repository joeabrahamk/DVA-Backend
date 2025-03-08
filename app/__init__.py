from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os
from dotenv import load_dotenv
from flask_migrate import Migrate

# Load environment variables
load_dotenv()

# Initialize extensions without importing models
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Database Configuration
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL is not set in the environment variables")

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize Extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)  # ✅ Correctly initialize Flask-Migrate
    CORS(app, supports_credentials=True)

    # Import Blueprints inside create_app (avoids circular import)
    from app.routes import bp  # ✅ Corrected import path
    app.register_blueprint(bp)

    return app
