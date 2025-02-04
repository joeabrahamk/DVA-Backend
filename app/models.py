from sqlalchemy.orm import relationship
from app import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(50), unique=True, index=True)
    email = db.Column(db.String(100), unique=True, index=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)  # Fixed column syntax
    hashed_password = db.Column(db.String(255))
    avatar_id = db.Column(db.Integer, db.ForeignKey('user_avatars.avatar_id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())  # Corrected timestamp
    home_lat = db.Column(db.Float(precision=6))
    home_long = db.Column(db.Float(precision=6))
    work_lat = db.Column(db.Float(precision=6))
    work_long = db.Column(db.Float(precision=6))

    # Relationships
    avatar = relationship("UserAvatar", back_populates="users")

class UserAvatar(db.Model):
    __tablename__ = 'user_avatars'
    avatar_id = db.Column(db.Integer, primary_key=True, index=True)
    avatar_url = db.Column(db.String(255), unique=True)

    # Relationship
    users = relationship("User", back_populates="avatar")

# Other models remain the same but ensure all timestamps use db.func.current_timestamp()
