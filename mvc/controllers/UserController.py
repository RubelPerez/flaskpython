import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
from models.User import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def index():
    user = User.query.all()

    return jsonify(user)


def store():
    name = request.form.get('name')
    age = request.form.get('age')
    address = request.form.get('address')
    user = User(name, age, address)
    db.session.add(user)
    db.session.commit()
    return "klk"


def show(user_id):
    print("show", user_id)
    return str(user_id)


def update(user_id):
    print("update", user_id)
    return str(user_id)


def delete(user_id):
    print("delete", user_id)
    return str(user_id)


def destroy(user_id):
    print("destroy", user_id)
    return str(user_id)
