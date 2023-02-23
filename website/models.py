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
    meds = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # Stores in DateTime Field
    # Additional featue
    notes = db.Column(db.String(1000))

class User(db.Model, UserMixin):
    """
    Storing users
    - db.Integer = type of column
    - db.String = Characterse
    """
    id = db.Column(db.Integer, primary_key=True)
    # No user can have the same email as another user. Email exists.
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))