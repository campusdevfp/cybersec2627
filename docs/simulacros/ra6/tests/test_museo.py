"""Tests de museo."""
import sqlite3

import pytest

from museo import (borrar, buscar_por_autor, crear_tabla, insertar, listar,
                   mayores_que)

DATOS = [('Las Meninas', 'Velazquez', 1656), ('El grito', 'Munch', 1893), ('Guernica', 'Picasso', 1937)]


@pytest.fixture()
def bd(tmp_path):
    ruta = str(tmp_path / "datos.db")
    crear_tabla(ruta)
    return ruta


@pytest.fixture()
def bd_con_datos(bd):
    for fila in DATOS:
        insertar(bd, *fila)
    return bd


def test_insertar_y_listar(bd_con_datos):
    assert listar(bd_con_datos) == [('Las Meninas', 'Velazquez', 1656), ('El grito', 'Munch', 1893), ('Guernica', 'Picasso', 1937)]


def test_buscar_por_autor(bd_con_datos):
    assert buscar_por_autor(bd_con_datos, 'Munch') == [('El grito', 1893)]


def test_buscar_sin_resultado(bd_con_datos):
    assert buscar_por_autor(bd_con_datos, "No existe") == []


def test_mayores_que(bd_con_datos):
    assert mayores_que(bd_con_datos, 0) == [('Las Meninas', 1656), ('El grito', 1893), ('Guernica', 1937)]


def test_mayores_que_es_estricto(bd_con_datos):
    tope = max(f[2] for f in DATOS)
    assert all(v != tope for _, v in mayores_que(bd_con_datos, tope)), (
        "Debe ser estrictamente mayor: usa > y no >=")


def test_mayores_que_sin_resultados(bd_con_datos):
    assert mayores_que(bd_con_datos, 99999) == []


def test_crear_tabla_dos_veces(bd):
    crear_tabla(bd)
    assert listar(bd) == []


def test_datos_guardados_en_disco(bd_con_datos):
    con = sqlite3.connect(bd_con_datos)
    n = con.execute("SELECT COUNT(*) FROM obras").fetchone()[0]
    con.close()
    assert n == len(DATOS), (
        "Los datos no están en el fichero: falta commit() "
        "(o usar 'with sqlite3.connect(...)')")


def test_borrar(bd_con_datos):
    borrar(bd_con_datos, DATOS[0][0])
    assert len(listar(bd_con_datos)) == len(DATOS) - 1, (
        "Se ha borrado más de la cuenta: al DELETE le falta el WHERE")


def test_borrar_inexistente(bd_con_datos):
    borrar(bd_con_datos, "No existe")
    assert len(listar(bd_con_datos)) == len(DATOS)


def test_comillas_no_rompen(bd_con_datos):
    insertar(bd_con_datos, "O'Keeffe: nubes", "O'Keeffe", 1965)
    assert buscar_por_autor(bd_con_datos, "O'Keeffe") == [("O'Keeffe: nubes", 1965)], (
        "Un apóstrofo rompe la consulta si la construyes concatenando texto: usa ?")
