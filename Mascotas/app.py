from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/mascotas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)

Migrate(app, database)


class Mascota(database.Model):
    __tablename__ = "Mascotas"
    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.Text(150))
    juguetes = database.relationship('Juguetes', backref='mascota', uselist=False)
    propietario = database.relationship('Propietario', backref='mascota', uselist=False)

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        texto = "aqui {}".format(self.nombre)
        return texto

    def mostrar_juegos(self):
        for i in self.juguetes:
            print(i)


class Juguetes(database.Model):
    __tablename__ = "Juguetes"
    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.Text)
    mascotas_id = database.Column(database.Integer, database.ForeignKey('Mascotas.id'))

    def __init__(self, nombre, mascotas_id):
        self.nombre = nombre
        self.mascotas_id = mascotas_id


class Propietario(database.Model):
    __tablename__ = "Propietarios"
    id = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.Text(125))
    mascotas_id = database.Column(database.Integer, database.ForeignKey('Mascotas.id'))

    def __init__(self, nombre, mascotas_id):
        self.nombre = nombre
        self.mascotas_id = mascotas_id
