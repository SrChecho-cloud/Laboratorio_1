
from modelos.pelicula import pelicula


def test_crear_pelicula():
    peli = pelicula(1, "Titanic", "Romance", 1997)

    assert peli.get_id_pelicula() == 1
    assert peli.get_titulo() == "Titanic"
    assert peli.get_genero() == "Romance"
    assert peli.get_anio() == 1997
    assert peli.get_disponible() == True


def test_set_titulo():
    peli = pelicula(1, "Titanic", "Romance", 1997)

    peli.set_titulo("Matrix")

    assert peli.get_titulo() == "Matrix"


def test_set_genero():
    peli = pelicula(1, "Titanic", "Romance", 1997)

    peli.set_genero("Accion")

    assert peli.get_genero() == "Accion"


def test_set_anio():
    peli = pelicula(1, "Titanic", "Romance", 1997)

    peli.set_anio(2000)

    assert peli.get_anio() == 2000


def test_set_disponible():
    peli = pelicula(1, "Titanic", "Romance", 1997)

    peli.set_disponible(False)

    assert peli.get_disponible() == False
