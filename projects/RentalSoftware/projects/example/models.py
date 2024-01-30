from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your data models here, for example:
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.String(17), unique=True, nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    # Add other fields as necessary

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Add other fields as necessary

# Define other models such as RentalAgreement, Invoice, etc.