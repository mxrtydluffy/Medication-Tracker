# Folder discription: Makes website folder a python package.

# Import the flask object
from flask import Flask
# Import SQL Alchemy
from flask_sqlalchemy import SQLAlchemy
# Path module to determine wether the path to database exists.
from os import path
# Flask login module
from flask_login import LoginManager
# Environmental Variables
from dotenv import load_dotenv
import os
load_dotenv()


# Initilize Database with db object.
db = SQLAlchemy()
DB_NAME = "medication.db"

def create_app():
    app = Flask(__name__)
    # .config will secure the session data for the website
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    # The SQLALCHEMY DATABASE is located at this location.
    # Stores in this website folder where __init__.py is in.
    app.config['DATABASE_URL'] = os.getenv("DATABASE_URL")

    # Takes database defined telling this is the app going to use with this database.
    db.init_app(app)

    # Register with flask application
    # Anything the import file will be referred from the prefix.
    # Can change prefix to desired wording.
    from .views import views
    from .auth import auth

    ####################
    #   MOVED TO APP   #
    ####################

    # Need to make sure the model.py file loads and runs before the
    # database is initilized.
    from .models import User, Medications

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    # Where to redirect if user is not logged in 
    login_manager.login_view = 'auth.login'
    # Tell login manager what app is being used.
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        """
        Tells flask how to load the user. Here it looks for the primary key (int(id))
        """
        return User.query.get(int(id))

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