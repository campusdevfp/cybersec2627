"""Tests del módulo notas."""
import pytest

from notas import (a_nota, aprobados, clasificar, media, mejor,
                   porcentaje_aprobados)


@pytest.mark.parametrize("notas,esperado", [
    ([5.0, 7.0, 9.0], 7.0), ([4.0], 4.0), ([0.0, 10.0], 5.0)])
def test_media(notas, esperado):
    assert media(notas) == pytest.approx(esperado)


def test_media_sin_notas():
    assert media([]) == 0.0, (
        "Con la lista vacía no se puede dividir: devuelve 0.0 antes de calcular")


@pytest.mark.parametrize("notas,esperado", [
    ([5.0, 4.0, 9.0], 2), ([], 0), ([4.9], 0), ([5.0], 1)])
def test_aprobados(notas, esperado):
    assert aprobados(notas) == esperado


def test_aprobados_incluye_el_cinco_justo():
    assert aprobados([5.0]) == 1, "Un 5 aprueba: la comparación es >=, no >"


@pytest.mark.parametrize("notas,esperado", [
    ([5.0, 9.5, 3.0], 9.5), ([], 0.0), ([2.0], 2.0)])
def test_mejor(notas, esperado):
    assert mejor(notas) == esperado


@pytest.mark.parametrize("nota,esperado", [
    (10.0, "Sobresaliente"), (9.0, "Sobresaliente"), (8.0, "Notable"),
    (7.0, "Notable"), (6.0, "Bien"), (5.0, "Suficiente"),
    (4.9, "Insuficiente"), (0.0, "Insuficiente")])
def test_clasificar(nota, esperado):
    assert clasificar(nota) == esperado


def test_clasificar_respeta_el_orden():
    assert clasificar(10.0) == "Sobresaliente", (
        "Comprueba primero las notas altas: si empiezas por >=5, "
        "un 10 entraría ahí y nunca llegaría a Sobresaliente")


@pytest.mark.parametrize("texto,esperado", [
    ("7.5", 7.5), ("0", 0.0), ("10", 10.0)])
def test_a_nota(texto, esperado):
    assert a_nota(texto) == pytest.approx(esperado)


@pytest.mark.parametrize("texto", ["hola", "", "siete"])
def test_a_nota_con_texto_invalido(texto):
    assert a_nota(texto) == 0.0, (
        "Si el texto no es un número hay que capturar ValueError "
        "con try/except y devolver 0.0")


@pytest.mark.parametrize("notas,esperado", [
    ([5.0, 5.0, 0.0, 0.0], 50.0), ([10.0], 100.0), ([0.0], 0.0)])
def test_porcentaje_aprobados(notas, esperado):
    assert porcentaje_aprobados(notas) == pytest.approx(esperado)


def test_porcentaje_sin_notas():
    assert porcentaje_aprobados([]) == 0.0, (
        "Sin notas habría división entre cero: captúrala o compruébalo antes")
