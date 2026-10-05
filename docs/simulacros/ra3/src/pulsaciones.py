"""Registro de pulsaciones."""


def media(pulsaciones: list[float]) -> float:
    """Media; 0.0 si no hay datos."""
    # TODO: cuidado con la lista vacía
    raise NotImplementedError

def minima(pulsaciones: list[float]) -> float:
    """La más baja; 0.0 si no hay datos."""
    # TODO: min() sobre una lista vacía lanza ValueError
    raise NotImplementedError

def en_zona(pulsaciones: list[float], minimo: float, maximo: float) -> int:
    """Cuántas caen dentro del intervalo, extremos incluidos."""
    # TODO: recorre con un for y ve contando; los extremos SÍ cuentan
    raise NotImplementedError

def clasificar(pulsacion: float) -> str:
    """'Reposo' < 60 · 'Normal' < 100 · 'Alta' el resto."""
    # TODO: encadena los if en orden; el último caso no necesita condición
    raise NotImplementedError

def a_numero(texto: str) -> float:
    """Convierte a número; 0.0 si no se puede."""
    # TODO: try / except ValueError
    raise NotImplementedError
