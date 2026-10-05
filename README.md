# CMO-313 · Fundamentos de programación — Alumnado

Sitio de **contenidos y ejercicios** del módulo, construido con [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

Contiene la **teoría, los ejemplos y los ejercicios con solución** para trabajar. Este repositorio es la **fuente única del temario**: si hay que corregir o ampliar contenidos, se edita aquí. Los exámenes, bancos de ejercicios y calificaciones están en el repositorio del profesorado.

## Ver el sitio

> Copia y pega **solo las líneas de comando** (las que no empiezan por `#`). En macOS (zsh), pegar una línea con un comentario `#` detrás provoca el error `unexpected extra arguments`.

### Opción A — en local con recarga en vivo (requiere Python)

Crea y activa el entorno (en Windows, la activación es `.venv\Scripts\Activate.ps1`):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Abre `http://127.0.0.1:8000`.

### Opción B — generar el sitio para uso OFFLINE

```bash
mkdocs build
```

Esto genera la carpeta `site/`. Cópiala a cualquier dispositivo y abre `site/index.html` en el navegador. Gracias al plugin *offline*, la búsqueda funciona sin conexión.

> ℹ **Todo funciona sin conexión**, incluidos los diagramas (son SVG propios, no dependen de ningún servicio externo) y la tipografía (se usa la del sistema).

## Exportar el temario a PDF

Con el sitio abierto (`mkdocs serve` o la carpeta `site/`), entra en **«Todo el material (PDF)»** desde el menú: verás todo el temario en una sola página con un botón **Exportar a PDF**.

El botón abre el diálogo de impresión del navegador → elige **Guardar como PDF**. Al imprimir se oculta la navegación y **las soluciones desplegables se abren solas**, así que salen en el papel.

> Activa **Gráficos de fondo** en el diálogo para conservar el color de tablas y recuadros.

## Estructura

```
repo-alumno/
├── mkdocs.yml
├── requirements.txt              # mkdocs-material
├── hooks/pagina_completa.py
└── docs/
    ├── index.md                  # inicio
    ├── ud1/ … ud6/index.md       # las 6 unidades (teoría + ejercicios)
    ├── proyectos/
    │   ├── index.md              # cómo se trabaja un proyecto
    │   ├── ud1/ … ud6/           # los 6 proyectos base con sus tests
    │   └── proyecto-udN.zip      # el mismo proyecto, listo para descargar
    ├── simulacros/
    │   ├── index.md              # qué es un simulacro y cómo usarlo
    │   ├── ra1/ … ra6/           # 6 exámenes de mentira, CON tests
    │   └── simulacro-raN.zip
    ├── recursos/entorno.md       # chuleta de venv / pip / mypy
    ├── assets/diagramas/         # SVG (claro y oscuro)
    └── completo.md               # todo en una página → PDF
```

## Cómo está pensado para estudiar

1. **Lee una sección** y ejecuta sus ejemplos.
2. Haz el bloque **Practica lo de esta sección** que la cierra: 3–4 ejercicios cortos
   con la solución desplegable, que solo usan lo que acabas de leer. **136 en todo el
   módulo.** Hazlos antes de seguir.
3. En clase: dudas, **4 actividades guiadas** y **8 ejercicios largos** por unidad.
4. **Proyecto de la unidad**: estructura real de proyecto Python, con tests que ejecutas tú.
5. **Simulacro**: un examen de mentira con el mismo formato y rúbrica, y con los tests
   publicados.
6. **Examen**: igual que el simulacro, pero **sin tests**.

Este repositorio contiene **solo materiales de estudio**. Los exámenes, las guías docentes
y las calificaciones están en el repositorio del profesorado.

## Publicar en GitHub Pages (opcional)

```bash
mkdocs gh-deploy
```
