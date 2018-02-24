from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField,PasswordField,BooleanField,TextAreaField
from wtforms.validators import Required

class LoginForm(FlaskForm):
	name=StringField('用户名',validators=[Required()])
	password=PasswordField('密码',validators=[Required()])
	remember_me=BooleanField('记住我？')
	submit=SubmitField('登录')

class ListForm(FlaskForm):
	content=TextAreaField('内容',validators=[Required()],render_kw={"placeholder":"最多输入140字..."})
	submit=SubmitField('提交')

class EditForm(FlaskForm):
	content=TextAreaField('内容',validators=[Required()])
	submit=SubmitField('修改')