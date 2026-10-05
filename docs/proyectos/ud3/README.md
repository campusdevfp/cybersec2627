# Proyecto Gestor de notas · UD3 (RA3)

Analiza las notas de un grupo sin romperse nunca, pase lo que pase.

Practicas condiciones, bucles, acumuladores y control de excepciones.

Completa los `TODO` de `src/` hasta que **todos los tests pasen**.

## Estructura

```
proyecto-ud3/
├── README.md
├── requirements.txt
├── pytest.ini
├── src/          ← tu código
└── tests/        ← los tests (no hay que tocarlos)
```

| Módulo | Sus tests |
|---|---|
| `src/notas.py` | `tests/test_notas.py` |

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

