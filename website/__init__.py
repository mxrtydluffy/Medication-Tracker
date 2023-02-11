# Makes website folder a python package.

from flask import Flask

def create_app():
    app = Flask(__name__)
    # .config will secure the session data for the website
    app.config['SECRET_KEY'] = 'medz_all_the_way'

    return app