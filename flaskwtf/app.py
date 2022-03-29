from flask import Flask, render_template, url_for, session
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import *
from wtforms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YXNkYXNkYXNkYXNk'
app.secret_key = 'BAD_SECRET_KEY'


class Formulario(FlaskForm):
    nombre = StringField('nombre')
    apellido = StringField('apellido')
    telefono = StringField('telefono')
    estado = SubmitField('estado')


def saveSessionVars(nombre, apellido, telefono, estado):
    session['nombre'] = nombre
    session['apellido'] = apellido
    session['telefono'] = telefono
    session['estado'] = estado


@app.route("/", methods=['GET', 'POST'])
def index():
    nombre = ' '
    apellido = ' '
    telefono = ' '
    estado = False
    formulario = Formulario()

    if formulario.validate_on_submit():
        estado = True
        nombre = formulario.nombre.data
        apellido = formulario.apellido.data
        telefono = formulario.telefono.data
        saveSessionVars(nombre, apellido, telefono, estado)
    return render_template("wtf.html", formulario=formulario, estado=estado, nombre=nombre, apellido=apellido,
                           telefono=telefono)


@app.route("/informacion")
def informacion():
    return render_template("informacion.html", nombre=session.pop('nombre'), apellido=session.pop('apellido'),
                           telefono=session.pop('telefono'), estado=session.pop('estado'))


if __name__ == "__main__":
    app.run()
