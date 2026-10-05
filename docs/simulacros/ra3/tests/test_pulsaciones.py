"""Tests de pulsaciones."""
import pytest

from pulsaciones import media, minima, en_zona, clasificar, a_numero


@pytest.mark.parametrize("args,esperado", [
    (([60.0, 80.0, 100.0],), 80.0),
    (([],), 0.0),
    (([70.0],), 70.0),
    (([72.0, 75.0],), 73.5),
])
def test_media(args, esperado):
    resultado = media(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado


@pytest.mark.parametrize("args,esperado", [
    (([60.0, 80.0],), 60.0),
    (([],), 0.0),
    (([98.0, 55.0, 71.0],), 55.0),
])
def test_minima(args, esperado):
    resultado = minima(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado


@pytest.mark.parametrize("args,esperado", [
    (([55.0, 70.0, 120.0], 60.0, 100.0), 1),
    (([], 60.0, 100.0), 0),
    (([60.0, 100.0], 60.0, 100.0), 2),
    (([59.9, 100.1], 60.0, 100.0), 0),
])
def test_en_zona(args, esperado):
    resultado = en_zona(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado


@pytest.mark.parametrize("args,esperado", [
    ((50.0,), 'Reposo'),
    ((59.9,), 'Reposo'),
    ((60.0,), 'Normal'),
    ((99.9,), 'Normal'),
    ((100.0,), 'Alta'),
    ((180.0,), 'Alta'),
])
def test_clasificar(args, esperado):
    resultado = clasificar(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado


@pytest.mark.parametrize("args,esperado", [
    (('72',), 72.0),
    (('72.5',), 72.5),
    (('hola',), 0.0),
    (('',), 0.0),
])
def test_a_numero(args, esperado):
    resultado = a_numero(*args)
    if isinstance(esperado, float):
        assert resultado == pytest.approx(esperado)
    else:
        assert resultado == esperado
