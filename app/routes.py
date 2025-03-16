from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app import db, bcrypt  # ✅ Ensure correct import
from app.models import User, FuelHistory  # ✅ Ensure models are correctly imported
import logging

bp = Blueprint('main', __name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@bp.route('/signup', methods=['POST'])
@cross_origin(supports_credentials=True)
def signup():
    try:
        data = request.json

        if not data or 'username' not in data or 'password' not in data:
            return jsonify({'message': 'Invalid data'}), 400  # ✅ Error handling

        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        new_user = User(
            username=data['username'],
            name=data.get('name', ''), 
            email=data.get('email', ''),
            age=data.get('age', 0),  
            hashed_password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully', "user_id": new_user.user_id}), 201
    except Exception as e:
        logging.error(f"Error in signup: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@bp.route('/user/<int:user_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_user(user_id):
    try:
        user = User.query.get(user_id)

        if not user:
            return jsonify({'message': 'User not found'}), 404

        user_data = {
            'user_id': user.user_id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'age': user.age
        }
        return jsonify(user_data), 200
    except Exception as e:
        logging.error(f"Error in get_user: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@bp.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def login():
    try:
        data = request.json
        logging.info(f"Login attempt received with data: {data}")

        if not data or 'username' not in data or 'password' not in data:
            return jsonify({'message': 'Invalid data'}), 400

        user = User.query.filter_by(username=data['username']).first()
        
        if user is None:
            logging.warning("User not found")
            return jsonify({'message': 'Invalid credentials'}), 401

        logging.info(f"User found: {user.username}")

        if bcrypt.check_password_hash(user.hashed_password, data['password']):
            logging.info("Password match successful")
            return jsonify({'message': 'Login successful', 'user_id': user.user_id}), 200
        else:
            logging.warning("Incorrect password")
            return jsonify({'message': 'Invalid credentials'}), 401

    except Exception as e:
        logging.error(f"Error in login: {str(e)}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500


@bp.route('/fuel_history/<int:user_id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_fuel_history(user_id):
    try:
        history = FuelHistory.query.filter_by(user_id=user_id).all()

        if not history:
            return jsonify({'message': 'No fuel history found'}), 404

        history_data = [entry.to_dict() for entry in history]
        response = {
            "message": "Fuel history retrieved successfully",
            'fuel_history': history_data
        }
        return jsonify(response), 200
    except Exception as e:
        logging.error(f"Error in get_fuel_history: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@bp.route('/add_fuel_history', methods=['POST'])
@cross_origin(supports_credentials=True)
def add_fuel_history():
    try:
        data = request.json

        if not data or 'user_id' not in data or 'fuel_type' not in data:
            return jsonify({'message': 'Invalid data'}), 400  # ✅ Error handling

        new_entry = FuelHistory(
            user_id=data['user_id'],
            fuel_type=data['fuel_type'],
            quantity=data['quantity'],
            price=data['price'],
            currency=data['currency'],
            date_time=data['date_time']
        )

        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'message': 'Fuel history added successfully', 'entry_id': new_entry.id}), 201
    except Exception as e:
        logging.error(f"Error in add_fuel_history: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@bp.route('/', methods=['GET'])
def home():
    try:
        return jsonify({'message': 'Welcome to the Fuel Tracker API'}), 200
    except Exception as e:
        logging.error(f"Error in home: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500