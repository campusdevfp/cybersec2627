"""Tests del módulo inventario."""
import sqlite3

import pytest

from inventario import (actualizar_precio, borrar, caros_que, crear_tabla,
                        insertar, listar, precio_medio)


@pytest.fixture()
def bd(tmp_path):
    """Base de datos temporal, nueva para cada test."""
    ruta = str(tmp_path / "inventario.db")
    crear_tabla(ruta)
    return ruta


@pytest.fixture()
def bd_con_datos(bd):
    insertar(bd, "Camisa", 20.0, 10)
    insertar(bd, "Gorra", 8.0, 25)
    insertar(bd, "Abrigo", 50.0, 3)
    return bd


def test_crear_tabla_dos_veces_no_falla(bd):
    crear_tabla(bd)
    assert listar(bd) == []


def test_insertar_y_listar(bd_con_datos):
    assert listar(bd_con_datos) == [
        ("Camisa", 20.0, 10), ("Gorra", 8.0, 25), ("Abrigo", 50.0, 3)]


def test_los_datos_quedan_guardados_en_disco(bd_con_datos):
    con = sqlite3.connect(bd_con_datos)
    filas = con.execute("SELECT COUNT(*) FROM productos").fetchone()[0]
    con.close()
    assert filas == 3, (
        "Los datos no están en el fichero: falta confirmar la transacción "
        "con commit() (o usar 'with sqlite3.connect(...)')")


def test_actualizar_precio(bd_con_datos):
    actualizar_precio(bd_con_datos, "Camisa", 25.0)
    precios = {n: p for n, p, _ in listar(bd_con_datos)}
    assert precios["Camisa"] == 25.0


def test_actualizar_no_afecta_a_los_demas(bd_con_datos):
    actualizar_precio(bd_con_datos, "Camisa", 1.0)
    precios = {n: p for n, p, _ in listar(bd_con_datos)}
    assert precios["Gorra"] == 8.0, (
        "Se han cambiado todos los precios: al UPDATE le falta el WHERE")


def test_borrar(bd_con_datos):
    borrar(bd_con_datos, "Gorra")
    nombres = [n for n, _, _ in listar(bd_con_datos)]
    assert nombres == ["Camisa", "Abrigo"]


def test_borrar_no_vacia_la_tabla(bd_con_datos):
    borrar(bd_con_datos, "Gorra")
    assert len(listar(bd_con_datos)) == 2, (
        "Se ha borrado más de la cuenta: al DELETE le falta el WHERE")


def test_borrar_inexistente_no_hace_nada(bd_con_datos):
    borrar(bd_con_datos, "No existe")
    assert len(listar(bd_con_datos)) == 3


def test_caros_que(bd_con_datos):
    assert caros_que(bd_con_datos, 10.0) == [("Abrigo", 50.0), ("Camisa", 20.0)]


def test_caros_que_es_estricto(bd_con_datos):
    assert ("Camisa", 20.0) not in caros_que(bd_con_datos, 20.0), (
        "Debe ser estrictamente mayor: usa > y no >=")


def test_caros_que_sin_resultados(bd_con_datos):
    assert caros_que(bd_con_datos, 999.0) == []


def test_precio_medio(bd_con_datos):
    assert precio_medio(bd_con_datos) == pytest.approx(26.0)


def test_precio_medio_tabla_vacia(bd):
    assert precio_medio(bd) == 0.0, (
        "AVG() devuelve None cuando la tabla está vacía: contémplalo")
