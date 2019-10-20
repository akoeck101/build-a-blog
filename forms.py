from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from main import db,User
class Registration(FlaskForm):
    #'Username', 'Password', etc is the label
    username = StringField('Username',validators=[DataRequired(), Length(min=4,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    #argument for EqualTo is the field we want this to be equal to need to make sure password and confirm password are equal, so need to use equal validator
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user: #if user exists already
            raise ValidationError('Sorry, that username is already taken.')
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if email: #if user exists already
            raise ValidationError('Email already exists.')    



class Login(FlaskForm):
    #'Username', 'Password', etc is the label
    username = StringField('Username',
    validators=[DataRequired(), Length(min=4,max=20)])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')

