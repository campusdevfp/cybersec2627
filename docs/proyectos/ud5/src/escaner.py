"""Escáner de puertos TCP para el laboratorio (RA5).

AVISO LEGAL: escanear puertos de sistemas ajenos sin autorización expresa y
por escrito es delito (arts. 197 bis y 264 del Código Penal). Este escáner
está pensado EXCLUSIVAMENTE para las máquinas de tu laboratorio aislado o
para 'localhost'. Por eso el destino por defecto es 127.0.0.1.

El escaneo real se hace con `sockets`, la misma base sobre la que funcionan
herramientas como Nmap. Además del sondeo, el módulo incluye funciones puras
(sin red) para interpretar resultados, que son las que evalúan los tests.
"""
from __future__ import annotations

import socket

# Destino por defecto: SIEMPRE el propio equipo, para no tocar sistemas ajenos.
OBJETIVO_POR_DEFECTO: str = "127.0.0.1"

# Servicios habituales por puerto (para dar contexto al informe).
SERVICIOS: dict[int, str] = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 445: "SMB",
    3306: "MySQL", 3389: "RDP", 8080: "HTTP-alt",
}

# Puertos que no deberían estar abiertos hacia el exterior (texto plano/riesgo).
PUERTOS_INSEGUROS: set[int] = {21, 23, 25, 110, 143, 445, 3389}


def servicio_de(puerto: int) -> str:
    """Nombre del servicio habitual de un puerto, o 'desconocido'."""
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def es_inseguro(puerto: int) -> bool:
    """Indica si un puerto abierto representa un riesgo típico."""
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def clasificar(puertos_abiertos: list[int]) -> dict[int, str]:
    """Asocia a cada puerto abierto una etiqueta de severidad.

    'INSEGURO' si está en la lista de riesgo; 'REVISAR' si es desconocido;
    'OK' en el resto (servicios habituales aceptables).
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def formatear_informe(puerto: int, estado: str) -> str:
    """Línea de informe:  '22/tcp  SSH  OK'."""
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def puerto_abierto(host: str, puerto: int, timeout: float = 0.5) -> bool:
    """Comprueba con un socket TCP si un puerto está abierto.

    Devuelve True si se puede establecer la conexión. Nunca lanza excepción:
    ante cualquier error de red devuelve False. Función con efectos de red,
    por eso no la cubren los tests automáticos (usan las funciones puras).
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError


def escanear(host: str = OBJETIVO_POR_DEFECTO,
             puertos: list[int] | None = None,
             timeout: float = 0.5) -> list[int]:
    """Escanea una lista de puertos de un host y devuelve los abiertos.

    Por seguridad, si no se indican puertos se usan los de SERVICIOS.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError
