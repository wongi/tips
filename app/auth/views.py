from flask import render_template,redirect,url_for,flash,session
from flask_login import login_user,logout_user,login_required

from .. import db
from ..models import User 
from . import auth
from .forms import LoginForm

@auth.route('/login/',methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(name=form.name.data,password=form.password.data).first()
		if user:
			login_user(user,form.remember_me.data)
			session['username']=form.name.data 
			return redirect(url_for('main.index'))
		else:
			flash('错误的用户名或密码！')
	return render_template('auth/login.html',form=form)

@auth.route('/logout/')
@login_required
def logout():
	logout_user()
	flash('登出')
	return redirect(url_for('main.index'))