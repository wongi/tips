from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import Required

class LoginForm(FlaskForm):
	name=StringField('What is  your name?',validators=[Required()])
	password=PasswordField('Password',validators=[Required()])
	remember_me=BooleanField('Keep me logged in')
	submit=SubmitField('Log In')