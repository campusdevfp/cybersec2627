# CMO-314 · Ciberseguridad — Alumnado

Materiales de estudio del módulo **Ciberseguridad** (CMO-314, 90 h), con **Python 3** como herramienta principal. Sitio consultable **online y offline**, exportable a PDF.

## Contenido

- **6 unidades** (una por RA) con teoría, actividades, retos y ejercicios con solución: `docs/ud1`…`docs/ud6`.
- **6 proyectos** en Python (plantilla con `TODO` + tests): `docs/proyectos/ud1`…`ud6`.
- **Recursos**: entorno y laboratorio, uso ético y legal, Python para ciberseguridad.

## Ver el sitio

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve            # http://127.0.0.1:8000
mkdocs build            # genera site/ (offline)
```

## Trabajar un proyecto

```bash
cd docs/proyectos/ud1
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest        # al principio falla: completa los TODO de src/
mypy src
```

## Exportar a PDF

Con el sitio levantado, entra en **«Todo el material (PDF)»** y usa el botón **Exportar a PDF** (imprime → guardar como PDF). Los desplegables con soluciones se abren automáticamente al imprimir.

## Uso responsable

Las técnicas y herramientas se usan **solo** sobre tus sistemas o el laboratorio autorizado. Acceder a sistemas ajenos sin permiso es delito. Ver `docs/recursos/uso-etico.md`.
