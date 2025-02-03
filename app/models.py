from sqlalchemy.orm import relationship
from app import db


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(50), unique=True, index=True)
    email = db.Column(db.String(100), unique=True, index=True)
    hashed_password = db.Column(db.String(255))
    avatar_id = db.Column(db.Integer, db.ForeignKey('user_avatars.avatar_id'))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default='CURRENT_TIMESTAMP')

    # Relationships
    fuel_history = relationship("FuelHistory", back_populates="user")
    saved_locations = relationship("SavedLocation", back_populates="user")
    vehicles = relationship("Vehicle", back_populates="user")
    reviews = relationship("Review", back_populates="user")

class UserAvatar(db.Model):
    __tablename__ = 'user_avatars'

    avatar_id = db.Column(db.Integer, primary_key=True, index=True)
    avatar_url = db.Column(db.String(255), unique=True)

    # Relationships
    users = relationship("User", back_populates="avatar")

class FuelStation():
    __tablename__ = 'fuel_stations'

    station_id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(255))
    latitude = db.Column(db.Float(precision=6))
    longitude = db.Column(db.Float(precision=6))
    contact_number = db.Column(db.String(15))
    is_24x7 = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default='CURRENT_TIMESTAMP')

    # Relationships
    fuel_history = relationship("FuelHistory", back_populates="station")
    fuel_prices = relationship("FuelPrice", back_populates="station")
    reviews = relationship("Review", back_populates="station")

class FuelType():
    __tablename__ = 'fuel_types'

    fuel_type_id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(50), unique=True)

    # Relationships
    fuel_history = relationship("FuelHistory", back_populates="fuel_type")
    fuel_prices = relationship("FuelPrice", back_populates="fuel_type")

class FuelHistory():
    __tablename__ = 'fuel_history'

    history_id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    station_id = db.Column(db.Integer, db.ForeignKey('fuel_stations.station_id'))
    fuel_type_id = db.Column(db.Integer, db.ForeignKey('fuel_types.fuel_type_id'))
    quantity = db.Column(db.Float(precision=2))
    price = db.Column(db.Float(precision=2))
    currency = db.Column(db.String(10))
    date_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default='CURRENT_TIMESTAMP')

    # Relationships
    user = relationship("User", back_populates="fuel_history")
    station = relationship("FuelStation", back_populates="fuel_history")
    fuel_type = relationship("FuelType", back_populates="fuel_history")

class FuelPrice():
    __tablename__ = 'fuel_prices'

    price_id = db.Column(db.Integer, primary_key=True, index=True)
    station_id = db.Column(db.Integer, db.ForeignKey('fuel_stations.station_id'))
    fuel_type_id = db.Column(db.Integer, db.ForeignKey('fuel_types.fuel_type_id'))
    price = db.Column(db.Float(precision=2))
    currency = db.Column(db.String(10))
    updated_at = db.Column(db.DateTime, default='CURRENT_TIMESTAMP')

    # Relationships
    station = relationship("FuelStation", back_populates="fuel_prices")
    fuel_type = relationship("FuelType", back_populates="fuel_prices")

class SavedLocation():
    __tablename__ = 'saved_locations'

    location_id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    name = db.Column(db.String(50))
    latitude = db.Column(db.Float(precision=6))
    longitude = db.Column(db.Float(precision=6))
    created_at = db.Column(db.DateTime, default='CURRENT_TIMESTAMP')

    # Relationships
    user = relationship("User", back_populates="saved_locations")

class Vehicle():
    __tablename__ = 'vehicles'

    vehicle_id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    name = db.Column(db.String(50))
    fuel_efficiency = db.Column(db.Float(precision=2))

    # Relationships
    user = relationship("User", back_populates="vehicles")

class Review():
    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    station_id = db.Column(db.Integer, db.ForeignKey('fuel_stations.station_id'))
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default='CURRENT_TIMESTAMP')

    # Relationships
    user = relationship("User", back_populates="reviews")
    station = relationship("FuelStation", back_populates="reviews")