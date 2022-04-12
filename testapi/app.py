import os

from flask import Flask, jsonify, session, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db_movies'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app)

app.secret_key = os.urandom(64)


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


@app.route("/")
def index():
    if 'username' in session:
        return "hola papito mi rey"
    return "klk tu quiere?"


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form.get('username') == 'daniel':
        txtUsername = request.form.get('username')
        session['username'] = txtUsername
        return redirect(url_for("index"))

    return render_template("login.html", )


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    try:
        session.pop('username')
        return redirect(url_for("index"))
    except:
        return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
