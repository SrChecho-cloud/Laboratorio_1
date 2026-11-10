Blockbuster - Sistema de Videoclub

Sistema de gestión de un videoclub desarrollado en Python para el trabajo práctico integrador de la materia Laboratorio I.
El programa permite registrar clientes, administrar películas, gestionar alquileres y devoluciones, consultar la información disponible y generar un reporte en formato PDF.
Funcionalidades

El sistema cuenta con un menú principal con las siguientes opciones:
Registrar cliente
Permite ingresar el ID, nombre y DNI de un cliente.
No permite registrar dos clientes con el mismo ID o DNI.
Agregar película
Permite ingresar el ID, título, género y año de una película.
Cada película debe tener un ID único.
Las películas se registran inicialmente como disponibles.
Mostrar clientes
Muestra todos los clientes registrados junto con su ID, nombre y DNI.
Mostrar catálogo
Muestra todas las películas registradas.
Informa el ID, título, género, año y disponibilidad de cada película.
Buscar película
Permite buscar una película utilizando su ID.
Si la película existe, muestra sus datos y su estado de disponibilidad.
Alquilar película
Permite asociar una película disponible con un cliente registrado.
La película pasa a estar no disponible.
Se registra la fecha del alquiler.
No se permite alquilar una película que ya está alquilada.
Devolver película
Permite registrar la devolución de una película.
El alquiler pasa a estar inactivo.
La película vuelve a estar disponible.
Solo se pueden devolver películas que tengan un alquiler activo.
Mostrar alquileres activos
Muestra las películas que actualmente están alquiladas.
También informa el cliente asociado a cada alquiler.
Generar PDF
Genera el archivo reporte_videoclub.pdf en la carpeta desde la que se ejecuta el programa.
Salir
Finaliza la ejecución del sistema.
Tecnologías utilizadas

Tecnología	Uso
Python	Lenguaje principal del proyecto
FPDF2	Generación del reporte en formato PDF
Pytest	Ejecución de pruebas unitarias
Git	Control de versiones
GitHub	Alojamiento y colaboración sobre el repositorio
Dependencias del proyecto

Las dependencias declaradas en requirements.txt son:

text

colorama==0.4.6
fonttools==4.68.0
fpdf2==2.9.0
iniconfig==2.3.1
packaging==26.3
pillow==13.0.0
pluggy==1.7.0
Pygments==2.21.0
pytest==9.2.0
El programa utiliza directamente fpdf2 para generar el PDF y pytest para las pruebas unitarias. Las demás dependencias forman parte del archivo de requisitos del entorno del proyecto.
Estructura del proyecto


text

Laboratorio_1/
│
├── .gitignore
├── Main.py
├── README.md
├── requirements.txt
├── reporte_videoclub.pdf
│
├── Modelos/
│   ├── __init__.py
│   ├── alquiler.py
│   ├── cliente.py
│   ├── devolucion.py
│   ├── operacion.py
│   ├── pelicula.py
│   └── videoclub.py
│
└── Tests/
    ├── test_alquiler.py
    ├── test_cliente.py
    ├── test_devolucion.py
    ├── test_operacion.py
    ├── test_pelicula.py
    └── test_videoclub.py

Descripción de los archivos principales

Main.py
Contiene el menú principal y la interacción con el usuario.
Permite registrar clientes y películas, realizar alquileres y devoluciones, consultar información y generar el PDF.
Modelos/__init__.py
Identifica a Modelos como un paquete de Python.
Modelos/cliente.py
Define la clase Cliente.
Contiene los datos del cliente: ID, nombre y DNI.
Modelos/pelicula.py
Define la clase pelicula.
Contiene los datos de una película y su estado de disponibilidad.
Modelos/operacion.py
Define la clase abstracta Operacion.
Es la clase base para las operaciones de alquiler y devolución.
Modelos/alquiler.py
Define la clase Alquiler.
Representa el alquiler de una película por parte de un cliente.
Modelos/devolucion.py
Define la clase Devolucion.
Representa la devolución de una película alquilada.
Modelos/videoclub.py
Define la clase Videoclub.
Administra las listas de clientes, películas y alquileres.
Controla altas, búsquedas, alquileres, devoluciones y generación de reportes.
Tests/
Contiene las pruebas unitarias del sistema.
requirements.txt
Contiene las dependencias y versiones utilizadas por el proyecto.
.gitignore
Indica archivos y carpetas que no deben incluirse en el control de versiones, como el entorno virtual, cachés de Python y archivos temporales.
reporte_videoclub.pdf
Es un reporte PDF generado por el sistema. El archivo se encuentra incluido como referencia, aunque los reportes generados están excluidos del control de versiones mediante .gitignore.
Programación orientada a objetos

El proyecto aplica los principales conceptos de la programación orientada a objetos.
Encapsulamiento

Los atributos de las clases se definen como atributos privados utilizando doble guion bajo.
Por ejemplo, en Modelos/cliente.py:

python

class Cliente:
    def __init__(self, id_cliente, nombre, dni):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__dni = dni
El acceso a estos datos se realiza mediante métodos públicos, como:

python

def get_nombre(self):
    return self.__nombre

def set_nombre(self, nombre):
    self.__nombre = nombre
También se aplica este concepto en Videoclub, donde las listas internas de clientes, películas y alquileres son privadas:

python

self.__clientes = []
self.__peliculas = []
self.__alquileres = []
Además, los métodos get_clientes, get_peliculas y get_alquileres devuelven copias de las listas.
Herencia

Las clases Alquiler y Devolucion heredan de la clase abstracta Operacion:

python

class Alquiler(Operacion):

python

class Devolucion(Operacion):
Ambas clases reutilizan los atributos y métodos definidos en Operacion, como el cliente y la película asociados.
Abstracción

La clase Operacion está definida como una clase abstracta utilizando ABC y abstractmethod:

python

from abc import ABC, abstractmethod

class Operacion(ABC):
    @abstractmethod
    def ejecutar(self, videoclub):
        pass
Esto establece que toda operación debe implementar el método ejecutar.
No se puede crear directamente una instancia de Operacion sin implementar ese método.
Polimorfismo

Alquiler y Devolucion implementan el método ejecutar de manera diferente:

python

class Alquiler(Operacion):
    def ejecutar(self, videoclub):
        return videoclub.registrar_alquiler(self)

python

class Devolucion(Operacion):
    def ejecutar(self, videoclub):
        return videoclub.registrar_devolucion(self)
Aunque ambas clases utilizan el mismo nombre de método, cada una ejecuta una operación distinta según el tipo de objeto.
Instalación y configuración

Requisitos

Se necesita tener instalado:
Python 3
Git
PowerShell en Windows
1. Clonar el repositorio

Desde PowerShell, ejecutar:

powershell

git clone https://github.com/SrChecho-cloud/Laboratorio_1.git
cd Laboratorio_1
Reemplazar <URL_DEL_REPOSITORIO> por la URL real del repositorio de GitHub.
2. Crear el entorno virtual


powershell

py -m venv venv
3. Activar el entorno virtual


powershell

.\venv\Scripts\Activate.ps1
Si PowerShell impide la ejecución de scripts, puede ser necesario habilitarla para el usuario actual:

powershell

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Luego volver a activar el entorno:

powershell

.\venv\Scripts\Activate.ps1
4. Instalar las dependencias


powershell

python -m pip install --upgrade pip
pip install -r requirements.txt
Ejecución

Con el entorno virtual activado y ubicándose en la raíz del proyecto, ejecutar:

powershell

python Main.py
También puede utilizarse:

powershell

py Main.py
El programa mostrará el menú principal en la consola.
Nota sobre los nombres de los módulos:
La carpeta del repositorio se llama Modelos, con mayúscula, pero los imports del código utilizan modelos en minúscula. En Windows normalmente no genera inconvenientes porque el sistema de archivos no distingue mayúsculas y minúsculas. En sistemas que sí distinguen mayúsculas y minúsculas, como algunas configuraciones de Linux, los imports deben coincidir con el nombre real de la carpeta.
Pruebas unitarias

Las pruebas se encuentran en la carpeta Tests:
Tests/test_alquiler.py
Tests/test_cliente.py
Tests/test_devolucion.py
Tests/test_operacion.py
Tests/test_pelicula.py
Tests/test_videoclub.py
Para ejecutar todas las pruebas desde PowerShell:

powershell

pytest
También se puede utilizar:

powershell

python -m pytest
Las pruebas verifican, entre otros aspectos:
Creación de clientes y películas.
Uso de getters y setters.
Registro de clientes.
Validación de IDs y DNI duplicados.
Registro de películas.
Búsqueda de clientes y películas.
Registro de alquileres.
Control de películas no disponibles.
Registro de devoluciones.
Validación de devoluciones sin alquiler activo.
Generación del archivo PDF.
Comportamiento de la clase abstracta Operacion.
Generación de PDF

El reporte se genera seleccionando la opción 9. Generar PDF del menú principal.
Internamente, el método generar_pdf() de la clase Videoclub utiliza la biblioteca FPDF2 y crea el archivo:

text

reporte_videoclub.pdf
El reporte contiene:
Título del sistema: BLOCKBUSTER.
Fecha y hora de generación.
Sistema operativo utilizado.
Cantidad de clientes registrados.
Catálogo completo de películas.
ID, título, género, año y estado de cada película.
Listado de alquileres activos.
Nombre del cliente, título de la película y fecha del alquiler.
El archivo se genera en la carpeta actual desde la que se ejecuta el programa.
Almacenamiento de datos

El sistema no utiliza una base de datos ni archivos de almacenamiento permanente para guardar la información de clientes, películas y alquileres.
Los datos se almacenan en listas en memoria dentro de la clase Videoclub:

python

self.__clientes = []
self.__peliculas = []
self.__alquileres = []
Por este motivo:
La información solo está disponible durante la ejecución del programa.
Los datos se pierden al cerrar el sistema.
Al iniciar nuevamente Main.py, las listas comienzan vacías.
El archivo PDF generado es un reporte, no un mecanismo de persistencia de los datos del sistema.
Control de versiones

El proyecto utiliza Git para registrar los cambios realizados en el código y GitHub para alojar el repositorio y facilitar su administración.
El archivo .gitignore evita incluir elementos que no forman parte del código fuente, como:
El entorno virtual venv/.
Archivos temporales de Python.
La caché de Pytest.
Configuraciones locales del editor.
El archivo generado reporte_videoclub.pdf.