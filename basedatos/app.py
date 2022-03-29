from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from tables.cars import Car

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)
Migrate(app, database)
Car()


@app.route("/hola")
def hola():
    return "hola"
