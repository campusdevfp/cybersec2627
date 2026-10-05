"""Catálogo de dispositivos."""


class Dispositivo:
    """Dispositivo con precio validado."""

    def __init__(self, nombre: str, precio: float) -> None:
        # TODO: guarda el nombre y asigna el precio A TRAVÉS de la property
        #       (self.precio = precio), para que se valide también al crear
        raise NotImplementedError

    @property
    def precio(self) -> float:
        """Valor de precio."""
        # TODO: devuelve el atributo interno
        raise NotImplementedError

    @precio.setter
    def precio(self, valor: float) -> None:
        # TODO: si es negativo, lanza ValueError; si no, guárdalo en self._precio
        raise NotImplementedError

    def describir(self) -> str:
        """Descripción."""
        # TODO: 'Dispositivo <nombre>: <precio con 2 decimales> €'
        raise NotImplementedError

    def __str__(self) -> str:
        # TODO: reutiliza describir(), no repitas el formato
        raise NotImplementedError


class Movil(Dispositivo):
    """Teléfono móvil."""

    # TODO: hereda de Dispositivo y sobrescribe SOLO describir()
    #       ('Movil <nombre>: ...'). No repitas __init__: ya lo heredas.


class Portatil(Dispositivo):
    """Ordenador portátil."""

    # TODO: igual que Movil, pero con 'Portatil <nombre>: ...'
