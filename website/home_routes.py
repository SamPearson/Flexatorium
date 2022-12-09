from flask import Blueprint, render_template
from flask_login import current_user

home_routes = Blueprint('public_pages', __name__)


@home_routes.route('/', methods=['Get'])
def home():
    return render_template("home.html", user=current_user)


@home_routes.route('/about', methods=['Get'])
def about():
    return render_template("about.html", user=current_user)


@home_routes.route('/timer', methods=['Get'])
def timer():
    return "heyo!"

