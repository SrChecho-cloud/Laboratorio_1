# 🎬 Blockbuster - Sistema de Videoclub

Sistema de gestión de un videoclub desarrollado en **Python** para el trabajo práctico integrador de la materia **Laboratorio I**.

El programa permite registrar clientes, administrar películas, gestionar alquileres y devoluciones, consultar la información disponible y generar reportes en formato PDF.

---

## 📋 Funcionalidades

El sistema cuenta con un menú principal que permite realizar las siguientes operaciones:

| Opción | Funcionalidad | Descripción |
|---|---|---|
| 1 | Registrar cliente | Permite ingresar ID, nombre y DNI. No admite IDs ni DNI duplicados. |
| 2 | Agregar película | Permite registrar una película con ID, título, género y año. |
| 3 | Mostrar clientes | Muestra todos los clientes registrados. |
| 4 | Mostrar catálogo | Muestra las películas y su disponibilidad. |
| 5 | Buscar película | Busca una película utilizando su ID. |
| 6 | Alquilar película | Registra el alquiler de una película disponible a un cliente registrado. |
| 7 | Devolver película | Registra la devolución y vuelve a habilitar la película. |
| 8 | Mostrar alquileres activos | Muestra las películas alquiladas y los clientes asociados. |
| 9 | Generar PDF | Crea un reporte con información del sistema. |
| 0 | Salir | Finaliza la ejecución del programa. |

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python 3 | Lenguaje principal del proyecto. |
| FPDF2 | Generación de reportes PDF. |
| Pytest | Ejecución de pruebas unitarias. |
| Git | Control de versiones. |
| GitHub | Alojamiento del repositorio. |

### Dependencias

Las dependencias y sus versiones se encuentran declaradas en el archivo `requirements.txt`.

Entre ellas se encuentran:

- `fpdf2`: generación de documentos PDF.
- `pytest`: ejecución de pruebas.
- Otras dependencias utilizadas por las bibliotecas instaladas.

---

## 📁 Estructura del proyecto

```text
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
```

### Descripción de los archivos principales

| Archivo o carpeta | Descripción |
|---|---|
| `Main.py` | Contiene el menú principal y la interacción con el usuario. |
| `Modelos/cliente.py` | Define la clase `Cliente`. |
| `Modelos/pelicula.py` | Define la clase `pelicula` y sus datos. |
| `Modelos/operacion.py` | Define la clase abstracta `Operacion`. |
| `Modelos/alquiler.py` | Define la clase `Alquiler`. |
| `Modelos/devolucion.py` | Define la clase `Devolucion`. |
| `Modelos/videoclub.py` | Administra clientes, películas, alquileres y reportes. |
| `Tests/` | Contiene las pruebas unitarias del sistema. |
| `requirements.txt` | Contiene las dependencias del proyecto. |
| `.gitignore` | Indica qué archivos y carpetas se excluyen del control de versiones. |
| `reporte_videoclub.pdf` | Ejemplo de reporte generado por el sistema. |

---

## 🧩 Programación orientada a objetos

El proyecto utiliza los principales conceptos de la programación orientada a objetos.

### Encapsulamiento

Los atributos de las clases se definen como privados utilizando doble guion bajo (`__`). Para acceder o modificar estos datos se utilizan métodos públicos, como getters y setters.

Por ejemplo, en la clase `Cliente`:

```python
class Cliente:
    def __init__(self, id_cliente, nombre, dni):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__dni = dni
```

También se aplica en `Videoclub`, donde las listas de clientes, películas y alquileres son privadas.

### Herencia

Las clases `Alquiler` y `Devolucion` heredan de la clase `Operacion`.

```python
class Alquiler(Operacion):
    pass
```

```python
class Devolucion(Operacion):
    pass
```

De esta manera, ambas reutilizan los atributos y métodos definidos en su clase base.

### Abstracción

La clase `Operacion` es abstracta y utiliza `ABC` y `abstractmethod`.

```python
from abc import ABC, abstractmethod

class Operacion(ABC):

    @abstractmethod
    def ejecutar(self, videoclub):
        pass
```

Esto establece que las clases que heredan de `Operacion` deben implementar el método `ejecutar()`.

### Polimorfismo

Las clases `Alquiler` y `Devolucion` implementan el método `ejecutar()` de distintas maneras.

```python
def ejecutar(self, videoclub):
    return videoclub.registrar_alquiler(self)
```

En `Devolucion`, el mismo método llama a otra operación:

```python
def ejecutar(self, videoclub):
    return videoclub.registrar_devolucion(self)
```

Aunque utilizan el mismo nombre de método, cada clase realiza una acción diferente.

---

## ⚙️ Instalación y configuración

### Requisitos

Para ejecutar el proyecto se necesita:

- Python 3.
- Git.
- PowerShell en Windows.

### 1. Clonar el repositorio

Desde PowerShell, ejecutar:

```powershell
git clone https://github.com/SrChecho-cloud/Laboratorio_1.git
cd Laboratorio_1
```

### 2. Crear el entorno virtual

```powershell
py -m venv venv
```

### 3. Activar el entorno virtual

```powershell
.\venv\Scripts\Activate.ps1
```

Si PowerShell impide ejecutar el script de activación, se puede habilitar para el usuario actual con:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Después, volver a ejecutar el comando de activación.

### 4. Instalar las dependencias

Con el entorno virtual activado:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶️ Ejecución del programa

Desde la carpeta principal del proyecto y con el entorno virtual activado, ejecutar:

```powershell
py Main.py
```

También se puede utilizar:

```powershell
python Main.py
```

Al iniciar, se mostrará el menú principal del videoclub en la consola.

**Nota sobre los nombres de las carpetas:** el proyecto utiliza la carpeta `Modelos` con mayúscula, mientras que los imports del código están escritos como `modelos` en minúscula. Esto funciona en Windows, pero puede generar problemas en sistemas Linux, que distinguen entre mayúsculas y minúsculas.

---

## 🧪 Pruebas unitarias

El proyecto utiliza **Pytest** para comprobar el funcionamiento de las clases y métodos.

Las pruebas se encuentran en la carpeta `Tests/`:

- `test_cliente.py`
- `test_pelicula.py`
- `test_operacion.py`
- `test_alquiler.py`
- `test_devolucion.py`
- `test_videoclub.py`

Para ejecutar todas las pruebas desde PowerShell:

```powershell
py -m pytest -v
```

Las pruebas verifican, entre otros aspectos:

- Creación de clientes y películas.
- Funcionamiento de getters y setters.
- Validación de IDs y DNI duplicados.
- Búsqueda de clientes y películas.
- Registro de alquileres y devoluciones.
- Control de disponibilidad de películas.
- Comportamiento de la clase abstracta `Operacion`.
- Generación del reporte PDF.

**Resultado de las pruebas realizadas:** 32 pruebas aprobadas.

---

## 📄 Generación de PDF

El sistema permite generar un reporte seleccionando la opción **9. Generar PDF** del menú principal.

La generación se realiza mediante el método `generar_pdf()` de la clase `Videoclub`, utilizando la biblioteca FPDF2.

El archivo generado se llama:

```text
reporte_videoclub.pdf
```

El reporte contiene:

- Nombre del sistema: BLOCKBUSTER.
- Fecha y hora de generación.
- Sistema operativo utilizado.
- Cantidad de clientes registrados.
- Catálogo completo de películas.
- ID, título, género, año y disponibilidad de cada película.
- Listado de alquileres activos.
- Nombre del cliente y fecha del alquiler.

El archivo se genera en la carpeta desde la que se ejecuta el programa.

---

## 💾 Almacenamiento de datos

El sistema no utiliza una base de datos ni almacenamiento permanente para guardar la información.

Los clientes, películas y alquileres se almacenan en listas en memoria dentro de la clase `Videoclub`.

Por este motivo:

- La información está disponible mientras el programa se encuentra en ejecución.
- Los datos se pierden al cerrar el sistema.
- Al iniciar nuevamente el programa, las listas comienzan vacías.
- El PDF generado funciona como un reporte y no como un mecanismo para recuperar los datos.

---

## 🌐 Control de versiones

El proyecto utiliza **Git** para registrar los cambios realizados durante el desarrollo y **GitHub** para alojar el repositorio.

Se utiliza un archivo `.gitignore` para excluir elementos que no forman parte del código fuente, como:

- El entorno virtual `venv/`.
- Archivos temporales de Python.
- Caché de Pytest.
- Configuraciones locales del editor.
- Archivos PDF generados que no se quieran incorporar al repositorio.

Repositorio: [Laboratorio_1 - GitHub](https://github.com/SrChecho-cloud/Laboratorio_1)

---

**Trabajo práctico integrador final - Laboratorio I**