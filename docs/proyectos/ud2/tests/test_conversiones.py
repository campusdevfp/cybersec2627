"""Tests del módulo conversiones."""
import pytest

from conversiones import celsius_a_fahrenheit, km_a_millas, minutos_a_horas


@pytest.mark.parametrize("km,esperado", [(1.0, 0.621371), (0.0, 0.0), (10.0, 6.21371)])
def test_km_a_millas(km, esperado):
    assert km_a_millas(km) == pytest.approx(esperado)


@pytest.mark.parametrize("c,esperado", [(0.0, 32.0), (100.0, 212.0), (-40.0, -40.0)])
def test_celsius_a_fahrenheit(c, esperado):
    assert celsius_a_fahrenheit(c) == pytest.approx(esperado)


@pytest.mark.parametrize("minutos,esperado", [
    (400, (6, 40)), (60, (1, 0)), (45, (0, 45)), (0, (0, 0))])
def test_minutos_a_horas(minutos, esperado):
    assert minutos_a_horas(minutos) == esperado


def test_minutos_a_horas_devuelve_tupla():
    assert isinstance(minutos_a_horas(90), tuple), (
        "Debe devolver DOS valores: return horas, minutos")
