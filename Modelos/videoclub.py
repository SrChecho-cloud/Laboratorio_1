from fpdf import FPDF
from datetime import datetime
import platform

class Videoclub:

    def __init__(self):
        self.__clientes = []
        self.__peliculas = []
        self.__alquileres = []

    # Getters
    def get_clientes(self):
        return self.__clientes.copy()

    def get_peliculas(self):
        return self.__peliculas.copy()

    def get_alquileres(self):
        return self.__alquileres.copy()

    # Registrar cliente
    def agregar_cliente(self, cliente):

        for c in self.__clientes:
            if c.get_id_cliente() == cliente.get_id_cliente():
                raise ValueError("El cliente ya existe")

            if c.get_dni() == cliente.get_dni():
                raise ValueError("El DNI ya está registrado")

        self.__clientes.append(cliente)

    # Registrar pelicula
    def agregar_pelicula(self, pelicula):

        for p in self.__peliculas:
            if p.get_id_pelicula() == pelicula.get_id_pelicula():
                raise ValueError("La pelicula ya existe")

        self.__peliculas.append(pelicula)

    # Buscar cliente
    def buscar_cliente(self, id_cliente):

        for cliente in self.__clientes:
            if cliente.get_id_cliente() == id_cliente:
                return cliente

        return None

    # Buscar pelicula
    def buscar_pelicula(self, id_pelicula):

        for pelicula in self.__peliculas:
            if pelicula.get_id_pelicula() == id_pelicula:
                return pelicula

        return None

    # Registrar alquiler
    def registrar_alquiler(self, alquiler):

        cliente = alquiler.get_cliente()
        pelicula = alquiler.get_pelicula()

        if self.buscar_cliente(cliente.get_id_cliente()) is None:
            raise ValueError("El cliente no está registrado")

        if self.buscar_pelicula(pelicula.get_id_pelicula()) is None:
            raise ValueError("La pelicula no está registrada")

        if not pelicula.get_disponible():
            raise ValueError("La pelicula no está disponible")

        pelicula.set_disponible(False)
        self.__alquileres.append(alquiler)

        return True

    # Registrar devolucion
    def registrar_devolucion(self, devolucion):

        cliente = devolucion.get_cliente()
        pelicula = devolucion.get_pelicula()

        for alquiler in self.__alquileres:

            if (alquiler.get_cliente().get_id_cliente() == cliente.get_id_cliente()
                and alquiler.get_pelicula().get_id_pelicula() == pelicula.get_id_pelicula()
                and alquiler.get_activo()):

                alquiler.set_activo(False)
                pelicula.set_disponible(True)

                return True

        raise ValueError("No existe un alquiler activo para esta pelicula")


    # Generar PDF
    def generar_pdf(self):

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        # Titulo
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 10, "BLOCKBUSTER", align="C")
        pdf.ln(15)

        # Informacion del sistema
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Informacion del sistema")
        pdf.ln(10)

        pdf.set_font("Helvetica", size=11)
        pdf.cell(0, 8, f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
        pdf.ln(8)
        pdf.cell(0, 8, f"Sistema operativo: {platform.system()} {platform.release()}")
        pdf.ln(8)
        pdf.cell(0, 8, f"Clientes registrados: {len(self.__clientes)}")
        pdf.ln(15)

        # Catalogo de peliculas
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Catalogo de peliculas")
        pdf.ln(10)

        pdf.set_font("Helvetica", size=11)

        if self.__peliculas:
            for pelicula in self.__peliculas:
                estado = "Disponible" if pelicula.get_disponible() else "Alquilada"

                texto = (
                    f"ID: {pelicula.get_id_pelicula()} | "
                    f"Titulo: {pelicula.get_titulo()} | "
                    f"Genero: {pelicula.get_genero()} | "
                    f"Anio: {pelicula.get_anio()} | "
                    f"Estado: {estado}"
                )

                pdf.multi_cell(0, 8, texto)
        else:
            pdf.cell(0, 8, "No hay peliculas registradas.")

        pdf.ln(10)

        # Alquileres activos
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Alquileres activos")
        pdf.ln(10)

        pdf.set_font("Helvetica", size=11)

        alquileres_activos = 0

        for alquiler in self.__alquileres:
            if alquiler.get_activo():
                cliente = alquiler.get_cliente()
                pelicula = alquiler.get_pelicula()

                pdf.multi_cell(
                    0,
                    8,
                    f"Cliente: {cliente.get_nombre()} | "
                    f"Pelicula: {pelicula.get_titulo()} | "
                    f"Fecha: {alquiler.get_fecha_alquiler()}"
                )

                alquileres_activos += 1

        if alquileres_activos == 0:
            pdf.cell(0, 8, "No hay alquileres activos.")

        pdf.output("reporte_videoclub.pdf")

        print("PDF generado correctamente: reporte_videoclub.pdf")