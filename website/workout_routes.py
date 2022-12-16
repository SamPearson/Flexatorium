from flask import Blueprint, render_template
from flask_login import current_user, login_required

workouts = Blueprint('workouts', __name__)

from .dummy_data import *

@workouts.route('/browse', methods=['GET', 'POST'])
def browse():
    return render_template("browse_workouts.html", user=current_user, workout_data=sample_workouts)


@workouts.route('/favorites', methods=['GET', 'POST'])
@login_required
def favorites():
    return "<h1>prankd! Your ugly FACE is my favorite!</h1>"


@workouts.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    return render_template("edit_workout.html", user=current_user)