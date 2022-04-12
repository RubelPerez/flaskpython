from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def pageNotFound(error):
    return render_template("error404.html", error=error), 404
