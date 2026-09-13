# Proyecto Detector de fuerza bruta · UD2 (RA2)

Lee un log de autenticación, cuenta los intentos fallidos por IP y señala las IP sospechosas, marcando las que pudieron llegar a autenticarse.

Completa los `TODO` de `src/deteccion.py` hasta que **todos los tests pasen** y `mypy src` diga *Success*.

## Estructura

```
proyecto-ud2/
├── README.md
├── requirements.txt
├── pytest.ini
├── src/deteccion.py      ← tu código
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

1. **Lee** `src/deteccion.py`: cada función tiene un docstring que dice qué debe hacer.
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

## Técnica propia del RA2 (buena práctica que verás en el informe)

El código debe usar **`re`** (expresiones regulares) para analizar el log.
