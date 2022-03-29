import json

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db_movies'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)


class Movies(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    image = database.Column(database.Text)
    movie = database.Column(database.Text)
    year = database.Column(database.Text)
    description = database.Column(database.Text)

    def __init__(self, image, movie, year, description):
        self.image = image
        self.movie = movie
        self.year = year
        self.description = description

    def __repr__(self):
        return "movie: {} image: {} year: {} description {}".format(self.movie, self.image, self.year, self.description)


@app.route("/")
def index():
    pelicula = Movies.query.get(13)
    pelicula.description = "Mondongo"
    database.session.add(pelicula)
    database.session.commit()
    return render_template("lista.html")
