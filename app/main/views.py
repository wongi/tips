from flask import render_template,redirect,url_for,session,flash
from .. import db
from ..models import User
from . import main 
from .forms import LoginForm


@main.route('/')
def index():
	return render_template('index.html',name=session.get('username'))

@main.route('/login/',methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(name=form.name.data,password=form.password.data).first()
		if user:
			session['username']=form.name.data 
			return redirect(url_for('.index'))
		else:
			flash('错误的用户名或密码！')
			return render_template('login.html',form=form)
			
	return render_template('login.html',form=form)