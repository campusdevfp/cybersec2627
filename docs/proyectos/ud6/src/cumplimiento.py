"""Verificación de cumplimiento RGPD y anonimización de datos (RA6).

Dos tareas que la normativa impone y que se resuelven con Python:
  1. Comprobar que cada tratamiento de datos tiene una base de licitud válida
     y un plazo de conservación razonable (principios del RGPD).
  2. Seudonimizar/anonimizar datos personales antes de usarlos fuera de su
     finalidad: enmascarar correos y sustituir el DNI por un seudónimo estable.
"""
from __future__ import annotations

import hashlib
import re

# Bases de licitud válidas del artículo 6 del RGPD.
BASES_LICITUD: set[str] = {
    "consentimiento", "contrato", "obligacion_legal",
    "interes_vital", "interes_publico", "interes_legitimo",
}

# Plazo máximo razonable de conservación por defecto (meses).
PLAZO_MAXIMO_MESES: int = 60


def base_valida(base: str) -> bool:
    """Indica si una base de licitud es una de las reconocidas por el RGPD."""
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def evaluar_tratamiento(tratamiento: dict[str, object]) -> list[str]:
    """Devuelve la lista de incumplimientos de un tratamiento (vacía = OK).

    Espera un diccionario con al menos: 'nombre', 'base', 'plazo_meses' y
    'datos' (lista de campos). Comprueba base de licitud, plazo y minimización.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def cumple(tratamiento: dict[str, object]) -> bool:
    """True si el tratamiento no tiene incumplimientos."""
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def enmascarar_email(email: str) -> str:
    """Enmascara un correo: 'ana.perez@iesx.es' -> 'a******z@iesx.es'.

    Deja la primera y la última letra del nombre de usuario y conserva el
    dominio. Si el usuario es muy corto, enmascara todo menos la primera letra.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def seudonimo(dni: str, sal: str = "cmo314") -> str:
    """Sustituye un DNI por un seudónimo estable (hash con sal).

    El mismo DNI produce siempre el mismo seudónimo (permite cruzar registros
    sin exponer el dato), pero no se puede revertir sin la sal. Se devuelven
    los primeros 12 caracteres del hash SHA-256.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def anonimizar_texto(texto: str) -> str:
    """Sustituye DNIs y correos de un texto libre por marcadores.

    Reemplaza cada DNI (8 cifras + letra) por '[DNI]' y cada correo por
    '[EMAIL]'. Útil para limpiar logs o informes antes de compartirlos.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError
