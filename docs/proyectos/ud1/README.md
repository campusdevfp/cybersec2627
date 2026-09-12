# Proyecto Verificador de integridad · UD1 (RA1)

Comprueba si algún fichero ha sido modificado comparando su hash SHA-256 con un manifiesto de referencia. Es la herramienta de la cadena de custodia forense y de la verificación de descargas.

Completa los `TODO` de `src/integridad.py` hasta que **todos los tests pasen** y `mypy src` diga *Success*.

## Estructura

```
proyecto-ud1/
├── README.md
├── requirements.txt
├── pytest.ini
├── src/integridad.py      ← tu código
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

1. **Lee** `src/integridad.py`: cada función tiene un docstring que dice qué debe hacer.
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

## Criterio específico del RA1 (rúbrica, punto 2)

El código debe usar **`hashlib`** para calcular los hashes.
