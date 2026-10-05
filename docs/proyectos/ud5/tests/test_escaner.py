"""Tests del escáner de puertos (RA5).

Solo se prueban las funciones PURAS (sin red). El sondeo real con sockets
(puerto_abierto/escanear) se comprueba manualmente en el laboratorio.
"""
import socket

import pytest

from escaner import (OBJETIVO_POR_DEFECTO, clasificar, es_inseguro, escanear,
                     formatear_informe, servicio_de)


def test_objetivo_por_defecto_es_localhost():
    assert OBJETIVO_POR_DEFECTO == "127.0.0.1"


@pytest.mark.parametrize("puerto,esperado", [
    (22, "SSH"), (443, "HTTPS"), (80, "HTTP"), (9999, "desconocido"),
])
def test_servicio_de(puerto, esperado):
    assert servicio_de(puerto) == esperado


@pytest.mark.parametrize("puerto,esperado", [
    (23, True), (21, True), (3389, True), (22, False), (443, False),
])
def test_es_inseguro(puerto, esperado):
    assert es_inseguro(puerto) is esperado


def test_clasificar():
    r = clasificar([22, 23, 9999, 443])
    assert r == {22: "OK", 23: "INSEGURO", 9999: "REVISAR", 443: "OK"}


def test_clasificar_vacio():
    assert clasificar([]) == {}


def test_formatear_informe():
    assert formatear_informe(22, "OK") == "22/tcp  SSH  OK"
    assert formatear_informe(23, "INSEGURO") == "23/tcp  Telnet  INSEGURO"


def test_escanear_localhost_puerto_cerrado_alto():
    # Un puerto muy alto y raro casi con total seguridad estará cerrado.
    # Comprueba que escanear() devuelve una lista y no rompe con la red real.
    resultado = escanear("127.0.0.1", [59999], timeout=0.2)
    assert isinstance(resultado, list)
    assert 59999 not in resultado


def test_escanear_detecta_puerto_abierto():
    # Abrimos un socket de servidor en un puerto libre y comprobamos que
    # el escáner lo ve como abierto. Es una prueba de integración local.
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(("127.0.0.1", 0))   # 0 = puerto libre que asigna el SO
    servidor.listen(1)
    puerto = servidor.getsockname()[1]
    try:
        abiertos = escanear("127.0.0.1", [puerto], timeout=0.5)
        assert puerto in abiertos
    finally:
        servidor.close()
