# Entorno de trabajo (chuleta)

Guía rápida para preparar Python de forma profesional. La explicación completa está en la [Unidad 1](../ud1/index.md#2-el-entorno-de-trabajo-ide-entornos-virtuales-y-pip).

## 1. Comprobar Python

```bash
python --version      # p. ej. Python 3.12.3
```

## 2. Entorno virtual (una vez por proyecto)

```bash
python -m venv .venv          # crear
# activar:
source .venv/bin/activate     # macOS / Linux
.venv\Scripts\Activate.ps1    # Windows (PowerShell)
deactivate                    # salir
```

!!! warning "Actívalo antes de instalar"
    Si instalas paquetes sin el entorno activado, se instalan en el sistema y se mezclan entre proyectos.

## 3. pip (paquetes)

```bash
pip install pytest mypy       # instalar
pip list                      # ver instalados
pip uninstall pytest          # desinstalar
```

## 4. requirements.txt (dependencias reproducibles)

```bash
pip freeze > requirements.txt      # guardar versiones
pip install -r requirements.txt    # reinstalar en otro equipo
```

## 5. Comprobar tipos con mypy

```bash
mypy mi_programa.py           # "Success: no issues found" = tipos correctos
```

## 6. Flujo típico de una práctica

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python mi_programa.py         # ejecutar
mypy mi_programa.py           # comprobar tipos
pytest -q                     # pasar los casos de prueba
```
