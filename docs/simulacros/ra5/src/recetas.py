"""Recetario en CSV y JSON."""
import csv
import json

CABECERA: list[str] = ["nombre", "minutos"]


def guardar_csv(ruta: str, filas: list[tuple[str, int]]) -> None:
    """Guarda las filas en un CSV con cabecera."""
    # TODO: open(..., "w", newline="", encoding="utf-8"), csv.writer,
    #       primero la CABECERA y luego una fila por receta
    raise NotImplementedError


def cargar_csv(ruta: str) -> list[tuple[str, int]]:
    """Lee el CSV; [] si el fichero no existe."""
    # TODO: sáltate la cabecera y convierte la segunda columna a int.
    #       Si el fichero no existe, captura FileNotFoundError y devuelve []
    raise NotImplementedError


def guardar_json(ruta: str, datos: dict) -> None:
    """Guarda un diccionario en JSON legible y con tildes."""
    # TODO: json.dump con indent=2 y ensure_ascii=False
    raise NotImplementedError


def cargar_json(ruta: str) -> dict:
    """Lee el JSON; {} si el fichero no existe."""
    # TODO: json.load; si no existe el fichero, devuelve {}
    raise NotImplementedError


def linea_tabla(nombre: str, minutos: int) -> str:
    """Fila alineada para la consola."""
    # TODO: nombre a la izquierda en 15 huecos, minutos a la derecha en 5
    raise NotImplementedError
