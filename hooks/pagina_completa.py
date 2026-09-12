"""
Hook de MkDocs: construye la página «Todo el material» concatenando el resto.

La página `completo.md` solo contiene la cabecera y el marcador
<!--CONTENIDO-->. Este hook lo sustituye, al construir el sitio, por el
contenido de todas las páginas indicadas en PAGINAS, corrigiendo las rutas
relativas (imágenes y enlaces) para que sigan funcionando desde la raíz.

Así la página completa nunca se queda desactualizada: se regenera sola.
"""
from __future__ import annotations

import posixpath
import re
from pathlib import Path

# Páginas a incluir, en orden
PAGINAS = [
    ("index.md", None),
    ("el-curso.md", None),
    ("recursos/entorno.md", None),
    ("recursos/uso-etico.md", None),
    ("recursos/python-ciberseguridad.md", None),
    ("ud1/index.md", None),
    ("ud2/index.md", None),
    ("ud3/index.md", None),
    ("ud4/index.md", None),
    ("ud5/index.md", None),
    ("ud6/index.md", None),
    ("proyectos/index.md", None),
    ("retos/index.md", None),
]
_PAGINAS_ORIGINAL = [
    ("index.md", None),
    ("ud1/index.md", None),
    ("ud2/index.md", None),
    ("ud3/index.md", None),
    ("ud4/index.md", None),
    ("ud5/index.md", None),
    ("ud6/index.md", None),
    ("recursos/entorno.md", None),
    ("proyectos/index.md", None),
    ("retos/index.md", None),
]

MARCADOR = "<!--CONTENIDO-->"
PAGINA_DESTINO = "completo.md"


def _reescribe_rutas(texto: str, origen: str) -> str:
    """Convierte las rutas relativas de una página en rutas desde la raíz."""
    carpeta = posixpath.dirname(origen)
    if not carpeta:
        return texto

    def resolver(ruta: str) -> str:
        if ruta.startswith(("http://", "https://", "mailto:", "data:", "#", "/")):
            return ruta
        ancla = ""
        if "#" in ruta:
            ruta, ancla = ruta.split("#", 1)
            ancla = "#" + ancla
        if not ruta:
            return ancla
        return posixpath.normpath(posixpath.join(carpeta, ruta)) + ancla

    # ![alt](ruta)  y  [texto](ruta)
    texto = re.sub(r"(\]\()([^)\s]+)(\))",
                   lambda m: m.group(1) + resolver(m.group(2)) + m.group(3), texto)
    # src="ruta"  en HTML embebido
    texto = re.sub(r'(src=")([^"]+)(")',
                   lambda m: m.group(1) + resolver(m.group(2)) + m.group(3), texto)
    return texto


def _degrada_titulos(texto: str) -> str:
    """Baja un nivel los encabezados para que el h1 de la página sea único."""
    return re.sub(r"^(#{1,5}) ", r"#\1 ", texto, flags=re.M)


def on_page_markdown(markdown: str, page, config, files):  # noqa: ANN001
    if page.file.src_uri != PAGINA_DESTINO or MARCADOR not in markdown:
        return markdown

    docs = Path(config["docs_dir"])
    trozos: list[str] = []
    for origen, titulo in PAGINAS:
        fichero = docs / origen
        if not fichero.exists():
            continue
        texto = fichero.read_text(encoding="utf-8")
        texto = _reescribe_rutas(texto, origen)
        texto = _degrada_titulos(texto)
        if titulo:
            texto = f"## {titulo}\n\n{texto}"
        trozos.append(texto)

    return markdown.replace(MARCADOR, "\n\n<hr class=\"salto\">\n\n".join(trozos))
