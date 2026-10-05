"""Verificador de integridad de ficheros mediante funciones hash.

Un manifiesto de integridad asocia a cada fichero su hash SHA-256. Comparando
el hash actual con el del manifiesto se detecta cualquier manipulación: es la
misma idea que usa el análisis forense para probar que una evidencia no se ha
alterado (cadena de custodia) y que usan las distribuciones de software para
que compruebes lo que descargas.

Completa cada TODO y borra el `raise NotImplementedError`.
"""
from __future__ import annotations

import hashlib

# Algoritmo de hash del curso. MD5 y SHA-1 están rotos para integridad:
# usamos SHA-256 (constante en MAYÚSCULAS porque no debe cambiar).
ALGORITMO: str = "sha256"


def hash_de_texto(texto: str) -> str:
    """Devuelve el hash SHA-256 de un texto, en hexadecimal."""
    # TODO: codifica el texto a bytes (utf-8) y usa hashlib.new(ALGORITMO, ...)
    #       devuelve el resultado con .hexdigest()
    raise NotImplementedError


def hash_de_bytes(datos: bytes) -> str:
    """Devuelve el hash SHA-256 de una secuencia de bytes, en hexadecimal."""
    # TODO: como el anterior, pero los datos ya son bytes
    raise NotImplementedError


def coinciden(hash_esperado: str, hash_actual: str) -> bool:
    """Compara dos hashes sin distinguir mayúsculas de minúsculas."""
    # TODO: quita espacios (.strip()), pásalos a minúsculas (.lower()) y compara
    raise NotImplementedError


def parsear_manifiesto(contenido: str) -> dict[str, str]:
    """Convierte un manifiesto de texto en un diccionario {fichero: hash}.

    Formato de cada línea:  <hash><espacios><nombre de fichero>
    Se ignoran las líneas en blanco y las que empiezan por '#'.
    """
    # TODO: recorre las líneas; ignora vacías y comentarios (#);
    #       separa en dos partes con split(maxsplit=1); guarda {nombre: hash}
    raise NotImplementedError


def verificar(manifiesto: dict[str, str],
              hashes_actuales: dict[str, str]) -> dict[str, str]:
    """Compara el manifiesto con los hashes actuales y clasifica cada fichero.

    Estados: 'OK', 'MODIFICADO', 'AUSENTE', 'NUEVO' (ver enunciado).
    """
    # TODO: recorre el manifiesto: si no está en actuales -> AUSENTE;
    #       si coinciden -> OK; si no -> MODIFICADO.
    #       Luego recorre actuales: los que no estén en el manifiesto -> NUEVO.
    raise NotImplementedError


def hay_alteraciones(resultado: dict[str, str]) -> bool:
    """Indica si algún fichero no está en estado 'OK'."""
    # TODO: True si algún estado es distinto de 'OK'
    raise NotImplementedError


def formatear_linea(nombre: str, estado: str) -> str:
    """Devuelve una línea de informe del tipo  '[OK] documento.txt'."""
    # TODO: usa una f-string con el estado entre corchetes
    raise NotImplementedError
