from flask import Flask
from flask_jwt_extended import JWTManager
from .database import Base, engine
from .models import User, FuelStation, FuelHistory
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dva_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to a secure key

    # Initialize database
    Base.metadata.create_all(bind=engine)

    # Initialize JWT
    jwt = JWTManager(app)

    # Register the Blueprint
    app.register_blueprint(bp)

    return app