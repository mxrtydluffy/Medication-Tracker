# Define file "Blueprint" that has roots.
from flask import Blueprint, render_template, request, flash, redirect, url_for
# Import User
from .models import User
# Import flash login which secures password. Not displaying it on plain text.
# Password type equals the hash that is stored
from werkzeug.security import generate_password_hash, check_password_hash
# Import db
from . import db

auth = Blueprint('auth', __name__)

# Able to accept both requests
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Have information that is sent to access this route
    data = request.form
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<h1>Sign Out</h1>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Want to make sure user is valid once POST request goes through
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('Email must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Email must be at least 7 characters.', category='error')
        else:
            # Defined fields that was in models.py
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256')) # Hashing algorithmn
            # Add user to database
            db.session.add(new_user)
            # Comit to the database
            db.session.commit()
            flash('Account created!', category='success')
            # Return redirect to the URL towards the homepage
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")