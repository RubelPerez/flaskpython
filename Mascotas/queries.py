from app import database, Mascota, Juguetes, Propietario

# insert

insertMascota = Mascota('Jose')
database.session.add(insertMascota)
database.session.commit()

# Consultas select all
selectAll = Mascota.query.all()
print(selectAll)

# insert propietario
insertPropietario = Propietario('Arturo Jr', insertMascota.id)
database.session.add(insertPropietario)
database.session.commit()

# inser jugete
insertJuguete = Juguetes('Balon de futbol Jr', insertMascota.id)
database.session.add(insertJuguete)
database.session.commit()

# mostrar todo
mostrarTodo = Mascota.query.filter_by(nombre='Jose').first()
# print("aqui",mostrarTodo)
mostrarTodo.mostrar_juegos()
