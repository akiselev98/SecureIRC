from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from secureirc.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Invalid username.')

class RoomCreationForm(FlaskForm):
    roomname = StringField('Room Name')
    pub_listed = BooleanField('List Publicly')
    submit = SubmitField('Create Room')
    
    def validate_roomname(self, roomname):
        room = Room.query.filter_by(roomname=roomname.data).first()
        if room is not None:
            raise ValidationError('Invalid roomname.')
