class Config:
	DEBUG=True

class DevConfig(Config):
	SECRET_KEY='secret key'
	SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:wj2011go@localhost:3306/tips?charset=utf8mb4'
	SQLALCHEMY_TRACK_MODIFICATIONS=False

config={
	'default':DevConfig}
