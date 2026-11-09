
import pytest

from modelos.operacion import Operacion
from modelos.cliente import Cliente
from modelos.pelicula import pelicula


class OperacionPrueba(Operacion):

    def ejecutar(self, videoclub):
        pass


def test_operacion_abstracta():
    cliente = Cliente(1, "Sergio", "12575987")
    peli = pelicula(1, "Titanic", "Romance", 1997)

    with pytest.raises(TypeError):
        Operacion(cliente, peli)


def test_getters_y_setters():
    cliente = Cliente(1, "Sergio", "12575987")
    cliente2 = Cliente(2, "Pepe", "98753215")

    peli = pelicula(1, "Titanic", "Romance", 1997)
    peli2 = pelicula(2, "Matrix", "Ciencia ficcion", 1999)

    operacion = OperacionPrueba(cliente, peli)

    assert operacion.get_cliente() == cliente
    assert operacion.get_pelicula() == peli

    operacion.set_cliente(cliente2)
    operacion.set_pelicula(peli2)

    assert operacion.get_cliente() == cliente2
    assert operacion.get_pelicula() == peli2
