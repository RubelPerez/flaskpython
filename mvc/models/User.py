from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    age = db.Column(db.String(120))
    address = db.Column(db.String(120))

    def __init__(self, name, age, adrres):
        self.name = name
        self.age = age
        self.address = adrres
