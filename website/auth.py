# Define file "Blueprint" that has roots.
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

#Login & logout
@auth.route('/login')
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<h1>Sign Out</h1>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")