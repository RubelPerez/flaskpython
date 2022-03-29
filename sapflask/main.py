import json

# import flask
from flask import Flask, jsonify, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL
from sqlalchemy import create_engine

app = Flask(__name__)

# CONFIG DB
MYSQL_DATABASE_USER = 'root'
MYSQL_DATABASE_PASSWORD = ''
MYSQL_DATABASE_DB = 'sap_fl_db'
MYSQL_DATABASE_HOST = 'localhost'
FULL_URL_DB = f"mysql+pymysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}/{MYSQL_DATABASE_DB}?charset=utf8mb4"
# engine = create_engine(
#    f"mysql+pymysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}/{MYSQL_DATABASE_DB}?charset=utf8mb4")

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TACK_MODIFICATIONS'] = False

# inicializacion de DB

db = SQLAlchemy(app)

# config migrations
migrate = Migrate()
migrate.init_app(app, db)


# la tabla de la db
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    email = db.Column(db.String(250))

    def __str__(self):
        return \
            (
                f'id:{self.id}, '
                f'nombre:{self.nombre} , '
                f'apellido:{self.apellido} , '
                f'email:{self.email} '
            )


@app.route("/")
def index():
    # get Personas
    personas = Persona.query.all()    
    # print(type(personas))
    # print(personas[0])
    return jsonify([personas.to_json() for user in personas])


