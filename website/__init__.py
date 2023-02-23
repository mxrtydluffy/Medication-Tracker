# Folder discription: Makes website folder a python package.

# Import the flask object
from flask import Flask
# Import SQL Alchemy
from flask_sqlalchemy import SQLAlchemy

# Initilize Database with db object.
db = SQLAlchemy
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

    return app