# Folder discription: Makes website folder a python package.

# Import the flask object
from flask import Flask
# Import SQL Alchemy
from flask_sqlalchemy import SQLAlchemy
# Path module to determine wether the path to database exists.
from os import path

# Initilize Database with db object.
db = SQLAlchemy()
DB_NAME = 'medication.db'

def create_app():
    app = Flask(__name__)
    # .config will secure the session data for the website
    app.config['SECRET_KEY'] = 'medz_all_the_way'
    # The SQLALCHEMY DATABASE is located at this location.
    # Stores in this website folder where __init__.py is in.
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # Takes database defined telling this is the app going to use with this database.
    db.init_app(app)

    # Register with flask application
    # Anything the import file will be referred from the prefix.
    # Can change prefix to desired wording.
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Need to make sure the model.py file loads and runs before the
    # database is initilized.
    from .models import User, Medications

    create_database(app)

    return app

def create_database(app):
    """
    * Use PATH module & check databse exists 
    Checks if dartabase exists, if not it will create it (db.create_all).
    Don't want to override since it has data in it already.
    """
    if not path.exists('medication/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')