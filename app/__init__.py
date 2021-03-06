from flask import Flask,render_template,redirect,url_for,session,flash
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy 
from config import config
from flask_login import LoginManager

bootstrap=Bootstrap()
db=SQLAlchemy()
login_manager=LoginManager()
login_manager.login='login'

def create_app(config_name):
	app=Flask(__name__)
	app.config.from_object(config[config_name])
	bootstrap.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)
	
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint,url_prefix='/auth')
	
	return app
