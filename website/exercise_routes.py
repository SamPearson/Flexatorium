from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import current_user, login_required
from collections import defaultdict
import json

from .forms import EditExerciseForm

from . import db
from .models import Exercise

exercises = Blueprint('exercises', __name__)


@exercises.route('/browse', methods=['GET', 'POST'])
def browse():
    user_exercises = Exercise.query.filter_by(owner_id=current_user.id)
    return render_template("browse_exercises.html", user=current_user, exercise_data=user_exercises)


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

    if form.validate_on_submit():
        exercise = Exercise.query.filter_by(name=form.name.data).first()
        if exercise:
            flash('Email already registered', category='error')
        else:
            owner_id = current_user.id
            name = form.name.data
            description = form.description.data

            config_blob = defaultdict(list)
            for cfg_type, unit in zip(form.config_types, form.config_unit_names):
                config_blob[cfg_type.data].append({
                    'unit': unit.data,
                    'value': None
                })

            config = config_blob
            new_exercise = Exercise(owner_id=owner_id, name=name, description=description, config=config)

            db.session.add(new_exercise)
            db.session.commit()
            flash(f'Exercise "{form.name.data}" created!', 'success')

            return redirect( url_for('exercises.browse'))

    return render_template("edit_exercise.html", user=current_user, form=form, exercise_id=None)


@exercises.route('/delete', methods=['Post'])
@login_required
def delete_note():
    exercise = json.loads(request.data)
    exercise_id = exercise['exerciseId']
    exercise = Exercise.query.get(exercise_id)
    if exercise:
        if exercise.owner_id == current_user.id:
            db.session.delete(exercise)
            db.session.commit()
    return jsonify({})
