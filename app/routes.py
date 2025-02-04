from flask import Blueprint, request, jsonify
from .models import User
from app import db
from app import bcrypt
from flask_cors import cross_origin 

bp = Blueprint('main', __name__)

@bp.route('/signup', methods=['POST'])
@cross_origin()
def signup():
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    new_user = User(
        username=data['username'],
        name=data['name'],
        age=data['age'],
        hashed_password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if user and bcrypt.check_password_hash(user.hashed_password, data['password']):
        return jsonify({'message': 'Login successful', 'user_id': user.user_id}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
