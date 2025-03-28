from app import db  # Import db from initialized app
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(50), unique=True, index=True)
    email = db.Column(db.String(100), unique=True, index=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)  # Fixed column syntax
    hashed_password = db.Column(db.String(255), nullable=False)
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

class FuelHistory(db.Model):
    __tablename__ = 'fuel_history'  # ✅ Fixed table name reference
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)  # ✅ Fixed table name reference
    fuel_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(20), nullable=False)
    date_time = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'fuel_type': self.fuel_type,
            'quantity': self.quantity,
            'price': self.price,
            'currency': self.currency,
            'date_time': self.date_time
        }
        
        
class Clipboard(db.Model):
    __tablename__ = 'clipboards'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.String(50), nullable=False)  # Corrected from db.string to db.String

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'content': self.content,
            'created_at': self.created_at
        }


class Savedloc(db.Model):
    __tablename__ = 'savedlocs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    location_name = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.Float(precision=6), nullable=False)
    long = db.Column(db.Float(precision=6), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'location_name': self.location_name,
            'lat': self.lat,
            'long': self.long
        }
        
        
        
class Pump(db.Model):
    __tablename__ = 'pumps'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.Float(precision=6), nullable=False)
    long = db.Column(db.Float(precision=6), nullable=False)
    price = db.Column(db.Float, nullable=False)
    fuel_type = db.Column(db.String(50), nullable=False)
    location_name = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'lat': self.lat,
            'long': self.long,
            'price': self.price,
            'fuel_type': self.fuel_type,
            'location_name': self.location_name
        }
        