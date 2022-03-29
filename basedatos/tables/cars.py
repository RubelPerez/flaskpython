class Car(database.Model):
    # __tablename__ = 'Cars'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.Text(50))
    model = database.Column(database.Text(50))
    year = database.Column(database.Text(5))

    def __init__(self, id, name, model, year):
        self.name = name
        self.model = model
        self.year = year
