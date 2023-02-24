# Store all the URL end points for functioning the front end aspect of the website.
# Anything not related to authentication the user can navigate to goes here.

# Define file "Blueprint" that has roots.
from flask import Blueprint, render_template, request, flash, jsonify
# Import flask login module
from flask_login import login_required, current_user
# Select all the classes from models and import medications
from .models import Medications
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
# Cannot get to the homepage unless user is logged in.
@login_required
def home():
    """
    - References current user and checks if authenticated
    - Gets data via POST method.
    - Then gets the note from HTML doc
    """
    if request.method == 'POST':
        med = request.form.get('med')

        if len(med) < 1:
            flash('Medication is too short!', category='error')
        else:
            new_med = Medications(data=med, user_id=current_user.id)
            db.session.add(new_med)
            db.session.commit()
            flash('Medication added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-med', methods=['POST'])
def delete_med():
    """
    1.) Request will come in data parameter in request object 
    that needs to be imported from JSON.
    2.) Access the medId
    3.) Look for the med that has that ID
    4.) Check if it exists then delete it.
    5.) If user sign in owns the med then the med will be deleted
    5.) Return empty response
    """
    med = json.loads(request.data)
    medId = med['medId']
    med = Medications.query.get(medId)
    if med:
        if med.user_id == current_user.id:
            db.session.delete(med)
            db.session.commit()
            # Notifying user if sucessful or not

    return jsonify({})