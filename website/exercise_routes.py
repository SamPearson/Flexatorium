from flask import Blueprint, render_template
from flask_login import current_user, login_required

from .forms import EditExerciseForm

exercises = Blueprint('exercises', __name__)

sample_exercise_templates = [
    {
        'name': 'Rowing Machine',
        'description': """Simulated boat rowing on a machine. """,
        'intensity_unit': 'spm',
        'duration_unit': 'meters',
        'notes': 'Rowing machines vary'
    },
    {
        'name': 'Curl + Arnold Press',
        'description': 'A curl followed by the arnold press',
        'intensity_unit': 'lbs',
        'duration_unit': 'reps',
        'notes': ''
    },
    {
        'name': 'Deadlift',
        'description': 'Simulated Boat Rowing on a machine',
        'intensity_unit': 'spm',
        'duration_unit': 'meters',
        'notes': 'Rowing machines vary'
    }
]


@exercises.route('/browse', methods=['GET', 'POST'])
def browse():
    return render_template("browse_exercises.html", user=current_user, ex_templates=sample_exercise_templates)


@exercises.route('/favorites', methods=['GET', 'POST'])
@login_required
def favorites():
    return "<h1>prankd! Your ugly FACE is my favorite!</h1>"


@exercises.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditExerciseForm()
    return render_template("edit_exercise.html", user=current_user, action="Edit", form=form)


