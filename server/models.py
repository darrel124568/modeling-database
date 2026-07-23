from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Driver(db.Model):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    truck = db.relationship('Truck', back_populates='driver', uselist=False, cascade='all, delete-orphan')
    trips = db.relationship('Trip', back_populates='driver', cascade='all, delete-orphan')

class Truck(db.Model):
    __tablename__ = 'trucks'
    id = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String, nullable=False, unique=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), unique=True)
    expenses = db.relationship('Expense', back_populates='truck', cascade='all, delete-orphan')
    driver = db.relationship('Driver', back_populates='truck', uselist=False)
    trips = db.relationship('Trip', back_populates='truck', cascade='all, delete-orphan')


class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    expense_date = db.Column(db.String, nullable=False)
    truck_id = db.Column(db.Integer, db.ForeignKey('trucks.id'), nullable=False)
    truck = db.relationship('Truck', back_populates='expenses', uselist=False)

class Trip(db.Model):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    trip_date = db.Column(db.String, nullable=False)
    origin = db.Column(db.String, nullable=False)
    distance = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=False)
    truck_id = db.Column(db.Integer, db.ForeignKey('trucks.id'), nullable=False)
    driver = db.relationship('Driver', back_populates='trips')
    truck = db.relationship('Truck', back_populates='trips')
    revenue = db.relationship('Revenue', back_populates='trip', uselist=False, cascade='all, delete-orphan')

class Revenue(db.Model):
    __tablename__ = 'revenues'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.id'), nullable=False, unique=True)

    trip = db.relationship('Trip', back_populates='revenue')