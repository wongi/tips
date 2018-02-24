from flask import render_template,redirect,url_for,flash,session
from flask_login import login_user,logout_user,login_required,current_user
from sqlalchemy import func,distinct

from .. import db
from ..models import User,List
from . import auth
from .forms import LoginForm,ListForm,EditForm

@auth.route('/login/',methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(name=form.name.data,password=form.password.data).first()
		if user:
			login_user(user,form.remember_me.data)
			session['username']=form.name.data 
			return redirect(url_for('.list'))
		else:
			flash('错误的用户名或密码！')
	return render_template('auth/login.html',form=form)

@auth.route('/logout/')
@login_required
def logout():
	logout_user()
	flash('登出')
	return redirect(url_for('main.index'))

@auth.route('/list/')
@login_required
def list():
	lists=current_user.lists
	id=db.session.query(func.count(distinct(List.content)))
	print(id)
	return render_template('auth/list.html',lists=lists)

@auth.route('/add/',methods=['GET','POST'])
@login_required
def add_list():
	form=ListForm()
	if form.validate_on_submit():
		list=List(content=form.content.data,status_id=1,user_id=current_user.id)		
		db.session.add(list)
		flash('添加成功')
		return redirect(url_for('auth.list'))
	return render_template('auth/add_list.html',form=form)

@auth.route('/edit/<int:list_id>',methods=['GET','POST'])
@login_required
def edit_list(list_id):
	form=EditForm()
	list=List.query.get(list_id)
	if form.validate_on_submit():
		list.content=form.content.data
		db.session.add(list)
		return redirect(url_for('auth.list'))
	form.content.data=list.content
	return render_template('auth/edit_list.html',form=form)

@auth.route('/delete/<int:list_id>')
@login_required
def delete_list(list_id):
	list=List.query.get(list_id)
	db.session.delete(list)
	flash('删除成功')
	return redirect(url_for('auth.list'))

@auth.route('/complete/<int:list_id>',methods=['GET','POST'])
@login_required
def complete(list_id):
	list=List.query.get(list_id)
	list.status_id=2
	db.session.commit()
	return redirect(url_for('auth.list'))

