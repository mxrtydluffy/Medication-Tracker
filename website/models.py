# Define the schema how to store info to database.

# Import from the current (this) package, import db.
# Equivalent to say import from website
from . import db
# Custom class inherit that will give user object speciifc qualities for flask login
from flask_login import UserMixin
# Don't need to specify the Date Field manually.
# func gets current date & time
from sqlalchemy.sql import func

class Medications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # Stores in DateTime Field
    # Additional featue
    # notes = db.Column(db.String(1000))

    # Set relationship via foreign key inorder to know user who created medication
        # 1.) Get id number which is integer
        # 2.) Store foreign key on child object that references the parent object.
        # 3.) Every med it can be determine which user created it by looking at user_id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # One-to-many b/c one user has many meds

    # Add class for Doctors, Insurance companies, & reminders later

class User(db.Model, UserMixin):
    """
    Storing users
    - db.Integer = type of column
    - db.String = Characters
    """
    id = db.Column(db.Integer, primary_key=True)
    # No user can have the same email as another user. Email exists.
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # Want user to find all of medications
    # Tells flask & SQLALCHEMY ever meds made, add to this user notes relationship
    # that med ID.
    meds = db.relationship('Medications') # Referencing the class