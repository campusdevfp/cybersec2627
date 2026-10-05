"""Análisis de notas de un grupo."""

APROBADO: float = 5.0


def media(notas: list[float]) -> float:
    """Media de las notas. Si la lista está vacía devuelve 0.0."""
    # TODO
    raise NotImplementedError


def aprobados(notas: list[float]) -> int:
    """Cuántas notas son mayores o iguales que APROBADO."""
    # TODO: recorre con un bucle y cuenta
    raise NotImplementedError


def mejor(notas: list[float]) -> float:
    """La nota más alta. Si la lista está vacía devuelve 0.0."""
    # TODO
    raise NotImplementedError


def clasificar(nota: float) -> str:
    """Calificación: Sobresaliente >=9, Notable >=7, Bien >=6,
    Suficiente >=5, Insuficiente el resto."""
    # TODO: cuidado con el ORDEN de las condiciones
    raise NotImplementedError


def a_nota(texto: str) -> float:
    """Convierte un texto a nota. Si no se puede, devuelve 0.0."""
    # TODO: usa try / except ValueError
    raise NotImplementedError


def porcentaje_aprobados(notas: list[float]) -> float:
    """Porcentaje de aprobados. Si no hay notas devuelve 0.0."""
    # TODO: cuidado con la división entre cero
    raise NotImplementedError
