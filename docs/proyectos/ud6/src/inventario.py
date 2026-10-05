"""Inventario de productos sobre SQLite."""

# TODO: importa sqlite3


def crear_tabla(bd: str) -> None:
    """Crea la tabla productos si no existe.

    Columnas: id INTEGER PRIMARY KEY AUTOINCREMENT,
              nombre TEXT NOT NULL, precio REAL NOT NULL,
              stock INTEGER NOT NULL DEFAULT 0
    """
    # TODO: usa CREATE TABLE IF NOT EXISTS
    raise NotImplementedError


def insertar(bd: str, nombre: str, precio: float, stock: int) -> None:
    """Añade un producto. Recuerda confirmar los cambios."""
    # TODO: INSERT parametrizado con ?
    raise NotImplementedError


def listar(bd: str) -> list[tuple]:
    """Devuelve [(nombre, precio, stock), ...]."""
    # TODO
    raise NotImplementedError


def actualizar_precio(bd: str, nombre: str, precio: float) -> None:
    """Cambia el precio de UN producto."""
    # TODO: no olvides el WHERE
    raise NotImplementedError


def borrar(bd: str, nombre: str) -> None:
    """Elimina UN producto."""
    # TODO: no olvides el WHERE
    raise NotImplementedError


def caros_que(bd: str, precio: float) -> list[tuple]:
    """[(nombre, precio), ...] con precio estrictamente mayor,
    ordenados de mayor a menor."""
    # TODO
    raise NotImplementedError


def precio_medio(bd: str) -> float:
    """Media de precios. Si no hay productos devuelve 0.0."""
    # TODO: AVG devuelve None con la tabla vacía
    raise NotImplementedError
