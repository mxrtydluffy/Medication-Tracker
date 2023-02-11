# Store all the URL end points for functioning the front end aspect of the website.
# Anything not related to authentication the user can navigate to goes here.

# Define file "Blueprint" that has roots.
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
