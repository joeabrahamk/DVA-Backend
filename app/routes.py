from flask import Blueprint, request, jsonify
from app import db
# from app.models import User
import psycopg2
import os
from dotenv import load_dotenv
from .models import User

# Load environment variables from .env file
load_dotenv()

bp = Blueprint('main',(__name__))