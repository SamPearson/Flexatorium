from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

from .forms import SignupForm, LoginForm


user_routes = Blueprint('auth', __name__)


@user_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('user_pages.journal'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('No user with that email.', category='error')
    form = LoginForm()
    return render_template("login.html", user=current_user, form=form)


@user_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@user_routes.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    form = SignupForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Email already registered', category='error')

        else:
            email = form.email.data
            username = form.username.data
            password = form.password.data

            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!', 'success')
            login_user(new_user, remember=True)
            return redirect(url_for('public_pages.home'))  # views file, home function.

    return render_template("signup.html", user=current_user, form=form)

