from flask import Flask, render_template, session, redirect, url_for, flash
from Forms.personalInfo import FormInfo

app = Flask(__name__)
app.config['SECRET_KEY'] = "khasvdkhasbdklasjdblajsbdlajbsdljasd"


@app.route("/", methods=['GET', 'POST'])
def index():
    nombre = ' '
    apellido = ' '
    cedula = ' '
    aceptar = False
    formulario = FormInfo()
    if formulario.validate_on_submit():
        session['nombre'] = formulario.nombre.data
        session['apellido'] = formulario.apellido.data
        session['cedula'] = formulario.cedula.data
        session['aceptar'] = True
        app.logger.info("klk wawawa")
        return redirect(url_for("informacion"))
    return render_template("index.html", formulario=formulario)


#
# class ElFormulario(FlaskForm):
#     mensaje = StringField('mensaje')
#     aceptar = SubmitField('aceptar')


@app.route("/informacion", methods=['GET', 'POST'])
def informacion():
    mensaje = ' '
    elFormulario = FormInfo()
    if elFormulario.validate_on_submit():
        mensaje = elFormulario.mensaje.data
        if mensaje != "Daniel":
            flash(mensaje)
            return redirect(url_for("informacion"))
    return render_template("alerta.html", formulario=elFormulario, mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
