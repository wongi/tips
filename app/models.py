from app import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(64),unique=True,index=True,nullable=False)
	password=db.Column(db.String(128),nullable=False)
	lists=db.relationship('List',backref='user',lazy=True)

	def __repr__(self,name):
		return '<User %r>' % self.name

class List(db.Model):
	__tablename__='lists'
	id=db.Column(db.Integer,primary_key=True)
	content=db.Column(db.String(128),index=True,nullable=False)
	create_time=db.Column(db.DateTime(),default=datetime.utcnow)
	status_id=db.Column(db.Integer,db.ForeignKey('status.id'))
	user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

	def __repr__(self,content):
		return '<List %r>' % self.content

class Status(db.Model):
	__tablename__='status'
	id=db.Column(db.Integer,primary_key=True)
	status_name=db.Column(db.String(10),unique=True,nullable=False)
	lists=db.relationship('List',backref=db.backref('status',lazy=True))

	def __repr__(self,status_name):
		return '<Status %r>' % self.status_name


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))