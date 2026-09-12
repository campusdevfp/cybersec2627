"""Tests del verificador de cumplimiento y anonimizador (RA6)."""
import pytest

from cumplimiento import (BASES_LICITUD, PLAZO_MAXIMO_MESES, anonimizar_texto,
                          base_valida, cumple, enmascarar_email,
                          evaluar_tratamiento, seudonimo)


def test_constantes():
    assert PLAZO_MAXIMO_MESES == 60
    assert "consentimiento" in BASES_LICITUD


@pytest.mark.parametrize("base,esperado", [
    ("consentimiento", True), ("contrato", True), ("INTERES_LEGITIMO", True),
    ("porque_si", False), ("", False),
])
def test_base_valida(base, esperado):
    assert base_valida(base) is esperado


def test_tratamiento_correcto():
    t = {"nombre": "Clientes", "base": "contrato",
         "plazo_meses": 24, "datos": ["nombre", "email"]}
    assert evaluar_tratamiento(t) == []
    assert cumple(t) is True


def test_tratamiento_base_invalida():
    t = {"nombre": "X", "base": "porque_si", "plazo_meses": 12, "datos": []}
    problemas = evaluar_tratamiento(t)
    assert any("base de licitud" in p for p in problemas)


def test_tratamiento_plazo_excesivo():
    t = {"nombre": "X", "base": "contrato", "plazo_meses": 120, "datos": []}
    assert any("excesivo" in p for p in evaluar_tratamiento(t))


def test_tratamiento_sin_plazo():
    t = {"nombre": "X", "base": "contrato", "datos": []}
    assert any("plazo" in p for p in evaluar_tratamiento(t))


def test_categoria_especial_sin_consentimiento():
    t = {"nombre": "Fichaje", "base": "contrato", "plazo_meses": 12,
         "datos": ["categoria_especial"]}
    assert any("categoría especial" in p for p in evaluar_tratamiento(t))


def test_categoria_especial_con_consentimiento_ok():
    t = {"nombre": "Fichaje", "base": "consentimiento", "plazo_meses": 12,
         "datos": ["categoria_especial"]}
    assert cumple(t) is True


@pytest.mark.parametrize("email,esperado", [
    ("ana.perez@iesx.es", "a*******z@iesx.es"),
    ("jo@iesx.es", "j*@iesx.es"),
])
def test_enmascarar_email(email, esperado):
    assert enmascarar_email(email) == esperado


def test_enmascarar_email_invalido():
    with pytest.raises(ValueError):
        enmascarar_email("no-es-un-correo")


def test_seudonimo_estable_y_no_reversible():
    a = seudonimo("12345678Z")
    b = seudonimo("12345678z")   # normaliza mayúsculas
    assert a == b
    assert len(a) == 12
    assert a != "12345678Z"


def test_seudonimo_distintos_dni():
    assert seudonimo("12345678Z") != seudonimo("87654321X")


def test_anonimizar_texto():
    texto = "El cliente 12345678Z escribió desde ana.perez@iesx.es ayer."
    limpio = anonimizar_texto(texto)
    assert "[DNI]" in limpio
    assert "[EMAIL]" in limpio
    assert "12345678Z" not in limpio
    assert "ana.perez@iesx.es" not in limpio
