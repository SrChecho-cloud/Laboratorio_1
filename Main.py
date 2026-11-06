from modelos.videoclub import Videoclub
from modelos.cliente import Cliente
from modelos.pelicula import pelicula
from modelos.alquiler import Alquiler
from modelos.devolucion import Devolucion

videoclub = Videoclub()

while True:

    print("\n===== BLOCKBUSTER =====")
    print("1. Registrar cliente")
    print("2. Agregar película")
    print("3. Mostrar clientes")
    print("4. Mostrar catálogo")
    print("5. Buscar película")
    print("6. Alquilar película")
    print("7. Devolver película")
    print("8. Mostrar alquileres activos")
    print("9. Generar PDF")
    print("0. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        print("Registrar cliente")
        try:
            id_cliente = int(input("Ingrese el ID del cliente: "))
            nombre = input("Ingrese el nombre del cliente: ")
            dni = input("Ingrese el DNI del cliente: ")
            cliente = Cliente(id_cliente, nombre, dni)
            videoclub.agregar_cliente(cliente)
        except ValueError:
            print("Error: El ID del cliente ya está registrado.")


    elif opcion == "2":
        print("Agregar película")

        try:
            id_pelicula = int(input("Ingrese el ID de la pelicula: "))
            titulo = input("Ingrese el titulo de la pelicula: ")
            genero = input("Ingrese el genero de la pelicula: ")
            anio = int(input("Ingrese el año de la pelicula: "))

            nueva_pelicula = pelicula(id_pelicula, titulo, genero, anio)
            videoclub.agregar_pelicula(nueva_pelicula)

            print("Pelicula agregada correctamente")

        except ValueError as error:
            print("Error:", error)


    elif opcion == "3":
        print("Mostrar clientes")
        for cliente in videoclub.get_clientes():
            print(f"ID: {cliente.get_id_cliente()}, Nombre: {cliente.get_nombre()}, DNI: {cliente.get_dni()}")


    elif opcion == "4":
        print("Mostrar catálogo")
        for pelicula in videoclub.get_peliculas():
            print(f"ID: {pelicula.get_id_pelicula()}, Titulo: {pelicula.get_titulo()}, Genero: {pelicula.get_genero()}, Año: {pelicula.get_anio()}, Disponible: {pelicula.get_disponible()}")



    elif opcion == "5":
        print("Buscar película")
        try:
            id_pelicula = int(input("Ingrese el ID de la pelicula: "))
            pelicula = videoclub.buscar_pelicula(id_pelicula)
            if pelicula:
                print(f"ID: {pelicula.get_id_pelicula()}, Titulo: {pelicula.get_titulo()}, Genero: {pelicula.get_genero()}, Año: {pelicula.get_anio()}, Disponible: {pelicula.get_disponible()}")
            else:
                print("La pelicula no está registrada")
        except ValueError:
            print("Error: El ID de la película debe ser un número entero.")


    elif opcion == "6":
        print("Alquilar película")

        try:
            id_pelicula = int(input("Ingrese el ID de la pelicula: "))
            id_cliente = int(input("Ingrese el ID del cliente: "))

            pelicula = videoclub.buscar_pelicula(id_pelicula)
            cliente = videoclub.buscar_cliente(id_cliente)

            if pelicula and cliente:
                alquiler = Alquiler(cliente, pelicula)
                alquiler.ejecutar(videoclub)
                print("Alquiler registrado exitosamente")
            else:
                print("El cliente o la pelicula no estan registrados")
        except ValueError as error:
            print("Error: ingrese un ID válido para la pelicula y el cliente.")

    elif opcion == "7":
        print("Devolver película")

        try:
            id_pelicula = int(input("Ingrese el ID de la pelicula: "))
            id_cliente = int(input("Ingrese el ID del cliente: "))

            pelicula = videoclub.buscar_pelicula(id_pelicula)
            cliente = videoclub.buscar_cliente(id_cliente)

            if pelicula and cliente:
                devolucion = Devolucion(cliente, pelicula)
                devolucion.ejecutar(videoclub)
                print("Devolucion realizada correctamente")
            else:
                print("Cliente o pelicula no encontrados")
        except ValueError as error:
            print("Error: ingrese un ID válido para la pelicula y el cliente.")


    elif opcion == "8":
        print("Mostrar alquileres activos")

        for alquiler in videoclub.get_alquileres():
            if alquiler.get_activo():
                print(f"Pelicula: {alquiler.get_pelicula().get_titulo()}, Cliente: {alquiler.get_cliente().get_nombre()}")


    elif opcion == "9":
        print("Generar PDF")
        videoclub.generar_pdf()


    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción incorrecta")