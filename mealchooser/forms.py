from flask_wtf import FlaskForm       
from wtforms import StringField, PasswordField, SubmitField, BooleanField    # Imports the classes and functions to work with strings and passwords
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',    #This is also the label for the HTML
        validators=[DataRequired(), Length(min=2,max=20)])    #This is to validate the input

    email = StringField('Email', validators=[DataRequired(), Email()]) # Had to run pip install email_validator
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    confirm_password = PasswordField('Confirm Password', 
        validators=[DataRequired(), Length(min=5), EqualTo('password')])
    submit = SubmitField('Sing Up')

class LoginForm(FlaskForm):
    username = StringField('Username',    #This is also the label for the HTML
        validators=[DataRequired(), Length(min=2,max=20)])    #This is to validate the input
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    remember = BooleanField('Remember Me')   # Allows login with a secure cookie
    submit = SubmitField('Login')
