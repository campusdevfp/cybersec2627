# Proyectos

Cada unidad tiene un **proyecto base**: un pequeño programa con estructura real, ya montado, en el que tú escribes el código y **ejecutas los tests para comprobar que va todo bien**.

No es un ejercicio suelto: es la forma en que se trabaja de verdad — un repositorio con su `src/`, sus `tests/` y su `README`.

| UD | Proyecto | Qué practicas | Tests | Descargar |
|:---:|---|---|:---:|:---:|
| **1** | [Presupuesto de tienda](ud1/README.md) | variables, constantes, operadores, conversión y formato | 16 | [descargar](proyecto-ud1.zip) |
| **2** | [Biblioteca de utilidades](ud2/README.md) | funciones, parámetros, `math` y módulos | 31 | [descargar](proyecto-ud2.zip) |
| **3** | [Gestor de notas](ud3/README.md) | condiciones, bucles y excepciones | 31 | [descargar](proyecto-ud3.zip) |
| **4** | [Flota de vehículos](ud4/README.md) | clases, `property` y herencia | 13 | [descargar](proyecto-ud4.zip) |
| **5** | [Agenda de contactos](ud5/README.md) | ficheros de texto, CSV y JSON | 10 | [descargar](proyecto-ud5.zip) |
| **6** | [Inventario](ud6/README.md) | SQLite y el CRUD completo | 13 | [descargar](proyecto-ud6.zip) |

Descarga el `.zip` de tu unidad, descomprímelo y ábrelo en VS Code.

## Estructura de un proyecto

Todos son iguales, así que solo tienes que aprenderlo una vez:

```
proyecto-udN/
├── README.md          ← qué hay que hacer
├── requirements.txt   ← dependencias
├── pytest.ini         ← configuración (no tocar)
├── src/               ← TU CÓDIGO va aquí
└── tests/             ← los tests (no se tocan)
```

## Cómo se trabaja

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

La primera vez fallará casi todo: es lo normal, aún no has escrito nada. A partir de ahí:

1. **Lee** una función de `src/`: su *docstring* dice qué debe hacer.
2. **Escríbela**, sustituyendo el `TODO` y borrando el `raise NotImplementedError`.
3. **Ejecuta `pytest`** y mira si ese test ya pasa.
4. Repite hasta tenerlo **todo en verde**.

!!! tip "Ve de uno en uno"
    `pytest -x` se detiene en el primer fallo. Arreglas esa función, vuelves a lanzarlo y avanzas. Es mucho más llevadero que pelearse con quince errores a la vez.

## Comandos que usarás

```bash
pytest                      # todos los tests
pytest -q                   # salida resumida
pytest -x                   # para al primer fallo
pytest tests/test_algo.py   # solo un módulo
pytest -k media             # solo los tests cuyo nombre contenga "media"
mypy src                    # comprueba los tipos
```

## Cómo se lee un fallo

```text
FAILED tests/test_notas.py::test_media_sin_notas - ZeroDivisionError
```

Te dice el **fichero**, el **test** y el **motivo**. Y cuando el fallo no es evidente, el propio test incluye una pista:

```text
AssertionError: Con la lista vacía no se puede dividir:
devuelve 0.0 antes de calcular
```

!!! warning "Los tests no se tocan"
    Modificar un test para que pase no arregla nada: el examen usa su propia batería. Los tests son la especificación; tu trabajo es cumplirla.

## Un proyecto está terminado cuando…

```bash
pytest        # todo en verde
mypy src      # Success: no issues found
```

## Cuando lo tengas terminado

El proyecto es para **aprender**: largo y con calma. Para **medirte** está el
**[simulacro de examen](../simulacros/index.md)** de tu RA: mismo formato, tamaño y rúbrica
que la prueba real, con los tests publicados y contrarreloj.

Al terminarlo aplicas la rúbrica y ya sabes qué nota sacarías.
