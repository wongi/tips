from app import db
from flask_login import UserMixin
from . import login_manager

class User(UserMixin,db.Model):
	__tablename__='users'
	id=db.Column(db.Integer(),primary_key=True)
	name=db.Column(db.String(64),unique=True,index=True)
	password=db.Column(db.String(128))

	def __repr__(self,name):
		return '<User %r>' % self.name


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))