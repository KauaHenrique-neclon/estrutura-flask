from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, EmailField, IntegerField, PasswordField, FloatField
from wtforms.validators import DataRequired, Email



"""
   Exemplo de form de login
   render_kw passa um class para o html ou qlq atributo que um input pode receber
"""
class formLogin(FlaskForm):
    email = EmailField('email', validators=[Email()], render_kw={"placeholder": "Seu email"})
    password = PasswordField('password', validators=[DataRequired()],render_kw={"placeholder": "Sua senha"})
    submit = SubmitField('Entrar')