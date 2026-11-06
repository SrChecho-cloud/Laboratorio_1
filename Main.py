
from modelos.cliente import Cliente
from modelos.pelicula import PeliculaDVD
from modelos.alquiler import Alquiler
from modelos.devolucion import Devolucion
from modelos.videoclub import Videoclub


# Crear videoclub
videoclub = Videoclub()

# Registrar cliente
cliente1 = Cliente(1, "Juan", "40123456")
videoclub.agregar_cliente(cliente1)

# Registrar pelicula
pelicula1 = PeliculaDVD(1, "Titanic", "Romance", 1997)
videoclub.agregar_pelicula(pelicula1)

# Mostrar disponibilidad inicial
print("Disponibilidad inicial:", pelicula1.get_disponible())


# Realizar alquiler
alquiler1 = Alquiler(cliente1, pelicula1)

try:
    alquiler1.ejecutar(videoclub)
    print("Alquiler realizado correctamente")

except ValueError as error:
    print("Error:", error)

print("Disponibilidad despues del alquiler:", pelicula1.get_disponible())


# Realizar devolucion
devolucion1 = Devolucion(cliente1, pelicula1)

try:
    devolucion1.ejecutar(videoclub)
    print("Devolucion realizada correctamente")

except ValueError as error:
    print("Error:", error)

print("Disponibilidad despues de la devolucion:", pelicula1.get_disponible())
