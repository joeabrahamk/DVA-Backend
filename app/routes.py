from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .database import SessionLocal
from .models import User, FuelStation, FuelHistory
from . import bp

# Example: User login
@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()

    # Validate user credentials (e.g., check password hash)
    if user and user.hashed_password == password:  # Replace with proper password hashing
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Example: Protected route
@bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200