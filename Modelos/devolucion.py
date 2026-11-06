
from modelos.operacion import Operacion


class Devolucion(Operacion):

    def __init__(self, cliente, pelicula):
        super().__init__(cliente, pelicula)

    def ejecutar(self, videoclub):
        return videoclub.registrar_devolucion(self)
