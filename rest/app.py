from flask import Flask, render_template, request
import indexPost

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if indexPost.verifyLogin(name, email) == 'ok':
            return render_template("index.html", name=name,email=email)
    return render_template("index.html",name="error")


@app.route("/productos")
def productos():
    return """
    <ol>
    <li>Pollo</li>
    <li>Gallo</li>
    <li>Gallina</li>
    </ol>
    """


@app.route("/longitud/<nombre>")
def longitud(nombre):
    return "hola {}, tienes una longitud de {} caracteres ".format(nombre, len(nombre))


@app.route("/login/<usuario>/<clave>")
def login(usuario, clave):
    if usuario == 'admin' and clave == 'admin':
        return "Inicio de sesion correcto"
    return "error iniciando sesion"


@app.route("/suma/<int:numero1>/<int:numero2>")
def sumar(numero1, numero2):
    return str(numero1 + numero2)


@app.route("/html")
def muestra():
    sqlResult = [{"nombre": "juan", "apellido": "Perez"}, {"nombre": "Peito"}]
    personalInfo = {"nombre": "Daniel", "apellido": "Pérez", "edad": 25, "vivencia": "Cornella"}
    return render_template("index.html", numeroA="25", numeroB="123123", sqlResult=sqlResult, dicc=personalInfo)


@app.route("/formulario", methods=['GET', 'POST'])
def formulario():
    return render_template("formulario.html")


@app.errorhandler(404)
def error(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
