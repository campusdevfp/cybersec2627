"""Tests de análisis de riesgo y políticas de contraseñas (RA4)."""
import pytest

from riesgo import (LONGITUD_MINIMA, calcular_ale, contrasena_valida,
                    es_mfa, evaluar_contrasena, nivel_riesgo,
                    salvaguarda_rentable)


def test_longitud_minima():
    assert LONGITUD_MINIMA == 12


@pytest.mark.parametrize("imp,prob,esperado", [
    (1, 1, "BAJO"), (2, 4, "MEDIO"), (5, 5, "ALTO"),
    (3, 2, "BAJO"),   # 6 < 7
    (4, 2, "MEDIO"),  # 8
    (5, 3, "ALTO"),   # 15
])
def test_nivel_riesgo(imp, prob, esperado):
    assert nivel_riesgo(imp, prob) == esperado


def test_nivel_riesgo_fuera_de_rango():
    with pytest.raises(ValueError):
        nivel_riesgo(0, 3)
    with pytest.raises(ValueError):
        nivel_riesgo(3, 6)


def test_calcular_ale():
    # 40000 * 0.6 = 24000 SLE; * 0.25 = 6000
    assert calcular_ale(40000, 0.6, 0.25) == 6000.0
    assert calcular_ale(30000, 0.4, 0.2) == 2400.0


def test_calcular_ale_factor_invalido():
    with pytest.raises(ValueError):
        calcular_ale(1000, 1.5, 1)


def test_salvaguarda_rentable():
    assert salvaguarda_rentable(6000, 1000, 1400) is True   # ahorra 5000 > 1400
    assert salvaguarda_rentable(6000, 5000, 1400) is False  # ahorra 1000 < 1400


def test_evaluar_contrasena_correcta():
    assert evaluar_contrasena("Caballo-Verde7!") == []


def test_evaluar_contrasena_corta():
    problemas = evaluar_contrasena("Ab1!")
    assert any("12" in p for p in problemas)


def test_evaluar_contrasena_sin_simbolo():
    problemas = evaluar_contrasena("Caballoverde12")
    assert any("símbolo" in p for p in problemas)


def test_evaluar_contrasena_comprometida():
    problemas = evaluar_contrasena("Password1234!",
                                   comprometidas={"Password1234!"})
    assert any("filtradas" in p for p in problemas)


def test_contrasena_valida():
    assert contrasena_valida("Caballo-Verde7!") is True
    assert contrasena_valida("corta") is False


@pytest.mark.parametrize("factores,esperado", [
    (["conocimiento", "posesion"], True),
    (["conocimiento", "inherencia"], True),
    (["conocimiento", "conocimiento"], False),  # dos del mismo tipo
    (["posesion"], False),
    (["conocimiento", "posesion", "inherencia"], True),
])
def test_es_mfa(factores, esperado):
    assert es_mfa(factores) is esperado
