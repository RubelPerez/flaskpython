from app import Movies, database

# INSERT
database.create_all()
pelicula1 = Movies("image", "movie", "year", "description")
pelicula2 = Movies('Imagen Dura', 'Irene yo', '2003', 'pelicula comica')
database.session.add_all([pelicula1, pelicula2])
database.session.commit()

pelicula3 = Movies("foto 2x2", "startt wars", "1989", "guera de las gfalaxias")
database.session.add(pelicula3)
database.session.commit()
# fin insert

# SELECT
peliculas = Movies.query.all()
print("todas las peliculas")
print(peliculas)

filtrado = Movies.query.filter_by(movie="movie")
print("estamos filtrando...")
print(filtrado.all())

filtradoId = Movies.query.get(1)
print("Buscando por filtradoId...")
print(filtradoId)
# fin select

# update
pelicula = Movies.query.get(4)
pelicula.year = "Morrow"
database.session.add(pelicula)
database.session.commit()

# delete
deleteMovie = Movies.query.get(15)
database.session.delete(deleteMovie)
database.session.commit()
print("se ha borrado ", deleteMovie)

# SELECT ALL
movies = Movies.query.all()
print("Despues de todo")
print(movies)
