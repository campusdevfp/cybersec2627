"""Tests del módulo vehiculos."""
import pytest

from vehiculos import Coche, Moto, Vehiculo


def test_atributos():
    v = Vehiculo("Seat", 120)
    assert v.marca == "Seat"
    assert v.velocidad == 120


@pytest.mark.parametrize("clase,marca,velocidad,esperado", [
    (Vehiculo, "Seat", 120, "Vehiculo Seat a 120 km/h"),
    (Coche, "Seat", 120, "Coche Seat a 120 km/h"),
    (Coche, "Ford", 0, "Coche Ford a 0 km/h"),
    (Moto, "Honda", 90, "Moto Honda a 90 km/h"),
])
def test_describir(clase, marca, velocidad, esperado):
    assert clase(marca, velocidad).describir() == esperado


def test_str_usa_describir():
    assert str(Coche("Seat", 120)) == "Coche Seat a 120 km/h"


@pytest.mark.parametrize("clase", [Coche, Moto])
def test_heredan_de_vehiculo(clase):
    assert issubclass(clase, Vehiculo), (
        f"{clase.__name__} debe declararse como  class {clase.__name__}(Vehiculo):")


@pytest.mark.parametrize("clase", [Coche, Moto])
def test_las_derivadas_heredan_el_constructor(clase):
    v = clase("X", 50)
    assert v.marca == "X" and v.velocidad == 50, (
        "Las clases derivadas no deben repetir __init__: lo heredan de Vehiculo")


def test_velocidad_negativa_al_crear():
    with pytest.raises(ValueError):
        Vehiculo("Seat", -10)


def test_velocidad_negativa_al_asignar():
    v = Coche("Seat", 120)
    with pytest.raises(ValueError):
        v.velocidad = -1


def test_velocidad_valida_se_actualiza():
    v = Moto("Honda", 90)
    v.velocidad = 110
    assert v.velocidad == 110, (
        "El setter debe guardar en self._velocidad; si asignas a self.velocidad "
        "se llama a sí mismo sin parar")
