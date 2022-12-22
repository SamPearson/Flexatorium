from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .home_routes import home_routes
    app.register_blueprint(home_routes, url_prefix='/')

    from .exercise_routes import exercises
    app.register_blueprint(exercises, url_prefix='/exercises')

    from .workout_routes import workouts
    app.register_blueprint(workouts, url_prefix='/workouts')

    from .training_track_routes import training_tracks
    app.register_blueprint(training_tracks, url_prefix='/training_tracks')

    from .user_routes import user_routes
    app.register_blueprint(user_routes, url_prefix='/')

    from .journal_routes import journal_routes
    app.register_blueprint(journal_routes, url_prefix='/journal/')

    from . import models

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return models.RegisteredUser.query.get(int(user_id))

    return app
