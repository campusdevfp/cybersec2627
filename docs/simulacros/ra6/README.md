# Simulacro RA6 — Museo en SQLite

Un CRUD completo sobre una base de datos SQLite de obras de arte. Practicas creación de tablas, consultas parametrizadas y borrado seguro.

**Duración orientativa:** 50 min · **Entrega:** nada, es un ensayo

!!! tip "Para qué sirve esto"
    Es un **examen de mentira**: mismo formato, misma dificultad y misma rúbrica que el de
    verdad, pero **con los tests publicados**. Hazlo la sesión anterior al examen y llegarás
    con la mecánica rodada.

    El día del examen el proyecto vendrá **sin tests**: solo los docstrings y unos ejemplos.
    Por eso conviene que aquí te acostumbres a leer el docstring *antes* de mirar el test.

## Cómo trabajar

```bash
pip install -r requirements.txt
pytest
```

1. Abre `src/museo.py`. Cada función lleva un **docstring** que dice qué debe hacer: esa es
   la especificación.
2. Escríbela, borra el `raise NotImplementedError` y vuelve a lanzar `pytest`.
3. Termina cuando esté **todo en verde** y `mypy src` diga *Success*.

!!! warning "Entrénate para el examen"
    Intenta resolver cada función **leyendo solo el docstring**. Mira el test únicamente
    cuando falle. Si te acostumbras a programar contra el test, el día del examen te faltará
    esa muleta.

## Qué se valora

Es la rúbrica real del examen, para que sepas dónde se van los puntos. **La nota sale
solo de los casos de prueba**, repartidos por apartados:

`nota del apartado = (casos superados ÷ casos del apartado) × puntos del apartado`

| # | Apartado | Casos | Puntos |
|:---:|---|:---:|:---:|
| **A** | Crear la tabla e insertar | 3 | **3,00** |
| **B** | Consultas | 5 | **5,00** |
| **C** | Borrado | 2 | **2,00** |
| | **TOTAL** | **10** | **10,00** |

El examen de verdad tiene esta misma estructura, con las consultas parametrizadas entre lo que se
comprueba. Aquí tienes 11 casos publicados; en el examen no verás ninguno.

Obligatorio en la entrega, aunque no puntúe por separado: `mypy src` sin errores y cada
función con su docstring.

## Comandos útiles

```bash
pytest -x
pytest -k listar
mypy src
```
