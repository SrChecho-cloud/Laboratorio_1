
from modelos.cliente import Cliente
from modelos.pelicula import pelicula
from modelos.alquiler import Alquiler


def test_crear_alquiler():
    cliente = Cliente(1, "Sergio", "12575987")
    peli = pelicula(1, "Titanic", "Romance", 1997)

    alquiler = Alquiler(cliente, peli)

    assert alquiler.get_cliente() == cliente
    assert alquiler.get_pelicula() == peli
    assert alquiler.get_activo() == True
    assert alquiler.get_fecha_alquiler() is not None


def test_set_activo():
    cliente = Cliente(1, "Sergio", "12575987")
    peli = pelicula(1, "Titanic", "Romance", 1997)

    alquiler = Alquiler(cliente, peli)

    alquiler.set_activo(False)

    assert alquiler.get_activo() == False


def test_ejecutar_alquiler():
    cliente = Cliente(1, "Sergio", "12575987")
    peli = pelicula(1, "Titanic", "Romance", 1997)

    alquiler = Alquiler(cliente, peli)

    class VideoclubPrueba:
        def registrar_alquiler(self, alquiler_recibido):
            return alquiler_recibido == alquiler

    videoclub = VideoclubPrueba()

    assert alquiler.ejecutar(videoclub) == True
