from app import db

class User(db.Model):
	__tablename__='users'
	id=db.Column(db.Integer(),primary_key=True)
	name=db.Column(db.String(64),unique=True,index=True)
	password=db.Column(db.String(128))

	def __repr__(self,name):
		return '<User %r>' % self.name