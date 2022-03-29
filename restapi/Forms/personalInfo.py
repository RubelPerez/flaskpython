from flask_wtf import FlaskForm
from wtforms import *


class FormInfo(FlaskForm):
    mensaje = StringField('mensaje')
    aceptar = SubmitField('aceptar')
