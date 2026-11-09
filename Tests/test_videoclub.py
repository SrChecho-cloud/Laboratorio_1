
import pytest

from modelos.videoclub import Videoclub
from modelos.cliente import Cliente
from modelos.pelicula import pelicula
from modelos.alquiler import Alquiler
from modelos.devolucion import Devolucion


def test_getters():
    videoclub = Videoclub()

    assert videoclub.get_clientes() == []
    assert videoclub.get_peliculas() == []
    assert videoclub.get_alquileres() == []


def test_agregar_cliente():
    videoclub = Videoclub()
    cliente = Cliente(1, "Sergio", "12575987")

    videoclub.agregar_cliente(cliente)

    assert cliente in videoclub.get_clientes()


def test_cliente_id_duplicado():
    videoclub = Videoclub()
    cliente1 = Cliente(1, "Sergio", "12575987")
    cliente2 = Cliente(1, "Pepe", "98753215")

    videoclub.agregar_cliente(cliente1)

    with pytest.raises(ValueError):
        videoclub.agregar_cliente(cliente2)


def test_cliente_dni_duplicado():
    videoclub = Videoclub()
    cliente1 = Cliente(1, "Sergio", "12575987")
    cliente2 = Cliente(2, "Pepe", "12575987")

    videoclub.agregar_cliente(cliente1)

    with pytest.raises(ValueError):
        videoclub.agregar_cliente(cliente2)


def test_agregar_pelicula():
    videoclub = Videoclub()
    peli = pelicula(1, "Titanic", "Romance", 1997)

    videoclub.agregar_pelicula(peli)

    assert peli in videoclub.get_peliculas()


def test_pelicula_id_duplicado():
    videoclub = Videoclub()
    peli1 = pelicula(1, "Titanic", "Romance", 1997)
    peli2 = pelicula(1, "Matrix", "Accion", 1999)

    videoclub.agregar_pelicula(peli1)

    with pytest.raises(ValueError):
        videoclub.agregar_pelicula(peli2)


def test_buscar_cliente():
    videoclub = Videoclub()
    cliente = Cliente(1, "Sergio", "12575987")
    videoclub.agregar_cliente(cliente)

    assert videoclub.buscar_cliente(1) == cliente


def test_buscar_cliente_inexistente():
    videoclub = Videoclub()

    assert videoclub.buscar_cliente(99) is None


def test_buscar_pelicula():
    videoclub = Videoclub()
    peli = pelicula(1, "Titanic", "Romance", 1997)
    videoclub.agregar_pelicula(peli)

    assert videoclub.buscar_pelicula(1) == peli


def test_buscar_pelicula_inexistente():
    videoclub = Videoclub()

    assert videoclub.buscar_pelicula(99) is None


def test_registrar_alquiler():
    videoclub = Videoclub()
    cliente = Cliente(1, "Sergio", "12575987")
    peli = pelicula(1, "Titanic", "Romance", 1997)

    videoclub.agregar_cliente(cliente)
    videoclub.agregar_pelicula(peli)

    alquiler = Alquiler(cliente, peli)
    videoclub.registrar_alquiler(alquiler)

    assert alquiler in videoclub.get_alquileres()
    assert peli.get_disponible() == False


def test_alquiler_cliente_no_registrado():
    videoclub = Videoclub()
    cliente = Cliente(1, "Sergio", "12575987")
    peli = pelicula(1, "Titanic", "Romance", 1997)

    videoclub.agregar_pelicula(peli)

    alquiler = Alquiler(cliente, peli)

    with pytest.raises(ValueError):
        videoclub.registrar_alquiler(alquiler)


def test_alquiler_pelicula_no_registrada():
    videoclub = Videoclub()
    cliente = Cliente(1, "Sergio", "12575987")
    peli = pelicula(1, "Titanic", "Romance", 1997)

    videoclub.agregar_cliente(cliente)

    alquiler = Alquiler(cliente, peli)

    with pytest.raises(ValueError):
        videoclub.registrar_alquiler(alquiler)


def test_alquiler_pelicula_no_disponible():
    videoclub = Videoclub()
    cliente = Cliente(1, "Sergio", "12575987")
    peli = pelicula(1, "Titanic", "Romance", 1997)

    videoclub.agregar_cliente(cliente)
    videoclub.agregar_pelicula(peli)

    alquiler1 = Alquiler(cliente, peli)
    videoclub.registrar_alquiler(alquiler1)

    alquiler2 = Alquiler(cliente, peli)

    with pytest.raises(ValueError):
        videoclub.registrar_alquiler(alquiler2)


def test_registrar_devolucion():
    videoclub = Videoclub()
    cliente = Cliente(1, "Sergio", "12575987")
    peli = pelicula(1, "Titanic", "Romance", 1997)

    videoclub.agregar_cliente(cliente)
    videoclub.agregar_pelicula(peli)

    alquiler = Alquiler(cliente, peli)
    videoclub.registrar_alquiler(alquiler)

    devolucion = Devolucion(cliente, peli)
    videoclub.registrar_devolucion(devolucion)

    assert alquiler.get_activo() == False
    assert peli.get_disponible() == True


def test_devolucion_sin_alquiler_activo():
    videoclub = Videoclub()
    cliente = Cliente(1, "Sergio", "12575987")
    peli = pelicula(1, "Titanic", "Romance", 1997)

    videoclub.agregar_cliente(cliente)
    videoclub.agregar_pelicula(peli)

    devolucion = Devolucion(cliente, peli)

    with pytest.raises(ValueError):
        videoclub.registrar_devolucion(devolucion)


def test_generar_pdf(tmp_path, monkeypatch):
    videoclub = Videoclub()

    monkeypatch.chdir(tmp_path)

    videoclub.generar_pdf()

    assert (tmp_path / "reporte_videoclub.pdf").exists()
