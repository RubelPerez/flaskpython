import os

from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Forms import RegisterForm, DeleteForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db_otra'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)

Migrate(app, database)


class Mascota(database.Model):
    __tablename__ = "Mascotas"
    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.Text(120))

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        text = '[!] {}'.format(self.nombre)
        return text


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/list")
def list():
    mascotas = Mascota.query.all()
    print(mascotas)
    return render_template("list.html", mascotas=mascotas)


@app.route("/register", methods=['GET', 'POST'])
def register():
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        nombre = registerForm.nombre.data
        mascota = Mascota(nombre)
        database.session.add(mascota)
        database.session.commit()
        return redirect(url_for("register"))

    return render_template("register.html", formulario=registerForm)


@app.route("/delete", methods=['GET', 'POST'])
def delete():
    registerForm = DeleteForm()
    if registerForm.validate_on_submit():
        id = registerForm.id.data
        mascota = Mascota.query.get(id)
        database.session.delete(mascota)
        database.session.commit()
        flash('Eliminado correctamente')
        return redirect(url_for("delete"))

    return render_template("delete.html", formulario=registerForm)
