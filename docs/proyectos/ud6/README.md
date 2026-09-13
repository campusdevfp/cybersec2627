# Proyecto Cumplimiento y anonimización · UD6 (RA6)

Verifica que cada tratamiento de datos cumple el RGPD (base de licitud, plazo, minimización) y anonimiza datos personales (enmascara correos, seudonimiza DNIs, limpia textos).

Completa los `TODO` de `src/cumplimiento.py` hasta que **todos los tests pasen** y `mypy src` diga *Success*.

## Estructura

```
proyecto-ud6/
├── README.md
├── requirements.txt
├── pytest.ini
├── src/cumplimiento.py      ← tu código
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

1. **Lee** `src/cumplimiento.py`: cada función tiene un docstring que dice qué debe hacer.
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

## Técnica propia del RA6 (buena práctica que verás en el informe)

El código no debe dejar datos personales en claro: usa **`hashlib`** y **`re`**.
