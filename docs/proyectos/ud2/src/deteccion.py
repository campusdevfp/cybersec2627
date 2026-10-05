"""Detección de ataques de fuerza bruta a partir de registros de autenticación.

Un ataque de fuerza bruta deja una huella clara en los logs: muchos intentos
fallidos de acceso desde una misma IP en poco tiempo. Este módulo lee los
eventos de un log de autenticación (estilo SSH) y localiza las IP que superan
un umbral de intentos fallidos, que es justo lo que haría un SIEM o una regla
de fail2ban.
"""
from __future__ import annotations

import re
from collections import Counter

# Nº de fallos desde una misma IP a partir del cual se considera fuerza bruta.
UMBRAL: int = 5

# Formato de línea:  <fecha> sshd usuario=<u> ip=<ip> estado=<OK|FALLO>
_PATRON = re.compile(
    r"usuario=(?P<usuario>\S+)\s+ip=(?P<ip>\S+)\s+estado=(?P<estado>OK|FALLO)"
)


def parsear_evento(linea: str) -> dict[str, str] | None:
    """Extrae usuario, ip y estado de una línea de log.

    Devuelve un diccionario con esas tres claves, o None si la línea no
    encaja con el formato esperado.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def parsear_log(texto: str) -> list[dict[str, str]]:
    """Convierte el texto completo de un log en una lista de eventos válidos."""
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def contar_fallos_por_ip(eventos: list[dict[str, str]]) -> dict[str, int]:
    """Cuenta cuántos eventos con estado 'FALLO' tiene cada IP."""
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def ips_sospechosas(eventos: list[dict[str, str]], umbral: int = UMBRAL) -> list[str]:
    """Devuelve las IP con fallos >= umbral, ordenadas de más a menos fallos.

    A igualdad de fallos, se ordenan alfabéticamente para un resultado estable.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def usuarios_objetivo(eventos: list[dict[str, str]], ip: str) -> set[str]:
    """Conjunto de usuarios que una IP concreta ha intentado (con fallo)."""
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def hubo_acceso_correcto(eventos: list[dict[str, str]], ip: str) -> bool:
    """Indica si una IP llegó a autenticarse con éxito alguna vez.

    Un 'FALLO' repetido seguido de un 'OK' desde la misma IP es la señal más
    grave: el ataque de fuerza bruta pudo tener éxito.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def formatear_alerta(ip: str, fallos: int, comprometida: bool) -> str:
    """Línea de alerta del tipo  '10.0.20.5  7 fallos  [POSIBLE ACCESO]'."""
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError
