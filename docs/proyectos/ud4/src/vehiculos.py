"""Modelo de vehículos de una flota."""


class Vehiculo:
    """Vehículo genérico con velocidad validada."""

    def __init__(self, marca: str, velocidad: int) -> None:
        # TODO: guarda la marca y usa el property para la velocidad
        raise NotImplementedError

    @property
    def velocidad(self) -> int:
        """Velocidad actual en km/h."""
        # TODO: devuelve el valor interno self._velocidad
        raise NotImplementedError

    @velocidad.setter
    def velocidad(self, valor: int) -> None:
        # TODO: si el valor es negativo lanza ValueError;
        #       si no, guárdalo en self._velocidad
        raise NotImplementedError

    def describir(self) -> str:
        """Devuelve 'Vehiculo Seat a 120 km/h'."""
        # TODO
        raise NotImplementedError

    def __str__(self) -> str:
        return self.describir()


class Coche(Vehiculo):
    """Coche. Hereda de Vehiculo."""

    # TODO: sobrescribe describir() para que devuelva 'Coche Seat a 120 km/h'
    #       NO repitas el __init__: se hereda.


class Moto(Vehiculo):
    """Moto. Hereda de Vehiculo."""

    # TODO: sobrescribe describir() para que devuelva 'Moto Honda a 90 km/h'
