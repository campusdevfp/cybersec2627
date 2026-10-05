"""Tests del evaluador de cortafuegos (RA3)."""
import pytest

from cortafuegos import Cortafuegos, Regla, cargar_reglas


def test_regla_coincide_exacta():
    r = Regla("PERMITIR", "10.0.20.5", "10.0.30.10", 443)
    assert r.coincide("10.0.20.5", "10.0.30.10", 443) is True
    assert r.coincide("10.0.20.6", "10.0.30.10", 443) is False


def test_regla_comodin_origen_destino():
    r = Regla("PERMITIR", "*", "*", 80)
    assert r.coincide("cualquiera", "otro", 80) is True
    assert r.coincide("cualquiera", "otro", 81) is False


def test_regla_puerto_cero_es_cualquiera():
    r = Regla("DENEGAR", "10.0.20.5", "*", 0)
    assert r.coincide("10.0.20.5", "x", 22) is True
    assert r.coincide("10.0.20.5", "x", 443) is True


def test_regla_accion_invalida():
    with pytest.raises(ValueError):
        Regla("BLOQUEAR")


def test_politica_por_defecto_deniega():
    fw = Cortafuegos()
    assert fw.evaluar("a", "b", 22) == "DENEGAR"


def test_primera_coincidencia_gana():
    fw = Cortafuegos("DENEGAR")
    fw.agregar(Regla("PERMITIR", "10.0.20.5", "*", 443))
    fw.agregar(Regla("DENEGAR", "10.0.20.5", "*", 443))  # nunca se alcanza
    assert fw.evaluar("10.0.20.5", "web", 443) == "PERMITIR"


def test_denegar_explicito_antes_de_permitir_amplio():
    fw = Cortafuegos("DENEGAR")
    fw.agregar(Regla("DENEGAR", "10.0.20.9", "*", 0))
    fw.agregar(Regla("PERMITIR", "*", "*", 443))
    assert fw.evaluar("10.0.20.9", "web", 443) == "DENEGAR"  # gana la 1.ª
    assert fw.evaluar("10.0.20.5", "web", 443) == "PERMITIR"


def test_permitido_booleano():
    fw = Cortafuegos("DENEGAR")
    fw.agregar(Regla("PERMITIR", "*", "*", 443))
    assert fw.permitido("x", "y", 443) is True
    assert fw.permitido("x", "y", 22) is False


def test_cargar_reglas_desde_texto():
    texto = """\
# ACL de ejemplo
DEFECTO DENEGAR
PERMITIR 10.0.20.0/24 10.0.30.10 443
DENEGAR 10.0.20.9 * 0
"""
    fw = cargar_reglas(texto)
    assert fw.politica_por_defecto == "DENEGAR"
    assert len(fw.reglas) == 2
    assert fw.evaluar("10.0.20.0/24", "10.0.30.10", 443) == "PERMITIR"
    assert fw.evaluar("10.0.20.9", "cualquiera", 22) == "DENEGAR"


def test_str_regla():
    assert str(Regla("PERMITIR", "*", "*", 0)) == \
        "PERMITIR origen=* destino=* puerto=*"
