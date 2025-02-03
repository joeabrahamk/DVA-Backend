# filepath: /C:/Users/joeab/OneDrive/Desktop/projects/DVA-Backend/app/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
# Replace with your PostgreSQL connection string
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
db = SQLAlchemy()
# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()