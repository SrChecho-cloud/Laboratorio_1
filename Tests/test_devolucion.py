
from modelos.cliente import Cliente
from modelos.pelicula import pelicula
from modelos.devolucion import Devolucion


def test_crear_devolucion():
    cliente = Cliente(1, "Sergio", "12575987")
    peli = pelicula(1, "Titanic", "Romance", 1997)

    devolucion = Devolucion(cliente, peli)

    assert devolucion.get_cliente() == cliente
    assert devolucion.get_pelicula() == peli


def test_ejecutar_devolucion():
    cliente = Cliente(1, "Sergio", "12575987")
    peli = pelicula(1, "Titanic", "Romance", 1997)

    devolucion = Devolucion(cliente, peli)

    class VideoclubPrueba:
        def registrar_devolucion(self, devolucion_recibida):
            return devolucion_recibida == devolucion

    videoclub = VideoclubPrueba()

    assert devolucion.ejecutar(videoclub) == True
