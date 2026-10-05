"""Tests del detector de fuerza bruta (RA2)."""
import pytest

from deteccion import (UMBRAL, contar_fallos_por_ip, formatear_alerta,
                       hubo_acceso_correcto, ips_sospechosas, parsear_evento,
                       parsear_log, usuarios_objetivo)

LOG = """\
2026-05-01T10:00:00 sshd usuario=root ip=10.0.20.5 estado=FALLO
2026-05-01T10:00:01 sshd usuario=root ip=10.0.20.5 estado=FALLO
2026-05-01T10:00:02 sshd usuario=admin ip=10.0.20.5 estado=FALLO
2026-05-01T10:00:03 sshd usuario=root ip=10.0.20.5 estado=FALLO
2026-05-01T10:00:04 sshd usuario=root ip=10.0.20.5 estado=FALLO
2026-05-01T10:00:05 sshd usuario=root ip=10.0.20.5 estado=OK
2026-05-01T10:01:00 sshd usuario=ana ip=10.0.20.9 estado=OK
2026-05-01T10:02:00 sshd usuario=luis ip=10.0.20.7 estado=FALLO
-- línea de ruido que no encaja --
"""


def test_umbral_por_defecto():
    assert UMBRAL == 5


def test_parsear_evento_valido():
    e = parsear_evento("x sshd usuario=root ip=10.0.20.5 estado=FALLO")
    assert e == {"usuario": "root", "ip": "10.0.20.5", "estado": "FALLO"}


def test_parsear_evento_invalido_devuelve_none():
    assert parsear_evento("basura sin formato") is None


def test_parsear_log_ignora_ruido():
    eventos = parsear_log(LOG)
    assert len(eventos) == 8   # 9 líneas, 1 es ruido


def test_contar_fallos_por_ip():
    eventos = parsear_log(LOG)
    fallos = contar_fallos_por_ip(eventos)
    assert fallos["10.0.20.5"] == 5
    assert fallos["10.0.20.7"] == 1
    assert "10.0.20.9" not in fallos   # solo tuvo OK


def test_ips_sospechosas_por_defecto():
    eventos = parsear_log(LOG)
    assert ips_sospechosas(eventos) == ["10.0.20.5"]


def test_ips_sospechosas_umbral_bajo_ordena():
    eventos = parsear_log(LOG)
    # con umbral 1 entran .5 (5 fallos) y .7 (1 fallo); ordena por nº desc
    assert ips_sospechosas(eventos, umbral=1) == ["10.0.20.5", "10.0.20.7"]


def test_ips_sospechosas_desempate_alfabetico():
    eventos = [
        {"usuario": "a", "ip": "10.0.0.2", "estado": "FALLO"},
        {"usuario": "a", "ip": "10.0.0.1", "estado": "FALLO"},
    ]
    assert ips_sospechosas(eventos, umbral=1) == ["10.0.0.1", "10.0.0.2"]


def test_usuarios_objetivo():
    eventos = parsear_log(LOG)
    assert usuarios_objetivo(eventos, "10.0.20.5") == {"root", "admin"}


def test_hubo_acceso_correcto():
    eventos = parsear_log(LOG)
    assert hubo_acceso_correcto(eventos, "10.0.20.5") is True
    assert hubo_acceso_correcto(eventos, "10.0.20.7") is False


@pytest.mark.parametrize("ip,fallos,comp,esperado", [
    ("10.0.20.5", 7, True, "10.0.20.5  7 fallos  [POSIBLE ACCESO]"),
    ("10.0.20.7", 1, False, "10.0.20.7  1 fallos"),
])
def test_formatear_alerta(ip, fallos, comp, esperado):
    assert formatear_alerta(ip, fallos, comp) == esperado
