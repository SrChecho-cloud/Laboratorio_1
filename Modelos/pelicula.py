
class pelicula:

    def __init__(self, id_pelicula, titulo, genero, anio):
        self.__id_pelicula = id_pelicula
        self.__titulo = titulo
        self.__genero = genero
        self.__anio = anio
        self.__disponible = True

    # Getters
    def get_id_pelicula(self):
        return self.__id_pelicula

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def get_anio(self):
        return self.__anio

    def get_disponible(self):
        return self.__disponible

    # Setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero

    def set_anio(self, anio):
        self.__anio = anio

    def set_disponible(self, disponible):
        self.__disponible = disponible
