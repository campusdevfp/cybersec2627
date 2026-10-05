"""Evaluador de reglas de cortafuegos (ACL) con orientación a objetos.

Un cortafuegos aplica una lista ordenada de reglas a cada paquete y actúa
según la PRIMERA que coincide. Si ninguna coincide, se aplica la política por
defecto, que en un diseño seguro es DENEGAR. Aquí modelamos ese motor con
clases: es el corazón de pfSense, iptables/nftables o un grupo de seguridad
en la nube.
"""
from __future__ import annotations


class Regla:
    """Una regla de la ACL.

    Coincide con un paquete si el origen, el destino y el puerto encajan.
    El comodín '*' encaja con cualquier valor; el puerto 0 significa 'cualquiera'.
    """

    def __init__(self, accion: str, origen: str = "*", destino: str = "*",
                 puerto: int = 0) -> None:
        # TODO: implementa esta función (borra el raise)
        raise NotImplementedError

    def _encaja(self, valor: str, patron: str) -> bool:
        # TODO: implementa esta función (borra el raise)
        raise NotImplementedError

    def coincide(self, origen: str, destino: str, puerto: int) -> bool:
        """Indica si esta regla se aplica al paquete dado."""
        # TODO: implementa esta función (borra el raise)
        raise NotImplementedError

    def __str__(self) -> str:
        # TODO: implementa esta función (borra el raise)
        raise NotImplementedError


class Cortafuegos:
    """Motor de reglas con política por defecto (denegar en un diseño seguro)."""

    def __init__(self, politica_por_defecto: str = "DENEGAR") -> None:
        # TODO: implementa esta función (borra el raise)
        raise NotImplementedError

    def agregar(self, regla: Regla) -> None:
        """Añade una regla al final de la lista (menor prioridad)."""
        # TODO: implementa esta función (borra el raise)
        raise NotImplementedError

    def evaluar(self, origen: str, destino: str, puerto: int) -> str:
        """Devuelve 'PERMITIR' o 'DENEGAR' según la PRIMERA regla que coincide.

        Si ninguna regla coincide, aplica la política por defecto.
        """
        # TODO: implementa esta función (borra el raise)
        raise NotImplementedError

    def permitido(self, origen: str, destino: str, puerto: int) -> bool:
        """Versión booleana de evaluar()."""
        # TODO: implementa esta función (borra el raise)
        raise NotImplementedError


def cargar_reglas(texto: str) -> Cortafuegos:
    """Construye un cortafuegos a partir de un texto de reglas.

    Formato de cada línea:  ACCION origen destino puerto
    Ejemplo:                PERMITIR 10.0.20.0/24 10.0.30.10 443
    Se ignoran líneas en blanco y comentarios (#). La primera línea puede ser
    'DEFECTO PERMITIR' o 'DEFECTO DENEGAR' para fijar la política.
    """
    # TODO: implementa esta función (borra el raise)
    raise NotImplementedError
