from flask import Flask,render_template,redirect,url_for,session,flash
from flask_script import Manager,Shell 
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import Required

app=Flask(__name__)
bootstrap=Bootstrap(app)
manager=Manager(app)
db=SQLAlchemy(app)
manager=Manager(app)

def make_shell_context():
	return dict(app=app,db=db,User=User)

manager.add_command(Shell(make_context=make_shell_context))

app.config['DEBUG']=True
app.config['SECRET_KEY']='secret key'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:wj2011go@localhost:3306/tips?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


class LoginForm(FlaskForm):
	name=StringField('What is  your name?')
	password=PasswordField('Password')
	submit=SubmitField('Submit')

class User(db.Model):
	__tablename__='users'
	id=db.Column(db.Integer(),primary_key=True)
	name=db.Column(db.String(64),unique=True,index=True)
	password=db.Column(db.String(128))

	def __repr__(self,name):
		return '<User %r>' % self.name

@app.route('/')
def index():
	return render_template('index.html',name=session.get('username'))

@app.route('/login/',methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(name=form.name.data,password=form.password.data).first()
		if user:
			session['username']=form.name.data 
			return redirect(url_for('index'))
		else:
			flash('错误的用户名或密码！')
			return render_template('login.html',form=form)
			
	return render_template('login.html',form=form)

if __name__=='__main__':
	# app.run()
	manager.run()