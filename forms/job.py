from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash

class JobRegisterForm(FlaskForm):
    job = StringField('Название работки', validators=[DataRequired()])
    work_size = IntegerField('Размер работки', validators=[DataRequired()])
    collaborators = StringField('Сотрудники работки', validators=[DataRequired()])
    submit = SubmitField('Подтвердить создание работки и стать тимлидом работки')