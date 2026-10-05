"""Museo en SQLite."""
import sqlite3


def crear_tabla(bd: str) -> None:
    """Crea la tabla obras si no existe."""
    # TODO: CREATE TABLE IF NOT EXISTS obras (id, titulo, autor, anio)
    raise NotImplementedError


def insertar(bd: str, titulo: str, autor: str, anio: int) -> None:
    """Añade un registro."""
    # TODO: INSERT con ? para cada valor; NUNCA concatenando texto
    raise NotImplementedError


def listar(bd: str) -> list[tuple]:
    """Devuelve [(titulo, autor, anio), ...]."""
    # TODO: SELECT de las tres columnas y .fetchall()
    raise NotImplementedError


def buscar_por_autor(bd: str, autor: str) -> list[tuple]:
    """Registros cuyo autor coincide exactamente."""
    # TODO: SELECT titulo, anio ... WHERE autor = ?
    raise NotImplementedError


def mayores_que(bd: str, anio: int) -> list[tuple]:
    """Registros con anio estrictamente mayor, ordenados ASC."""
    # TODO: WHERE anio > ?  ...  ORDER BY anio ASC
    raise NotImplementedError


def borrar(bd: str, titulo: str) -> None:
    """Elimina un registro por su titulo."""
    # TODO: DELETE ... WHERE titulo = ?   (sin WHERE se borra TODO)
    raise NotImplementedError
