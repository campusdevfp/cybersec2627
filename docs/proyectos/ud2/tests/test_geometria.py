"""Tests del módulo geometria."""
import math

import pytest

from geometria import area_circulo, area_rectangulo, hipotenusa


@pytest.mark.parametrize("radio,esperado", [
    (1.0, math.pi), (2.0, math.pi * 4), (0.0, 0.0)])
def test_area_circulo(radio, esperado):
    assert area_circulo(radio) == pytest.approx(esperado)


def test_area_circulo_usa_pi_de_math():
    assert area_circulo(1.0) == pytest.approx(math.pi), (
        "Usa math.pi, no una aproximación como 3.14")


@pytest.mark.parametrize("a,b,esperado", [
    (3.0, 4.0, 5.0), (5.0, 12.0, 13.0), (0.0, 0.0, 0.0)])
def test_hipotenusa(a, b, esperado):
    assert hipotenusa(a, b) == pytest.approx(esperado)


@pytest.mark.parametrize("base,altura,esperado", [
    (4.0, 3.0, 12.0), (0.0, 5.0, 0.0)])
def test_area_rectangulo(base, altura, esperado):
    assert area_rectangulo(base, altura) == pytest.approx(esperado)
