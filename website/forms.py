from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, FormField, FieldList, \
    TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional


class SignupForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                             validators=[DataRequired(), EqualTo('password')])

    submit_button = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('🔥Remember Me🔥')

    submit_button = SubmitField('Log In')


class ExerciseConfigField(Form):
    name = StringField('Option Name')
    value = IntegerField('Value', validators=[Optional()])


class EditExerciseForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    config_types = FieldList(StringField())
    config_unit_names = FieldList(StringField())

    tags = StringField('Tags', validators=[Optional()])

    save_button = SubmitField('Save')
