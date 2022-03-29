from flask_wtf import FlaskForm
from wtforms import *

class RegisterForm(FlaskForm):
    nombre = StringField("Ingrese un nombre")
    aceptar = SubmitField("Agregar")

class DeleteForm(FlaskForm):
    id = IntegerField("Ingrese una ID para borrar")