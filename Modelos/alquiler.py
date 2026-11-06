
from datetime import date
from modelos.operacion import Operacion


class Alquiler(Operacion):

    def __init__(self, cliente, pelicula):
        super().__init__(cliente, pelicula)
        self.__fecha_alquiler = date.today()
        self.__activo = True

    # Getters
    def get_fecha_alquiler(self):
        return self.__fecha_alquiler

    def get_activo(self):
        return self.__activo

    # Setter
    def set_activo(self, activo):
        self.__activo = activo

    def ejecutar(self, videoclub):
        return videoclub.registrar_alquiler(self)
