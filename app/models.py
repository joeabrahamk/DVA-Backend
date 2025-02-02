from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float, DateTime, Text
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    avatar_id = Column(Integer, ForeignKey('user_avatars.avatar_id'))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    # Relationships
    fuel_history = relationship("FuelHistory", back_populates="user")
    saved_locations = relationship("SavedLocation", back_populates="user")
    vehicles = relationship("Vehicle", back_populates="user")
    reviews = relationship("Review", back_populates="user")

class UserAvatar(Base):
    __tablename__ = 'user_avatars'

    avatar_id = Column(Integer, primary_key=True, index=True)
    avatar_url = Column(String(255), unique=True)

    # Relationships
    users = relationship("User", back_populates="avatar")

class FuelStation(Base):
    __tablename__ = 'fuel_stations'

    station_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    location = Column(String(255))
    latitude = Column(Float(precision=6))
    longitude = Column(Float(precision=6))
    contact_number = Column(String(15))
    is_24x7 = Column(Boolean, default=False)
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    # Relationships
    fuel_history = relationship("FuelHistory", back_populates="station")
    fuel_prices = relationship("FuelPrice", back_populates="station")
    reviews = relationship("Review", back_populates="station")

class FuelType(Base):
    __tablename__ = 'fuel_types'

    fuel_type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)

    # Relationships
    fuel_history = relationship("FuelHistory", back_populates="fuel_type")
    fuel_prices = relationship("FuelPrice", back_populates="fuel_type")

class FuelHistory(Base):
    __tablename__ = 'fuel_history'

    history_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    station_id = Column(Integer, ForeignKey('fuel_stations.station_id'))
    fuel_type_id = Column(Integer, ForeignKey('fuel_types.fuel_type_id'))
    quantity = Column(Float(precision=2))
    price = Column(Float(precision=2))
    currency = Column(String(10))
    date_time = Column(DateTime)
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    # Relationships
    user = relationship("User", back_populates="fuel_history")
    station = relationship("FuelStation", back_populates="fuel_history")
    fuel_type = relationship("FuelType", back_populates="fuel_history")

class FuelPrice(Base):
    __tablename__ = 'fuel_prices'

    price_id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, ForeignKey('fuel_stations.station_id'))
    fuel_type_id = Column(Integer, ForeignKey('fuel_types.fuel_type_id'))
    price = Column(Float(precision=2))
    currency = Column(String(10))
    updated_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    # Relationships
    station = relationship("FuelStation", back_populates="fuel_prices")
    fuel_type = relationship("FuelType", back_populates="fuel_prices")

class SavedLocation(Base):
    __tablename__ = 'saved_locations'

    location_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    name = Column(String(50))
    latitude = Column(Float(precision=6))
    longitude = Column(Float(precision=6))
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    # Relationships
    user = relationship("User", back_populates="saved_locations")

class Vehicle(Base):
    __tablename__ = 'vehicles'

    vehicle_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    name = Column(String(50))
    fuel_efficiency = Column(Float(precision=2))

    # Relationships
    user = relationship("User", back_populates="vehicles")

class Review(Base):
    __tablename__ = 'reviews'

    review_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    station_id = Column(Integer, ForeignKey('fuel_stations.station_id'))
    rating = Column(Integer)
    comment = Column(Text)
    created_at = Column(DateTime, default='CURRENT_TIMESTAMP')

    # Relationships
    user = relationship("User", back_populates="reviews")
    station = relationship("FuelStation", back_populates="reviews")