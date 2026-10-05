"""Tests de dispositivos."""
import pytest

from dispositivos import Dispositivo, Movil, Portatil


@pytest.mark.parametrize("clase,args,esperado", [
    (Dispositivo, ('Router', 89.9), 'Dispositivo Router: 89.90 €'),
    (Movil, ('Pixel', 599.0), 'Movil Pixel: 599.00 €'),
    (Portatil, ('ThinkPad', 1250.5), 'Portatil ThinkPad: 1250.50 €'),
    (Movil, ('Basico', 0.0), 'Movil Basico: 0.00 €'),
])
def test_describir(clase, args, esperado):
    assert clase(*args).describir() == esperado


def test_str_usa_describir():
    obj = Movil("Pixel", 599.0)
    assert str(obj) == obj.describir()


@pytest.mark.parametrize("clase", [Movil, Portatil])
def test_heredan(clase):
    assert issubclass(clase, Dispositivo), (
        f"{clase.__name__} debe declararse como class {clase.__name__}(Dispositivo):")


@pytest.mark.parametrize("clase", [Movil, Portatil])
def test_heredan_el_constructor(clase):
    obj = clase("Pixel", 599.0)
    assert obj.nombre == "Pixel", (
        "Las derivadas no deben repetir __init__: lo heredan")


def test_precio_negativo_al_crear():
    with pytest.raises(ValueError):
        Dispositivo("Roto", -1)


def test_precio_negativo_al_asignar():
    obj = Portatil("ThinkPad", 1250.5)
    with pytest.raises(ValueError):
        obj.precio = -0.01


def test_precio_valido_se_actualiza():
    obj = Portatil("ThinkPad", 1250.5)
    obj.precio = 999.0
    assert obj.precio == 999.0, (
        "El setter debe guardar en self._precio, no en self.precio")


def test_precio_cero_es_valido():
    assert Movil("Basico", 0.0).precio == 0.0, (
        "Cero no es negativo: debe aceptarse")


def test_property_de_verdad():
    assert isinstance(type(Dispositivo("Router", 89.9)).precio, property), (
        "precio debe ser una property, no un atributo normal")
