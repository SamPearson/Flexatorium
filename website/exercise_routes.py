from flask import Blueprint, render_template
from flask_login import current_user, login_required

from .forms import EditExerciseForm

exercises = Blueprint('exercises', __name__)

from .dummy_data import *

@exercises.route('/browse', methods=['GET', 'POST'])
def browse():
    return render_template("browse_exercises.html", user=current_user, exercise_data=sample_exercises)


@exercises.route('/favorites', methods=['GET', 'POST'])
@login_required
def favorites():
    return "<h1>prankd! Your ugly FACE is my favorite!</h1>"


@exercises.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditExerciseForm()
    # send the exercise ID with the request when editing
    exercise_id = 1
    return render_template("edit_exercise.html", user=current_user, form=form, exercise_id=exercise_id)


@exercises.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = EditExerciseForm()
    return render_template("edit_exercise.html", user=current_user, form=form, exercise_id=None)


