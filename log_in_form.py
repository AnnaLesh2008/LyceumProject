from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    if_of_astro = IntegerField('Id космонавта', validators=[DataRequired()])
    password_of_astro = PasswordField('Пароль космонавта', validators=[DataRequired()])
    id_of_capitan = IntegerField('Id капитана', validators=[DataRequired()])
    password_of_capitan = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')

