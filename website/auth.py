# Define file "Blueprint" that has roots.
from flask import Blueprint, render_template, request, flash, redirect, url_for
# Import User
from .models import User
# Import flash login which secures password. Not displaying it on plain text.
# Password type equals the hash that is stored
from werkzeug.security import generate_password_hash, check_password_hash
# Import db
from . import db
# Helps login user | current_user represents current login user 
# Needs UserMixin so the current user will have access to all the info about the user.
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# Able to accept both requests
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Once signed in want the email and password
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Next want to check if the user and email sent to the form is valid
        # by looking for specific entry in database like column or field.
        #----------------------------------------------------------------
        # Here, want to filter the users that have this email right here
        user = User.query.filter_by(email=email).first()
        # if the user sucessfully logs in
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                # If server is running remains true if user clears browsing history.
                # Flask will remember user
                login_user(user, remember=True)
                # Once successfully logged in, direct user to homepage
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        # If there's no user with that email.
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
# Makes sure function cannot be executed unless user is logged in.
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        # Makes sure to not signup users with existing email.
        if user:
            flash('Email already exists.', category='error')
        # Want to make sure user is valid once POST request goes through
        elif len(email) < 4:
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
            login_user(user, remember=True)
            flash('Account created!', category='success')
            # Return redirect to the URL towards the homepage
            return redirect(url_for('views.home'))

    # If theres access with current user it will display in navbar.
    return render_template("sign_up.html", user=current_user)