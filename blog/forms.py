from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Required, Length, Email, EqualTo, ValidationError
from .models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(min=2, max=20)])
    email = StringField('Email', validators=[Required(),Email()])
    password = PasswordField('Password', validators=[Required()])
    confirm_password = PasswordField('Confirm Password', validators=[Required(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The username already exists!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The email already exists!')
class LoginForm(FlaskForm):  
    email = StringField('Email', validators=[Required(),Email()])
    password = PasswordField('Password', validators=[Required()]) 
    remember = BooleanField('Remember Me')  
    submit = SubmitField('Sign Up')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(min=2, max=20)])
    email = StringField('Email', validators=[Required(),Email()])
    password = PasswordField('Password', validators=[Required()])
    confirm_password = PasswordField('Confirm Password', validators=[Required(),EqualTo('password')])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('The username already exists!')

    def validate_email(self, email):
        if email.data != current_user.username:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('The email already exists!')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Content', validators=[Required()])
    submit = SubmitField('Post')