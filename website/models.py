
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy_json import MutableJson

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # The foreign key below refers to User class despite being in lower case
    user_id = db.Column(db.Integer, db.ForeignKey('registered_user.id'))


class RegisteredUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # Announcing a relationship with the Note class and storing linked Notes
    # The class name is capitalized here, Its reference to this class is in lower case.
    notes = db.relationship('Note')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


exercise_config_option = db.Table('exercise_config_option_table',
                                  db.Column('exercise_id', db.Integer,
                                            db.ForeignKey('exercise.id')),
                                  db.Column('config_option_id', db.Integer,
                                            db.ForeignKey('config_option.id')),
                                  )


class ConfigOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.String(150), unique=True, nullable=False)
    unit_type = db.Column(db.String(150), unique=True, nullable=False)


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('registered_user.id'))
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(250), default='')

    config_options = db.relationship('ConfigOption', secondary=exercise_config_option, backref='exercises')
    config = db.Column(MutableJson)
    muscle_group = db.Column(db.String(150), default='')  # basically tags
    training_focus = db.Column(db.String(150), default='')  # cardio/endurance/etc, also basically tags
    tags = db.Column(db.String(150), default='')  # basically tags


class ExerciseGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('registered_user.id'))
    phases = db.Column(db.String(150), unique=True)  # Sets of Exercises go here
    tags = db.Column(db.String(150), unique=True)
    scoring_method = db.Column(db.String(150), unique=True)
    notes = db.Column(db.String(150), unique=True)


class WorkoutLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('registered_user.id'))
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))


class WorkoutSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class TrainingTrack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
