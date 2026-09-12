# Proyecto Riesgo y contraseñas · UD4 (RA4)

Calcula el nivel de riesgo y la pérdida anual esperada (ALE), decide si una salvaguarda es rentable, evalúa contraseñas contra una política y comprueba si un conjunto de factores es MFA real.

Completa los `TODO` de `src/riesgo.py` hasta que **todos los tests pasen** y `mypy src` diga *Success*.

## Estructura

```
proyecto-ud4/
├── README.md
├── requirements.txt
├── pytest.ini
├── src/riesgo.py      ← tu código
└── tests/           ← los tests (no hay que tocarlos)
```

## Puesta en marcha

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

## Cómo trabajar

1. **Lee** `src/riesgo.py`: cada función tiene un docstring que dice qué debe hacer.
2. **Escribe** el código sustituyendo cada `TODO` (y borra el `raise NotImplementedError`).
3. **Ejecuta los tests** y ve arreglando lo que falle:

```bash
pytest        # todos
pytest -x     # para en el primer fallo
mypy src      # comprueba los tipos
```

4. Repite hasta que salga todo en verde.

!!! warning "Los tests son la especificación"
    No los modifiques para que pasen: describen lo que tu código debe hacer, y el examen usará una batería equivalente.

## Criterio específico del RA4 (rúbrica, punto 2)

El código debe **validar entradas** y lanzar/gestionar excepciones donde proceda.
