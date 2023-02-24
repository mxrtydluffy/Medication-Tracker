# Store all the URL end points for functioning the front end aspect of the website.
# Anything not related to authentication the user can navigate to goes here.

# Define file "Blueprint" that has roots.
from flask import Blueprint, render_template

from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
# Cannot get to the homepage unless user is logged in.
@login_required()
def home():
    return render_template("home.html")
