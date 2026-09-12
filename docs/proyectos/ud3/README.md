# Proyecto Motor de cortafuegos · UD3 (RA3)

Modela una ACL con clases: carga reglas, evalúa cada paquete por primera coincidencia y aplica denegar por defecto.

Completa los `TODO` de `src/cortafuegos.py` hasta que **todos los tests pasen** y `mypy src` diga *Success*.

## Estructura

```
proyecto-ud3/
├── README.md
├── requirements.txt
├── pytest.ini
├── src/cortafuegos.py      ← tu código
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

1. **Lee** `src/cortafuegos.py`: cada función tiene un docstring que dice qué debe hacer.
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

## Criterio específico del RA3 (rúbrica, punto 2)

El código debe definir y usar **clases** (orientación a objetos).
