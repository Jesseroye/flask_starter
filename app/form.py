from flask.ext.wtf import Form
from wtforms.fields import TextField,SubmitField,RadioField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import Required,InputRequired ,NumberRange, ValidationError
from flask_wtf.html5 import IntegerField
from sqlalchemy.sql import exists
from app import db
from app.models import User


def validate_username(form,field):
    if db.session.query(exists().where(User.username == field.data)).scalar():
        raise ValidationError('Username already exists.')

class Pform(Form):
    first_name = TextField("FirstName",validators=[Required("Please enter your first name.")])
    last_name = TextField("LastName",validators=[Required("Please enter your last name.")])
    username = TextField("Username",validators=[Required("Please enter your  username."),validate_username])
    sex = RadioField("Sex",choices=[('male','Male'),('female','Female')])
    age = IntegerField('Age', validators=[Required(),NumberRange(min=0, max=100)])
    image = FileField('Profile image', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField("Submit")