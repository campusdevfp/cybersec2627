"""Tests del módulo presupuesto."""
import pytest

from presupuesto import (IVA, a_decimal, a_entero, calcular_iva,
                         calcular_subtotal, formatear_importe)


def test_la_constante_iva_vale_21():
    assert IVA == 21


@pytest.mark.parametrize("texto,esperado", [("3", 3), ("0", 0), ("-7", -7)])
def test_a_entero(texto, esperado):
    assert a_entero(texto) == esperado


@pytest.mark.parametrize("texto,esperado", [("10.00", 10.0), ("0.99", 0.99)])
def test_a_decimal(texto, esperado):
    assert a_decimal(texto) == esperado


def test_a_entero_devuelve_un_int():
    assert isinstance(a_entero("5"), int), (
        "a_entero debe devolver un int, no una cadena: usa int(texto)")


@pytest.mark.parametrize("unidades,precio,esperado", [
    (3, 10.0, 30.0), (0, 15.5, 0.0), (1, 0.99, 0.99), (100, 0.01, 1.0)])
def test_calcular_subtotal(unidades, precio, esperado):
    assert calcular_subtotal(unidades, precio) == pytest.approx(esperado)


@pytest.mark.parametrize("subtotal,esperado", [
    (100.0, 21.0), (0.0, 0.0), (30.0, 6.3)])
def test_calcular_iva(subtotal, esperado):
    assert calcular_iva(subtotal) == pytest.approx(esperado)


def test_formatear_importe():
    assert formatear_importe("Subtotal", 30.0) == "Subtotal: 30.00 €", (
        "Deben salir 2 decimales y el símbolo €. Usa f\"{valor:.2f} €\"")


def test_formatear_redondea_a_dos_decimales():
    assert formatear_importe("Total", 1.2) == "Total: 1.20 €"
