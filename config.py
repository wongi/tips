class Config:
	DEBUG=True

class DevConfig(Config):
	SECRET_KEY='secret key'
	SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:wj2011go@localhost:3306/todolist?charset=utf8mb4'
	SQLALCHEMY_TRACK_MODIFICATIONS=False
	SQLALCHEMY_COMMIT_ON_TEARDOWN=True

config={
	'default':DevConfig}
