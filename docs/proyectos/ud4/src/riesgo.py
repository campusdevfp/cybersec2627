"""Análisis de riesgo y verificación de políticas de contraseñas (RA4).

Dos herramientas que un analista usa a diario:
  1. Cálculo del nivel de riesgo (impacto x probabilidad) y de la pérdida
     anual esperada (ALE), base de todo plan de securización.
  2. Verificación de contraseñas contra una política y contra una lista de
     contraseñas comprometidas, como hacen los sistemas de bastionado y MFA.
"""
from __future__ import annotations

# Longitud mínima exigida por la política de contraseñas del curso.
LONGITUD_MINIMA: int = 12

# Umbrales de la matriz de riesgo (valor = impacto x probabilidad, 1..5 c/u).
UMBRAL_MEDIO: int = 7
UMBRAL_ALTO: int = 15


def nivel_riesgo(impacto: int, probabilidad: int) -> str:
    """Clasifica el riesgo en 'BAJO', 'MEDIO' o 'ALTO'.

    impacto y probabilidad van de 1 a 5. Lanza ValueError si se salen del rango.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def calcular_ale(valor_activo: float, factor_exposicion: float,
                 frecuencia_anual: float) -> float:
    """Pérdida anual esperada (ALE).

    ALE = (valor_activo x factor_exposicion) x frecuencia_anual
    factor_exposicion es la fracción del activo que se pierde por incidente
    (0..1). Redondea a 2 decimales.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def salvaguarda_rentable(ale_actual: float, ale_residual: float,
                         coste_anual: float) -> bool:
    """Indica si una salvaguarda se justifica económicamente.

    Es rentable si la reducción de ALE que consigue supera su coste anual.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def evaluar_contrasena(contrasena: str,
                       comprometidas: set[str] | None = None) -> list[str]:
    """Devuelve la lista de problemas de una contraseña (vacía = correcta).

    Comprueba longitud mínima, presencia de minúscula, mayúscula, dígito y
    símbolo, y que no esté en la lista de contraseñas comprometidas.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def contrasena_valida(contrasena: str,
                      comprometidas: set[str] | None = None) -> bool:
    """True si la contraseña cumple toda la política."""
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def es_mfa(factores: list[str]) -> bool:
    """Comprueba si un conjunto de factores constituye MFA real.

    MFA exige >= 2 factores de CATEGORÍAS DISTINTAS: 'conocimiento',
    'posesion' o 'inherencia'. Dos del mismo tipo (p. ej. contraseña + PIN)
    NO son multifactor.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError
