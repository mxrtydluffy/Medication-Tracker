# Define file "Blueprint" that has roots.
from flask import Blueprint, render_template, request, flash

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
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Want to make sure user is valid once POST request goes through
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('Email must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Email must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')

    return render_template("sign_up.html")