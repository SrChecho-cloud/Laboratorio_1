
class Cliente:

    def __init__(self, id_cliente, nombre, dni):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__dni = dni

    # Getters
    def get_id_cliente(self):
        return self.__id_cliente

    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__dni

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_dni(self, dni):
        self.__dni = dni

