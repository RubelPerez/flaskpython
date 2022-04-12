from flask import Flask, jsonify, request
from products import productos

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"productos": productos})


@app.route("/<string:name>")
def filterByname(name):
    for p in productos:
        if name.lower() == p["nombre"].lower():
            return p
    return "nada"


@app.route("/actualizar/<string:nombre>", methods=['PUT'])
def update(nombre):
    productoF = [producto for producto in productos if producto['nombre'].lower() == nombre.lower()]
    if len(productoF) > 0:
        productoF[0]['nombre'] = request.json['nombre']
        productoF[0]['precio'] = request.json['precio']
        productoF[0]['cantidad'] = request.json['cantidad']
        return jsonify({"prductos": productos})
    return "nada"


@app.route("/delete/<string:nombre>", methods=['DELETE'])
def delete(nombre):
    productoD = [producto for producto in productos if producto['nombre'].lower() == nombre.lower()]
    if len(productoD) > 0:
        print("productoD",productoD)
        productos.remove(productoD[0])
        return jsonify({"productos":productos})
    return "error"