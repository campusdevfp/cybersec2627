# Proyecto Biblioteca de utilidades · UD2 (RA2)

Un pequeño paquete de funciones reutilizables, repartido en tres módulos.

Practicas definir funciones con parámetros y `return`, usar la librería estándar y organizar el código en módulos.

Completa los `TODO` de `src/` hasta que **todos los tests pasen**.

## Estructura

```
proyecto-ud2/
├── README.md
├── requirements.txt
├── pytest.ini
├── src/          ← tu código
└── tests/        ← los tests (no hay que tocarlos)
```

| Módulo | Sus tests |
|---|---|
| `src/conversiones.py` | `tests/test_conversiones.py` |
| `src/geometria.py` | `tests/test_geometria.py` |
| `src/estadistica.py` | `tests/test_estadistica.py` |

## Puesta en marcha

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

## Cómo trabajar

1. **Lee** el módulo de `src/`: cada función tiene su docstring diciendo qué debe hacer.
2. **Escribe** el código sustituyendo cada `TODO` (y borrando el `raise NotImplementedError`).
3. **Ejecuta los tests** y ve arreglando lo que falle:

```bash
pytest
```

4. Repite hasta que salga todo en verde.

### Comandos útiles

```bash
pytest                       # todos los tests
pytest -q                    # salida resumida
pytest tests/test_X.py       # solo un módulo
pytest -k nombre_del_test    # solo un test
pytest -x                    # para al primer fallo
mypy src                     # comprueba los tipos
```

!!! tip "Empieza por un test"
    Ejecuta `pytest -x` para que se detenga en el primer fallo, arregla esa función y vuelve a
    lanzarlo. Es mucho más llevadero que intentar resolverlo todo de golpe.

