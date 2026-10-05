"""Tests del módulo estadistica."""
import pytest

from estadistica import cuenta_pares, maximo, media


@pytest.mark.parametrize("numeros,esperado", [
    ([4.0, 8.0, 6.0], 6.0), ([5.0], 5.0), ([1.0, 2.0], 1.5)])
def test_media(numeros, esperado):
    assert media(numeros) == pytest.approx(esperado)


def test_media_de_lista_vacia():
    assert media([]) == 0.0, (
        "Con la lista vacía no se puede dividir: devuelve 0.0 antes de calcular")


@pytest.mark.parametrize("numeros,esperado", [
    ([4.0, 8.0, 6.0], 8.0), ([-3.0, -1.0], -1.0)])
def test_maximo(numeros, esperado):
    assert maximo(numeros) == esperado


def test_maximo_de_lista_vacia():
    assert maximo([]) == 0.0


@pytest.mark.parametrize("numeros,esperado", [
    ([1, 2, 3, 4], 2), ([1, 3, 5], 0), ([], 0), ([0, 2], 2)])
def test_cuenta_pares(numeros, esperado):
    assert cuenta_pares(numeros) == esperado
