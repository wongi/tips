from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Required

class LoginForm(FlaskForm):
	name=StringField('What is  your name?')
	password=PasswordField('Password')
	submit=SubmitField('Submit')