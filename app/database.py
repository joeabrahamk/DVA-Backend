from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your PostgreSQL connection string
SQLALCHEMY_DATABASE_URL = "postgresql://avnadmin:AVNS_vbyTxJckLo1HMnPP2M7@pg-3ab49eb0-d-v-a.f.aivencloud.com:17972/defaultdb?sslmode=require"

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()