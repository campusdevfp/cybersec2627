"""Tests del verificador de integridad (RA1)."""
import pytest

from integridad import (ALGORITMO, coinciden, formatear_linea, hash_de_bytes,
                        hash_de_texto, hay_alteraciones, parsear_manifiesto,
                        verificar)

# SHA-256 conocido de la cadena vacía y de "hola" (valores de referencia)
SHA256_VACIO = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
SHA256_HOLA = "b221d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79"


def test_algoritmo_es_sha256():
    assert ALGORITMO == "sha256"


def test_hash_de_texto_cadena_vacia():
    assert hash_de_texto("") == SHA256_VACIO


def test_hash_de_texto_valor_conocido():
    assert hash_de_texto("hola") == SHA256_HOLA


def test_hash_de_bytes_coincide_con_texto():
    assert hash_de_bytes(b"hola") == hash_de_texto("hola")


def test_hash_es_hexadecimal_de_64_caracteres():
    h = hash_de_texto("cualquier cosa")
    assert len(h) == 64
    assert all(c in "0123456789abcdef" for c in h)


@pytest.mark.parametrize("a,b,esperado", [
    (SHA256_HOLA, SHA256_HOLA, True),
    (SHA256_HOLA.upper(), SHA256_HOLA, True),   # no distingue mayúsculas
    (f"  {SHA256_HOLA}  ", SHA256_HOLA, True),  # ignora espacios
    (SHA256_HOLA, SHA256_VACIO, False),
])
def test_coinciden(a, b, esperado):
    assert coinciden(a, b) is esperado


def test_parsear_manifiesto_basico():
    contenido = (
        f"{SHA256_HOLA}  saludo.txt\n"
        f"{SHA256_VACIO}  vacio.txt\n"
    )
    m = parsear_manifiesto(contenido)
    assert m == {"saludo.txt": SHA256_HOLA, "vacio.txt": SHA256_VACIO}


def test_parsear_manifiesto_ignora_blancos_y_comentarios():
    contenido = (
        "# manifiesto de integridad\n"
        "\n"
        f"{SHA256_HOLA}  saludo.txt\n"
        "   \n"
    )
    m = parsear_manifiesto(contenido)
    assert m == {"saludo.txt": SHA256_HOLA}


def test_parsear_manifiesto_pasa_a_minusculas():
    m = parsear_manifiesto(f"{SHA256_HOLA.upper()}  a.txt")
    assert m["a.txt"] == SHA256_HOLA  # en minúsculas


def test_verificar_ok():
    manifiesto = {"a.txt": SHA256_HOLA}
    actuales = {"a.txt": SHA256_HOLA}
    assert verificar(manifiesto, actuales) == {"a.txt": "OK"}


def test_verificar_modificado():
    manifiesto = {"a.txt": SHA256_HOLA}
    actuales = {"a.txt": SHA256_VACIO}
    assert verificar(manifiesto, actuales) == {"a.txt": "MODIFICADO"}


def test_verificar_ausente_y_nuevo():
    manifiesto = {"a.txt": SHA256_HOLA, "b.txt": SHA256_VACIO}
    actuales = {"a.txt": SHA256_HOLA, "c.txt": SHA256_HOLA}
    r = verificar(manifiesto, actuales)
    assert r["a.txt"] == "OK"
    assert r["b.txt"] == "AUSENTE"
    assert r["c.txt"] == "NUEVO"


def test_hay_alteraciones():
    assert hay_alteraciones({"a": "OK", "b": "OK"}) is False
    assert hay_alteraciones({"a": "OK", "b": "MODIFICADO"}) is True
    assert hay_alteraciones({"a": "NUEVO"}) is True


def test_formatear_linea():
    assert formatear_linea("documento.txt", "OK") == "[OK] documento.txt"
    assert formatear_linea("virus.exe", "NUEVO") == "[NUEVO] virus.exe"
