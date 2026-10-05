"""Tests del módulo agenda."""
import json

import pytest

from agenda import (cargar_csv, cargar_json, guardar_csv, guardar_json,
                    linea_tabla)

CONTACTOS = [("Ada", "600111222"), ("Linus", "600333444")]


def test_guardar_csv_escribe_cabecera(tmp_path):
    ruta = str(tmp_path / "c.csv")
    guardar_csv(ruta, CONTACTOS)
    lineas = (tmp_path / "c.csv").read_text(encoding="utf-8").splitlines()
    assert lineas[0] == "nombre,telefono"
    assert lineas[1] == "Ada,600111222"


def test_csv_ida_y_vuelta(tmp_path):
    ruta = str(tmp_path / "c.csv")
    guardar_csv(ruta, CONTACTOS)
    assert cargar_csv(ruta) == CONTACTOS


def test_csv_sin_lineas_en_blanco(tmp_path):
    ruta = str(tmp_path / "c.csv")
    guardar_csv(ruta, CONTACTOS)
    contenido = (tmp_path / "c.csv").read_text(encoding="utf-8")
    assert "\n\n" not in contenido, (
        "Aparecen líneas en blanco entre filas: abre el fichero con newline=\"\"")


def test_csv_vacio(tmp_path):
    ruta = str(tmp_path / "c.csv")
    guardar_csv(ruta, [])
    assert cargar_csv(ruta) == []


def test_csv_inexistente():
    assert cargar_csv("no_existe_jamas.csv") == [], (
        "Si el fichero no existe hay que capturar FileNotFoundError y devolver []")


def test_json_ida_y_vuelta(tmp_path):
    ruta = str(tmp_path / "d.json")
    datos = {"tema": "oscuro", "avisos": True}
    guardar_json(ruta, datos)
    assert cargar_json(ruta) == datos


def test_json_conserva_tildes(tmp_path):
    ruta = str(tmp_path / "d.json")
    guardar_json(ruta, {"saludo": "adiós ñ"})
    crudo = (tmp_path / "d.json").read_text(encoding="utf-8")
    assert "adiós" in crudo, (
        "Las tildes se han escapado: usa ensure_ascii=False y encoding='utf-8'")


def test_json_es_valido(tmp_path):
    ruta = str(tmp_path / "d.json")
    guardar_json(ruta, {"a": 1})
    assert json.loads((tmp_path / "d.json").read_text(encoding="utf-8")) == {"a": 1}


def test_json_inexistente():
    assert cargar_json("no_existe_jamas.json") == {}


def test_linea_tabla():
    assert linea_tabla("Ada", "600111222") == f"{'Ada':<15}{'600111222':>12}"
