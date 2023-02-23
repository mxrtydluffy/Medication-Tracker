# Makes website folder a python package.

from flask import Flask

def create_app():
    app = Flask(__name__)
    # .config will secure the session data for the website
    app.config['SECRET_KEY'] = 'medz_all_the_way'

    # db = 

    # Register with flask application
    # Anything the import file will be referred from the prefix.
    # Can change prefix to desired wording.
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app