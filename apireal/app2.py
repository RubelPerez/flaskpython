# # from flask import Flask, jsonify
# # from flask_restful import Resource, Api
# #
# # app = Flask(__name__)
# # api = Api(app)
# #
# # #
# # # class Clientes(Resource):
# # #     def get(self):
# # #         return {"cliente1": [num for num in range(1, 11) if num % 2 != 0]}
# # #
# # #
# # # api.add_resource(Clientes, "/")
# # nombres = [
# #
# # ]
# #
# #
# # class Nombres(Resource):
# #     def get(self, id):
# #         for n in nombres:
# #             if n == id:
# #                 return {'nombre': n}
# #         return {"resultado": "no existe"}
# #
# #     def post(self, id):
# #         nombres.append(id)
# #         return {"resultado": "Nombre agregado"}
# #
# #     def delete(self, id):
# #         for indice, n in enumerate(nombres):
# #             if n == id:
# #                 nombres.pop(indice)
# #                 return {"resultado": "eliminado correcto"}
# #
# #
# # class Listar(Resource):
# #     def get(self):
# #         return {"productos":nombres}
# #
# #
# # api.add_resource(Nombres, "/nombres/<string:id>")
# # api.add_resource(Listar,"/listar")
# # if __name__ == "__main__":
# #     app.run()
# from flask import Flask, redirect, url_for
# from flask_restful import Api, Resource
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
#
# app = Flask(__name__)
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db_movies'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# database = SQLAlchemy(app)
# Migrate(app, database)
# api = Api(app)
#
#
# class ProductosDB(database.Model):
#     __tablename__ = "productos"
#     id = database.Column(database.Integer, primary_key=True)
#     nombre = database.Column(database.Text(255))
#     apellido = database.Column(database.Text(255))
#     telefono = database.Column(database.Text(255))
#
#     def __init__(self, nombre, apellido, telefono):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.telefono = telefono
#
#     def json(self):
#         return {"id": self.id, "nombre": self.nombre, "apellido": self.apellido, "telefono": self.telefono}
#
#
# class Productos(Resource):
#     def get(self, valor, apellido, telefono):
#         producto = ProductosDB.query.filter_by(id=valor).first()
#         print(producto.nombre)
#         if producto:
#             return producto.json()
#         return {"resultado": "no existe"}
#
#     def post(self, valor, apellido, telefono):
#         producto = ProductosDB(nombre=valor, apellido=apellido, telefono=telefono)
#         database.session.add(producto)
#         database.session.commit()
#         return redirect("/listado")
#
#     def delete(self, valor, apellido, telefono):
#         producto = ProductosDB.query.filter_by(id=valor).first()
#         database.session.delete(producto)
#         database.session.commit()
#         return ({"resultado": "eliminado correctamente"})
#
#
# class ListarTodo(Resource):
#     def get(self):
#         productos = ProductosDB.query.all()
#         listado = [p.json() for p in productos]
#         return ({"resultados": listado})
#
#
# api.add_resource(Productos, "/<string:valor>/<string:apellido>/<string:telefono>")
# api.add_resource(ListarTodo, "/listado")
