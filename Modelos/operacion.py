
from abc import ABC, abstractmethod


class Operacion(ABC):

    def __init__(self, cliente, pelicula):
        self.__cliente = cliente
        self.__pelicula = pelicula

    # Getters
    def get_cliente(self):
        return self.__cliente

    def get_pelicula(self):
        return self.__pelicula

    # Setters
    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_pelicula(self, pelicula):
        self.__pelicula = pelicula

    @abstractmethod
    def ejecutar(self, videoclub):
        pass
