"""Agenda de contactos con persistencia en CSV y JSON."""

# TODO: importa csv y json

CABECERA: list[str] = ["nombre", "telefono"]


def guardar_csv(ruta: str, contactos: list[tuple[str, str]]) -> None:
    """Escribe los contactos en un CSV con la cabecera nombre,telefono."""
    # TODO: usa csv.writer, newline="" y encoding="utf-8"
    raise NotImplementedError


def cargar_csv(ruta: str) -> list[tuple[str, str]]:
    """Lee el CSV. Si el fichero no existe devuelve []."""
    # TODO: sáltate la cabecera y captura FileNotFoundError
    raise NotImplementedError


def guardar_json(ruta: str, datos: dict) -> None:
    """Guarda un diccionario en JSON legible y con tildes."""
    # TODO: json.dump con indent=2 y ensure_ascii=False
    raise NotImplementedError


def cargar_json(ruta: str) -> dict:
    """Lee el JSON. Si no existe devuelve un diccionario vacío."""
    # TODO
    raise NotImplementedError


def linea_tabla(nombre: str, telefono: str) -> str:
    """Fila alineada: nombre a la izquierda en 15, teléfono a la derecha en 12."""
    # TODO
    raise NotImplementedError
