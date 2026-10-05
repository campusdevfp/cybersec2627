"""Tests de recetas."""
import json

import pytest

from recetas import (cargar_csv, cargar_json, guardar_csv, guardar_json,
                     linea_tabla)

DATOS = [('Tortilla', 25), ('Gazpacho', 10)]


def test_csv_ida_y_vuelta(tmp_path):
    ruta = str(tmp_path / "d.csv")
    guardar_csv(ruta, DATOS)
    assert cargar_csv(ruta) == DATOS


def test_csv_cabecera(tmp_path):
    ruta = str(tmp_path / "d.csv")
    guardar_csv(ruta, DATOS)
    assert (tmp_path / "d.csv").read_text(encoding="utf-8").splitlines()[0] == "nombre,minutos"


def test_csv_contenido_exacto(tmp_path):
    ruta = str(tmp_path / "d.csv")
    guardar_csv(ruta, DATOS)
    lineas = [ln for ln in (tmp_path / "d.csv").read_text(encoding="utf-8").splitlines() if ln]
    assert lineas == ['nombre,minutos', 'Tortilla,25', 'Gazpacho,10']


def test_csv_sin_lineas_en_blanco(tmp_path):
    ruta = str(tmp_path / "d.csv")
    guardar_csv(ruta, DATOS)
    assert "\n\n" not in (tmp_path / "d.csv").read_text(encoding="utf-8"), (
        'Aparecen líneas en blanco: abre el CSV con newline=""')


def test_csv_tipo_de_la_segunda_columna(tmp_path):
    ruta = str(tmp_path / "d.csv")
    guardar_csv(ruta, DATOS)
    assert all(isinstance(v, int) for _, v in cargar_csv(ruta)), (
        "Lo leído de un CSV es texto: conviértelo con int()")


def test_csv_vacio(tmp_path):
    ruta = str(tmp_path / "d.csv")
    guardar_csv(ruta, [])
    assert cargar_csv(ruta) == []


def test_csv_inexistente():
    assert cargar_csv("no_existe_jamas.csv") == [], (
        "Captura FileNotFoundError y devuelve []")


def test_linea_tabla():
    assert linea_tabla(*DATOS[0]) == 'Tortilla          25'


def test_json_ida_y_vuelta(tmp_path):
    ruta = str(tmp_path / "d.json")
    datos = {"receta": "Tortilla", "minutos": 25}
    guardar_json(ruta, datos)
    assert cargar_json(ruta) == datos


def test_json_conserva_tildes(tmp_path):
    ruta = str(tmp_path / "d.json")
    guardar_json(ruta, {"nota": "añadir jamón"})
    assert "jamón" in (tmp_path / "d.json").read_text(encoding="utf-8"), (
        "Usa ensure_ascii=False y encoding='utf-8'")


def test_json_es_valido(tmp_path):
    ruta = str(tmp_path / "d.json")
    guardar_json(ruta, {"a": 1})
    assert json.loads((tmp_path / "d.json").read_text(encoding="utf-8")) == {"a": 1}


def test_json_legible(tmp_path):
    ruta = str(tmp_path / "d.json")
    guardar_json(ruta, {"a": 1, "b": 2})
    assert len((tmp_path / "d.json").read_text(encoding="utf-8").splitlines()) > 1, (
        "Falta indent=2: el JSON debe quedar legible")


def test_json_inexistente():
    assert cargar_json("no_existe_jamas.json") == {}
