from flask import Blueprint, render_template
from flask_login import current_user, login_required

training_tracks = Blueprint('training_tracks', __name__)

mockup_training_tracks = [
    {
        '': ''
    }
]


@training_tracks.route('/browse', methods=['GET', 'POST'])
def browse():
    return render_template("browse_training_tracks.html", user=current_user, workouts=mockup_training_tracks)


@training_tracks.route('/favorites', methods=['GET', 'POST'])
@login_required
def favorites():
    return "<h1>prankd! Your ugly FACE is my favorite!</h1>"


@training_tracks.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    return render_template("edit_training_track.html", user=current_user)