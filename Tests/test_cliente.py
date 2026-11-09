
from modelos.cliente import Cliente


def test_crear_cliente():
    cliente = Cliente(1, "Sergio", "12575987")

    assert cliente.get_id_cliente() == 1
    assert cliente.get_nombre() == "Sergio"
    assert cliente.get_dni() == "12575987"


def test_set_nombre():
    cliente = Cliente(1, "Sergio", "12575987")

    cliente.set_nombre("Pepe")

    assert cliente.get_nombre() == "Pepe"


def test_set_dni():
    cliente = Cliente(1, "Sergio", "12575987")

    cliente.set_dni("98753215")

    assert cliente.get_dni() == "98753215"
