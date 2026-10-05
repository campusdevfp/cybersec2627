# Unidad 6 · Bases de datos relacionales

> **Módulo:** CMO-313 · Fundamentos de programación
> **Resultado de aprendizaje:** RA6 · **Duración:** 8 h · **Peso:** 10 %
> **Lenguaje:** Python 3 (tipado) + SQLite

En la UD5 guardaste datos en ficheros. Funciona para poca información, pero cuando hay miles de registros y hace falta buscarlos, ordenarlos o modificarlos, el fichero se queda corto. La solución es una **base de datos**.

Es el segundo RA de más peso (20 %) y la puerta de entrada a los módulos de bases de datos del ciclo.

---

## Mapa de la unidad

<figure markdown>
  ![Mapa de la unidad 6](../assets/diagramas/ud6-mapa.svg#only-light)
  ![Mapa de la unidad 6](../assets/diagramas/ud6-mapa-dark.svg#only-dark)
  <figcaption>Tu programa habla con la base de datos mediante sqlite3 y sentencias SQL.</figcaption>
</figure>

### Qué vas a saber hacer al terminar

- [ ] Explicar qué aporta una base de datos frente a un fichero.
- [ ] Conectarte a **SQLite** desde Python con `sqlite3`.
- [ ] Crear tablas con `CREATE TABLE`.
- [ ] Hacer las cuatro operaciones **CRUD**: insertar, consultar, modificar y borrar.
- [ ] Usar **consultas parametrizadas** y entender por qué son obligatorias.
- [ ] Filtrar y ordenar con `WHERE` y `ORDER BY`.
- [ ] Confirmar cambios con `commit()` y cerrar bien la conexión.

---

!!! tip "Cómo se trabaja esta unidad"
    Cada sección de teoría termina con **Practica lo de esta sección**: tres o cuatro
    ejercicios cortos con la solución desplegable, que solo usan lo que acabas de leer.

    **Hazlos en el momento, antes de seguir.** Ese es el trato: la teoría la lees tú
    —en casa o en clase— y el tiempo de aula se dedica a resolver dudas y a lo que de
    verdad cuesta. Si llegas a la siguiente sección sin haber tocado el teclado, la
    unidad se te va a hacer cuesta arriba.

    Después vienen las **actividades guiadas**, el **proyecto** de la unidad y el
    **simulacro** de examen. En ese orden.

---

## 1. Por qué una base de datos

Con un CSV de 50 000 productos, buscar uno obliga a leer el fichero entero; y si dos personas escriben a la vez, los datos se corrompen.

Un **SGBD** (Sistema Gestor de Bases de Datos) resuelve eso:

| Ventaja | Qué significa |
|---|---|
| **Búsquedas rápidas** | encuentra un registro entre millones sin leerlo todo |
| **Integridad** | impide datos inválidos o duplicados |
| **Concurrencia** | varios programas a la vez sin corromper nada |
| **Consultas potentes** | filtrar, ordenar y agrupar con una sola instrucción |

En una base de datos **relacional**, los datos se organizan en **tablas**: cada fila es un registro y cada columna un campo.

**Usaremos SQLite**: viene incluido en Python, guarda todo en un único fichero `.db` y no necesita instalar ningún servidor. Es el mismo motor que llevan dentro tu móvil y tu navegador.

---

> **Reto rápido 1.** Escribe en SQL, sin ejecutarlo, la consulta que devuelve el nombre de los productos que cuestan más de 20 €. *(Solución: `SELECT nombre FROM productos WHERE precio > 20;`)*

## 2. Conectarse desde Python

```python
import sqlite3

conexion = sqlite3.connect("inventario.db")   # crea el fichero si no existe
cursor = conexion.cursor()                    # el que ejecuta las sentencias

# ... operaciones ...

conexion.commit()                             # confirma los cambios
conexion.close()                              # cierra
```

| Pieza | Para qué sirve |
|---|---|
| `connect()` | abre (o crea) la base de datos |
| `cursor()` | objeto con el que se ejecutan las sentencias SQL |
| `commit()` | **confirma** los cambios: sin esto no se guardan |
| `close()` | cierra la conexión |

!!! danger "Sin `commit()` no se guarda nada"
    Es el error más frecuente de esta unidad: el programa parece funcionar, no da ningún error… y al volver a abrir la base de datos está vacía. **Después de insertar, modificar o borrar, hay que llamar a `commit()`.**

### 2.1 Mejor con `with`

Igual que con los ficheros, `with` se encarga del cierre:

```python
import sqlite3

with sqlite3.connect("inventario.db") as conexion:
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)",
                   ("Camisa", 19.99))
    # el commit lo hace with al salir sin errores
```

> **Reto rápido 1.** ¿Qué pasa si ejecutas un `INSERT` y cierras el programa sin `commit()`? *(No se guarda nada.)*

## 3. Crear la tabla

```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock  INTEGER NOT NULL DEFAULT 0
    )
""")
```

| Elemento | Qué significa |
|---|---|
| `IF NOT EXISTS` | no falla si la tabla ya existe (imprescindible) |
| `INTEGER PRIMARY KEY AUTOINCREMENT` | identificador único que se genera solo |
| `NOT NULL` | el campo es obligatorio |
| `DEFAULT 0` | valor por defecto si no se indica |

Tipos de SQLite: `INTEGER`, `REAL` (decimales), `TEXT` y `BLOB`.

---

> **Reto rápido 3.** Escribe el `CREATE TABLE` de una tabla `clientes` con id autonumérico, nombre obligatorio y email.

## 4. CRUD: las cuatro operaciones

**CRUD** = *Create, Read, Update, Delete*. Con esas cuatro se hace todo.

### 4.1 Create — `INSERT`

```python
cursor.execute(
    "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
    ("Camisa", 19.99, 10)
)
conexion.commit()
```

Varios de golpe:

```python
productos = [("Gorra", 8.0, 25), ("Pantalón", 34.5, 7)]
cursor.executemany(
    "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
    productos
)
conexion.commit()
```

### 4.2 Read — `SELECT`

```python
cursor.execute("SELECT id, nombre, precio FROM productos")

filas = cursor.fetchall()        # todas, como lista de tuplas
for id_, nombre, precio in filas:
    print(f"{id_:>3} {nombre:<12} {precio:>8.2f} €")
```

| Método | Devuelve |
|---|---|
| `fetchall()` | todas las filas (lista de tuplas) |
| `fetchone()` | la siguiente fila, o `None` si no hay |
| `fetchmany(n)` | como mucho `n` filas |

### 4.3 Update — `UPDATE`

```python
cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (24.99, 1))
conexion.commit()
```

!!! danger "`UPDATE` sin `WHERE` cambia TODAS las filas"
    `UPDATE productos SET precio = 0` pone a cero el precio de todo el inventario. Igual con `DELETE FROM productos`, que lo borra entero. **El `WHERE` no es opcional en la práctica.**

### 4.4 Delete — `DELETE`

```python
cursor.execute("DELETE FROM productos WHERE id = ?", (3,))
conexion.commit()
```

> Ojo a la coma en `(3,)`: sin ella no es una tupla, y `execute` la necesita.

---

> **Reto rápido 4.** ¿Qué pasa si ejecutas `DELETE FROM clientes` sin `WHERE`? *(Solución: borra **todas** las filas, y no hay deshacer.)*

## 5. Consultas parametrizadas (obligatorio)

Fíjate en que **nunca** hemos metido los valores dentro del texto SQL. Siempre `?` y una tupla aparte. Esta es la razón:

```python
nombre = input("Buscar: ")

# ✗ MAL: concatenando
cursor.execute("SELECT * FROM productos WHERE nombre = '" + nombre + "'")

# ✓ BIEN: parametrizada
cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
```

Con la primera forma, si el usuario escribe `'; DROP TABLE productos; --` la base de datos **ejecuta ese comando** y se pierde la tabla. Es la **inyección SQL**, una de las vulnerabilidades más explotadas de la historia.

!!! success "La regla, sin excepciones"
    Los datos van **siempre** con `?` y una tupla. Nunca se concatenan ni se interpolan en la cadena SQL. En el examen esto se comprueba.

> **Reto rápido 2.** Reescribe de forma segura: `cursor.execute(f"SELECT * FROM productos WHERE precio > {p}")`.
> *(Solución: `cursor.execute("SELECT * FROM productos WHERE precio > ?", (p,))`.)*

## 6. Filtrar y ordenar

```python
# filtrar
cursor.execute("SELECT nombre FROM productos WHERE precio > ?", (20,))

# ordenar
cursor.execute("SELECT nombre, precio FROM productos ORDER BY precio DESC")

# combinar y limitar
cursor.execute("""
    SELECT nombre, precio FROM productos
    WHERE stock > ?
    ORDER BY precio ASC
    LIMIT 5
""", (0,))
```

| Cláusula | Qué hace |
|---|---|
| `WHERE` | filtra las filas |
| `ORDER BY campo ASC / DESC` | ordena ascendente / descendente |
| `LIMIT n` | como mucho n resultados |
| `LIKE '%algo%'` | búsqueda por texto parcial |

Búsqueda parcial parametrizada:

```python
texto = "cam"
cursor.execute("SELECT nombre FROM productos WHERE nombre LIKE ?", (f"%{texto}%",))
```

Funciones de agregado:

```python
cursor.execute("SELECT COUNT(*), AVG(precio), MAX(precio) FROM productos")
total, media, maximo = cursor.fetchone()
```

---

> **Reto rápido 6.** Añade a un `SELECT` la cláusula que ordena de mayor a menor por precio. *(Solución: `ORDER BY precio DESC`.)*

## 7. Estructura de una aplicación con BD

Conviene separar el acceso a datos de la interfaz:

```python
import sqlite3

BD = "inventario.db"


def crear_tabla() -> None:
    """Crea la tabla si no existe."""
    with sqlite3.connect(BD) as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                stock  INTEGER NOT NULL DEFAULT 0
            )
        """)


def insertar(nombre: str, precio: float, stock: int) -> None:
    """Añade un producto."""
    with sqlite3.connect(BD) as con:
        con.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
            (nombre, precio, stock),
        )


def listar() -> list[tuple]:
    """Devuelve todos los productos."""
    with sqlite3.connect(BD) as con:
        return con.execute(
            "SELECT id, nombre, precio, stock FROM productos"
        ).fetchall()


def main() -> None:
    crear_tabla()
    insertar("Camisa", 19.99, 10)
    for fila in listar():
        print(fila)


if __name__ == "__main__":
    main()
```

Cada función hace **una** operación y **devuelve** datos; solo `main` imprime. Igual que en la UD2, esto es lo que permite probarlo automáticamente.

---

> **Reto rápido 7.** ¿Por qué `listar(bd)` devuelve las filas en vez de imprimirlas? *(Solución: para poder probarla con un test y reutilizarla.)*

## 8. Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| Los datos no se guardan | falta `commit()` | llámalo tras insertar/modificar/borrar |
| `no such table` | no creaste la tabla | `CREATE TABLE IF NOT EXISTS` al arrancar |
| `no such column` | nombre de columna mal escrito | revisa el `CREATE TABLE` |
| `Incorrect number of bindings` | los `?` no coinciden con la tupla | cuenta ambos |
| Se cambiaron todas las filas | `UPDATE`/`DELETE` sin `WHERE` | añade siempre el `WHERE` |
| `(3)` no funciona como parámetro | no es una tupla | escribe `(3,)` |
| `database is locked` | conexión sin cerrar | usa `with` |
| Inyección SQL | concatenaste la entrada del usuario | usa `?` siempre |

---

---

## 9. Ejercicios

Aquí están **todos los ejercicios de la unidad**, agrupados por el
tema al que corresponden y con la solución desplegable.

**Haz los de un tema en cuanto termines de leerlo.** No esperes al final: son cortos y solo
usan lo que acabas de ver, así que si algo no ha quedado claro lo descubres en el momento y
no tres semanas después.

!!! warning "Intenta antes de desplegar"
    Abrir la solución sin haberlo intentado da sensación de aprender, y no enseña nada. Si
    llevas quince minutos sin avanzar, mírala. Si llevas dos, no.


### Tema 1 · Por qué una base de datos

**1.1.** Tienes las notas de 60 alumnos guardadas en un CSV. Da **tres razones** por las que una base de datos lo haría mejor.
<details><summary>Solución</summary>

```text
1. BUSCAR. En el CSV hay que leerlo entero y recorrerlo a mano.
   En SQL:  SELECT * FROM alumnos WHERE nota >= 5   -> y ya esta.

2. INTEGRIDAD. El CSV admite cualquier cosa: una nota "hola", un campo vacio,
   dos alumnos con el mismo id. La tabla define tipos y restricciones
   (NOT NULL, PRIMARY KEY) y rechaza lo que no cuadra.

3. VARIOS A LA VEZ. Si dos programas escriben el CSV a la vez, se pisan y se
   pierden datos. La base de datos gestiona los accesos simultaneos.

Extra: relacionar tablas (alumnos + matriculas + modulos) es trivial en SQL
y un infierno a mano.
```
</details>

**1.2.** ¿Qué es una **tabla**, una **fila** y una **columna**? Ponlo en paralelo con algo que ya conoces.
<details><summary>Solución</summary>

```text
Tabla   -> el conjunto de datos del mismo tipo. Como un fichero CSV entero,
           o como una lista de objetos de una misma clase.
Fila     -> un registro concreto: UN alumno, UN libro. Como un objeto.
Columna  -> un campo con su tipo: nombre TEXT, nota REAL. Como un atributo.

Alumno(nombre, nota)  <->  tabla alumnos (nombre TEXT, nota REAL)
ada = Alumno(...)     <->  una fila
```
</details>

**1.3.** Traduce a SQL, sin ejecutar: «quiero el título y el año de los libros de Borges».
<details><summary>Solución</summary>

```text
SELECT titulo, anio          <- que columnas quiero
FROM   libros                <- de que tabla
WHERE  autor = 'Borges';     <- que filas

Las tres palabras clave, siempre en ese orden. Si te acostumbras a leerlas
asi -"que columnas, de donde, con que condicion"- el SQL deja de dar miedo.
```
</details>


### Tema 2 · Conectarse desde Python

**2.1.** Conéctate a una base de datos `prueba.db` y comprueba que el fichero se crea.
<details><summary>Solución</summary>

```python
import os
import sqlite3

with sqlite3.connect("prueba.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER)")

print(os.path.exists("prueba.db"))   # -> True

# SQLite no necesita servidor: la base de datos ES un fichero.
```
</details>

**2.2.** ¿Qué hace `with sqlite3.connect(...)` que no hace `sqlite3.connect(...)` a secas?
<details><summary>Solución</summary>

```text
El with hace COMMIT automatico al salir del bloque si todo ha ido bien
(y ROLLBACK si salta una excepcion).

Sin with, esto NO guarda nada:

    con = sqlite3.connect("bd.db")
    con.execute("INSERT INTO ...")
    # falta con.commit()  ->  al cerrar el programa, los datos se pierden

Es el error numero uno de la unidad: "el programa funciona pero la tabla
esta vacia". Casi siempre es un commit() que falta.
```
</details>

**2.3.** Crea una tabla, inserta una fila y comprueba con `fetchall()` que está.
<details><summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect("demo.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS alumnos (nombre TEXT, nota REAL)")
    con.execute("INSERT INTO alumnos (nombre, nota) VALUES (?, ?)", ("Ada", 9.5))

with sqlite3.connect("demo.db") as con:
    print(con.execute("SELECT nombre, nota FROM alumnos").fetchall())
    # -> [('Ada', 9.5)]
```
</details>


### Tema 3 · Crear la tabla

**3.1.** Crea la tabla `productos` con `id` autonumérico, `nombre` obligatorio y `precio`.
<details><summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect("tienda.db") as con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
    """)

print("tabla creada")   # -> tabla creada
```
</details>

**3.2.** ¿Por qué `IF NOT EXISTS`? Ejecuta la creación dos veces y compruébalo.
<details><summary>Solución</summary>

```python
import sqlite3


def crear(bd: str) -> None:
    """Crea la tabla si no está."""
    with sqlite3.connect(bd) as con:
        con.execute("CREATE TABLE IF NOT EXISTS t (id INTEGER)")


crear("dos.db")
crear("dos.db")   # sin IF NOT EXISTS, esta segunda llamada lanzaría
                  # OperationalError: table t already exists

print("dos veces sin error")   # -> dos veces sin error
```
</details>

**3.3.** Elige el tipo adecuado para: nombre de un cliente, número de unidades, precio, si está activo.
<details><summary>Solución</summary>

```text
nombre    -> TEXT
unidades  -> INTEGER
precio    -> REAL      (nunca TEXT: no se podria ordenar ni sumar)
activo    -> INTEGER   (SQLite no tiene BOOLEAN: se usa 0 / 1)

Y casi siempre:  id INTEGER PRIMARY KEY AUTOINCREMENT
para tener una clave unica sin pensar en ella.
```
</details>


### Tema 4 · CRUD

**4.1.** Inserta tres productos y recupéralos todos (Create + Read).
<details><summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect("crud.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT, precio REAL)")
    for fila in [("Camisa", 19.9), ("Gorra", 7.25), ("Botas", 45.0)]:
        con.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", fila)

with sqlite3.connect("crud.db") as con:
    for nombre, precio in con.execute("SELECT nombre, precio FROM productos"):
        print(f"{nombre:<10}{precio:>8.2f}")

# -> Camisa       19.90
# -> Gorra         7.25
# -> Botas        45.00
```
</details>

**4.2.** Sube un 10 % el precio de las gorras (Update) y comprueba el resultado.
<details><summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect("upd.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT, precio REAL)")
    con.execute("INSERT INTO productos VALUES (?, ?)", ("Gorra", 10.0))
    con.execute("UPDATE productos SET precio = precio * 1.10 WHERE nombre = ?", ("Gorra",))

with sqlite3.connect("upd.db") as con:
    print(con.execute("SELECT precio FROM productos").fetchone())   # -> (11.0,)
```
</details>

**4.3.** Borra un producto por su nombre (Delete). ¿Qué pasa si te dejas el `WHERE`?
<details><summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect("del.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT)")
    con.executemany("INSERT INTO productos VALUES (?)", [("Camisa",), ("Gorra",)])
    con.execute("DELETE FROM productos WHERE nombre = ?", ("Gorra",))

with sqlite3.connect("del.db") as con:
    print(con.execute("SELECT COUNT(*) FROM productos").fetchone()[0])   # -> 1

# Sin WHERE, "DELETE FROM productos" borra la tabla ENTERA y no hay deshacer.
# Antes de lanzar un DELETE, escribe primero el SELECT con ese mismo WHERE
# y mira qué filas salen.
```
</details>


### Tema 5 · Consultas parametrizadas

**5.1.** Busca un producto por nombre usando una consulta **parametrizada**.
<details><summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect("param.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT, precio REAL)")
    con.execute("INSERT INTO productos VALUES (?, ?)", ("Camisa", 19.9))

buscado: str = "Camisa"

with sqlite3.connect("param.db") as con:
    filas = con.execute(
        "SELECT nombre, precio FROM productos WHERE nombre = ?", (buscado,)).fetchall()

print(filas)   # -> [('Camisa', 19.9)]

# La coma de (buscado,) NO es opcional: sin ella no es una tupla.
```
</details>

**5.2.** Comprueba que un nombre con apóstrofo rompe la consulta si la construyes concatenando texto, y que con `?` no pasa nada.
<details><summary>Solución</summary>

```python
import sqlite3

buscado = "O" + chr(39) + "Keeffe"      # O'Keeffe

with sqlite3.connect("comillas.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS autores (nombre TEXT)")
    con.execute("INSERT INTO autores VALUES (?)", (buscado,))

# MAL: el apóstrofo cierra la cadena SQL antes de tiempo
comilla = chr(39)
sql_malo = "SELECT * FROM autores WHERE nombre = " + comilla + buscado + comilla
with sqlite3.connect("comillas.db") as con:
    try:
        con.execute(sql_malo).fetchall()
    except sqlite3.OperationalError:
        print("la concatenada revienta")   # -> la concatenada revienta

# BIEN: el ? se encarga de escapar lo que haga falta
with sqlite3.connect("comillas.db") as con:
    filas = con.execute(
        "SELECT nombre FROM autores WHERE nombre = ?", (buscado,)).fetchall()

print(len(filas))   # -> 1

# Y esto no va de comillas raras: es la MISMA puerta por la que entra una
# inyección SQL. El ? la cierra.
```
</details>

**5.3.** Explica por qué esto es peligroso: `f"SELECT * FROM u WHERE nombre = '{nombre}'"`.
<details><summary>Solución</summary>

```text
Porque lo que escriba el usuario se convierte en SQL. Es inyeccion SQL.

Si nombre vale:    ' OR '1'='1
la consulta queda: SELECT * FROM u WHERE nombre = '' OR '1'='1'
y devuelve TODAS las filas de la tabla.

Peor aun, con  '; DROP TABLE u; --  se puede destruir la tabla.

Con parametros nunca pasa: el ? no mezcla datos con instrucciones. Lo que
llega por ? se trata SIEMPRE como un valor, aunque parezca codigo SQL.
Por eso el criterio de esta unidad es todo-o-nada: una sola consulta
concatenada y el punto se pierde.
```
</details>


### Tema 6 · Filtrar y ordenar

**6.1.** Muestra los productos de más de 10 € ordenados de más caro a más barato.
<details><summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect("filtro.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT, precio REAL)")
    con.executemany("INSERT INTO productos VALUES (?, ?)",
                    [("Camisa", 19.9), ("Gorra", 7.25), ("Botas", 45.0)])

with sqlite3.connect("filtro.db") as con:
    filas = con.execute(
        "SELECT nombre, precio FROM productos WHERE precio > ? ORDER BY precio DESC",
        (10,)).fetchall()

print(filas)   # -> [('Botas', 45.0), ('Camisa', 19.9)]
```
</details>

**6.2.** Cuenta cuántos productos hay y calcula el precio medio.
<details><summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect("agr.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS productos (precio REAL)")
    con.executemany("INSERT INTO productos VALUES (?)", [(10.0,), (20.0,), (30.0,)])

with sqlite3.connect("agr.db") as con:
    cuantos = con.execute("SELECT COUNT(*) FROM productos").fetchone()[0]
    media = con.execute("SELECT AVG(precio) FROM productos").fetchone()[0]

print(cuantos, media)   # -> 3 20.0

# fetchone() devuelve una TUPLA: por eso el [0] para sacar el valor.
```
</details>

**6.3.** Busca los productos cuyo nombre empieza por «Ca», con `LIKE` y sin concatenar.
<details><summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect("like.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT)")
    con.executemany("INSERT INTO productos VALUES (?)",
                    [("Camisa",), ("Camiseta",), ("Gorra",)])

with sqlite3.connect("like.db") as con:
    filas = con.execute(
        "SELECT nombre FROM productos WHERE nombre LIKE ?", ("Ca%",)).fetchall()

print(filas)   # -> [('Camisa',), ('Camiseta',)]

# El comodín % va DENTRO del parámetro, no pegado al SQL.
```
</details>


### Tema 7 · Estructura de la aplicación

**7.1.** Separa en dos funciones el acceso a datos y la presentación: `listar(bd)` devuelve, `mostrar(filas)` imprime.
<details><summary>Solución</summary>

```python
import sqlite3


def listar(bd: str) -> list[tuple]:
    """Solo consulta: devuelve las filas."""
    with sqlite3.connect(bd) as con:
        return con.execute("SELECT nombre, precio FROM productos").fetchall()


def mostrar(filas: list[tuple]) -> None:
    """Solo presenta: no sabe nada de la base de datos."""
    for nombre, precio in filas:
        print(f"{nombre:<10}{precio:>8.2f}")


with sqlite3.connect("cap.db") as con:
    con.execute("CREATE TABLE IF NOT EXISTS productos (nombre TEXT, precio REAL)")
    con.execute("INSERT INTO productos VALUES (?, ?)", ("Camisa", 19.9))

mostrar(listar("cap.db"))   # -> Camisa       19.90

# listar() se puede probar con un test (devuelve datos comparables);
# mostrar() se puede reutilizar aunque mañana los datos vengan de un CSV.
```
</details>

**7.2.** ¿Por qué las funciones de acceso a datos reciben la ruta de la base de datos como parámetro en vez de tenerla escrita dentro?
<details><summary>Solución</summary>

```text
Porque asi se pueden PROBAR. El test crea una base de datos temporal
(tmp_path) y se la pasa a la funcion; al terminar, desaparece.

Si la ruta esta escrita dentro de la funcion:
  - los tests machacarian la base de datos de verdad
  - no se podrian ejecutar dos a la vez
  - no podrias tener una BD de pruebas y otra de produccion

Es la misma idea de siempre: todo lo que la funcion necesita, entra por
parametros.
```
</details>

**7.3.** Monta el esqueleto completo de la aplicación: crear tabla, insertar, listar y un `main()` que lo use.
<details><summary>Solución</summary>

```python
"""Mini aplicación con base de datos."""
import sqlite3

BD: str = "app.db"


def crear_tabla(bd: str) -> None:
    """Crea la tabla si no existe."""
    with sqlite3.connect(bd) as con:
        con.execute("CREATE TABLE IF NOT EXISTS notas (alumno TEXT, nota REAL)")


def insertar(bd: str, alumno: str, nota: float) -> None:
    """Añade una nota."""
    with sqlite3.connect(bd) as con:
        con.execute("INSERT INTO notas (alumno, nota) VALUES (?, ?)", (alumno, nota))


def listar(bd: str) -> list[tuple]:
    """Devuelve todas las notas."""
    with sqlite3.connect(bd) as con:
        return con.execute("SELECT alumno, nota FROM notas").fetchall()


def main() -> None:
    """Punto de entrada."""
    crear_tabla(BD)
    insertar(BD, "Ada", 9.5)
    for alumno, nota in listar(BD):
        print(f"{alumno}: {nota}")


if __name__ == "__main__":
    main()   # -> Ada: 9.5
```
</details>


### Actividades guiadas

#### Actividad 1 — Crear la base de datos
Crea `prueba.db` con una tabla `alumnos` (id, nombre, nota).
<details><summary>Solución</summary>

```python
import sqlite3

with sqlite3.connect("prueba.db") as con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nota   REAL NOT NULL
        )
    """)
```
</details>

#### Actividad 2 — Insertar y listar
<details><summary>Solución</summary>

```python
with sqlite3.connect("prueba.db") as con:
    con.execute("INSERT INTO alumnos (nombre, nota) VALUES (?, ?)", ("Ada", 9.5))

with sqlite3.connect("prueba.db") as con:
    for fila in con.execute("SELECT id, nombre, nota FROM alumnos"):
        print(fila)
```
</details>

#### Actividad 3 — Modificar y borrar
<details><summary>Solución</summary>

```python
with sqlite3.connect("prueba.db") as con:
    con.execute("UPDATE alumnos SET nota = ? WHERE nombre = ?", (10.0, "Ada"))
    con.execute("DELETE FROM alumnos WHERE nota < ?", (5.0,))
```
</details>

#### Actividad 4 — Buscar
Muestra los alumnos aprobados ordenados por nota descendente.
<details><summary>Solución</summary>

```python
with sqlite3.connect("prueba.db") as con:
    filas = con.execute(
        "SELECT nombre, nota FROM alumnos WHERE nota >= ? ORDER BY nota DESC",
        (5.0,)
    ).fetchall()
print(filas)
```
</details>

### Ejercicios propuestos

**E1 ○ · Contar registros.** `cuantos(bd: str) -> int` con `COUNT(*)`.
<details><summary>Solución</summary>

```python
import sqlite3

def cuantos(bd: str) -> int:
    with sqlite3.connect(bd) as con:
        return int(con.execute("SELECT COUNT(*) FROM alumnos").fetchone()[0])
```
</details>

**E2 ○ · Nota media.** `nota_media(bd: str) -> float` con `AVG`, devolviendo `0.0` si no hay filas.
<details><summary>Pista</summary><code>AVG</code> devuelve <code>None</code> con la tabla vacía.</details>
<details><summary>Solución</summary>

```python
def nota_media(bd: str) -> float:
    with sqlite3.connect(bd) as con:
        resultado = con.execute("SELECT AVG(nota) FROM alumnos").fetchone()[0]
    return float(resultado) if resultado is not None else 0.0
```
</details>

**E3 ◐ · Buscar por nombre.** Búsqueda parcial parametrizada con `LIKE`.
<details><summary>Solución</summary>

```python
def buscar(bd: str, texto: str) -> list[tuple]:
    with sqlite3.connect(bd) as con:
        return con.execute(
            "SELECT nombre, nota FROM alumnos WHERE nombre LIKE ?",
            (f"%{texto}%",)
        ).fetchall()
```
</details>

**E4 ● · Menú CRUD.** Programa con menú (alta, listado, modificación, baja, salir) y entrada validada.
<details><summary>Solución</summary>

```python
def menu() -> None:
    crear_tabla()
    opcion = ""
    while opcion != "0":
        print("1-Alta  2-Listar  3-Modificar  4-Baja  0-Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            insertar(input("Nombre: "), float(input("Precio: ")), 0)
        elif opcion == "2":
            for fila in listar():
                print(fila)
```
*(Añade `try/except` en las conversiones, como en la UD3.)*
</details>

**E5 ○ · Crear la tabla de clientes.** `crear_tabla(bd: str) -> None` crea la tabla `clientes` si no existe, con `id` autonumérico, `nombre` obligatorio y `email`.
<details><summary>Pista</summary><code>CREATE TABLE IF NOT EXISTS</code>, y el id como <code>INTEGER PRIMARY KEY AUTOINCREMENT</code>.</details>
<details><summary>Solución</summary>

```python
import sqlite3


def crear_tabla(bd: str) -> None:
    """Crea la tabla clientes si no existe."""
    with sqlite3.connect(bd) as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email  TEXT
            )
        """)
```
</details>

**E6 ◐ · Insertar un cliente.** `insertar(bd: str, nombre: str, email: str) -> None` añade un cliente con una consulta **parametrizada**.
<details><summary>Pista</summary>Los valores van como <code>?</code> y en una tupla aparte. Nunca concatenados.</details>
<details><summary>Solución</summary>

```python
import sqlite3


def insertar(bd: str, nombre: str, email: str) -> None:
    """Añade un cliente."""
    with sqlite3.connect(bd) as con:
        con.execute("INSERT INTO clientes (nombre, email) VALUES (?, ?)",
                    (nombre, email))
```
</details>

**E7 ◐ · Buscar por email.** `buscar_por_email(bd: str, email: str) -> list[tuple]` devuelve `[(nombre, email), ...]` de los clientes con ese email exacto. Lista vacía si no hay ninguno.
<details><summary>Pista</summary>Mismo patrón que el insertar, pero con <code>SELECT ... WHERE email = ?</code> y <code>.fetchall()</code>.</details>
<details><summary>Solución</summary>

```python
import sqlite3


def buscar_por_email(bd: str, email: str) -> list[tuple]:
    """Clientes con ese email exacto."""
    with sqlite3.connect(bd) as con:
        return con.execute(
            "SELECT nombre, email FROM clientes WHERE email = ?", (email,)).fetchall()
```
</details>

**E8 ● · Actualizar y contar los cambios.** `actualizar_email(bd: str, nombre: str, email: str) -> int` cambia el email de ese cliente y devuelve **cuántas filas ha modificado**.
<details><summary>Pista</summary>El cursor tiene un atributo <code>rowcount</code> con el número de filas afectadas por la última operación.</details>
<details><summary>Solución</summary>

```python
import sqlite3


def actualizar_email(bd: str, nombre: str, email: str) -> int:
    """Cambia el email de un cliente; devuelve cuántas filas cambió."""
    with sqlite3.connect(bd) as con:
        cur = con.execute("UPDATE clientes SET email = ? WHERE nombre = ?",
                          (email, nombre))
        return cur.rowcount
```
</details>

---

---

## 10. Práctica tipo examen

Los ejercicios de arriba tienen la solución a la vista. Lo que viene
ahora **no**: aquí se comprueba si sabes hacerlo solo, que es lo que mide el examen.

Son dos escalones, y en este orden:

| | Qué es | Cómo sabes si va bien |
|---|---|---|
| **Proyecto de la unidad** | Un proyecto Python completo, para trabajar con calma | Sus tests, que ejecutas tú |
| **Simulacro** | Mismo formato, tamaño y rúbrica que el examen, contrarreloj | Sus tests, y la tabla de apartados |

---

## 11. Proyecto de la unidad

Toda la práctica de esta unidad se hace sobre un **proyecto base**: un inventario sobre una base de datos SQLite. Está montado
con la estructura real de un proyecto Python y trae una **batería de tests** que puedes
ejecutar en cualquier momento para ver si va todo bien.

**[Proyecto Inventario →](../proyectos/ud6/README.md)**

```
proyecto-ud6/
├── src/      ← tu código (funciones con TODO)
└── tests/    ← 13 tests que comprueban tu trabajo
```

### Cómo se trabaja

```bash
pip install -r requirements.txt
pytest
```

La primera vez falla casi todo: aún no has escrito nada. A partir de ahí, lee una función,
escríbela, vuelve a lanzar `pytest` y comprueba si ese test ya pasa. Terminas cuando está
**todo en verde** y `mypy src` dice *Success*.

!!! tip "De uno en uno"
    `pytest -x` se detiene en el primer fallo. Arreglas esa función y sigues. Mucho más
    llevadero que enfrentarse a todos los errores a la vez.

!!! warning "Los tests son la especificación"
    No los modifiques para que pasen: describen exactamente lo que tu código debe hacer, y
    el examen usará una batería equivalente.

Detalles y comandos útiles en **[Proyectos](../proyectos/index.md)**.

---

---

## 12. Simulacro de examen

Cuando tengas el proyecto terminado, mídete: el **simulacro** es un examen de mentira con
**el mismo formato, tamaño y rúbrica** que el de verdad — y con los tests publicados.

**[Simulacro RA6 · Museo en SQLite →](../simulacros/ra6/README.md)** · 11 tests · 45–50 min

Hazlo **contrarreloj y sin ayuda**, como si fuera el examen. Al terminar, aplica la rúbrica
y tendrás una estimación bastante fiel de tu nota.

!!! warning "El examen de verdad va sin tests"
    Allí solo tendrás los **docstrings** y unos ejemplos. Por eso, en el simulacro, intenta
    resolver cada función leyendo solo su docstring y mira el test únicamente cuando falle.

---

---

## 13. Retos opcionales

- **R1.** Añade una segunda tabla `categorias` y relaciónala con `productos` mediante una clave ajena.
- **R2.** Investiga `GROUP BY` y cuenta cuántos productos hay por categoría.
- **R3.** Exporta el contenido de la tabla a un CSV, reutilizando lo de la UD5.

- **R4.** Añade a tu aplicación un menú de consola con las cuatro operaciones del CRUD.
- **R5.** Investiga `GROUP BY` y escribe una consulta que cuente cuántos productos hay de cada categoría.
- **R6.** Haz que la aplicación funcione con una base de datos de prueba cuando se lanza con el argumento `--test`, para no tocar la de verdad.
---

---

## 14. Autoevaluación rápida

<details><summary>1. ¿Qué pasa si olvidas <code>commit()</code>?</summary>Los cambios no se guardan, aunque no dé ningún error.</details>
<details><summary>2. ¿Por qué usar <code>?</code> en vez de concatenar?</summary>Para evitar la inyección SQL.</details>
<details><summary>3. ¿Qué hace <code>UPDATE productos SET precio = 0</code> sin <code>WHERE</code>?</summary>Pone el precio a 0 en TODAS las filas.</details>
<details><summary>4. Diferencia entre <code>fetchall()</code> y <code>fetchone()</code>.</summary>El primero devuelve todas las filas; el segundo, solo la siguiente.</details>
<details><summary>5. ¿Para qué <code>IF NOT EXISTS</code>?</summary>Para que crear la tabla no falle si ya existe.</details>
<details><summary>6. ¿Qué devuelve <code>AVG</code> con la tabla vacía?</summary><code>None</code>: hay que contemplarlo.</details>

---

---

## 15. Glosario

| Término | Definición |
|---|---|
| **SGBD** | Sistema gestor de bases de datos. |
| **Tabla / fila / columna** | Estructura, registro y campo. |
| **Clave primaria** | Campo que identifica cada fila de forma única. |
| **SQL** | Lenguaje para consultar y manipular la base de datos. |
| **CRUD** | Crear, leer, actualizar y borrar. |
| **Cursor** | Objeto que ejecuta sentencias y recorre resultados. |
| **`commit`** | Confirma los cambios pendientes. |
| **Consulta parametrizada** | La que pasa los datos con `?` en vez de concatenarlos. |
| **Inyección SQL** | Ataque que aprovecha el SQL construido por concatenación. |

---

---

## 16. Cómo se evalúa esta unidad (RA6)

El examen es **100 % práctico**: se entrega un proyecto con las funciones vacías y una
especificación, y hay que escribir el código.

**La nota sale solo de los casos de prueba.** No hay puntos por presentación ni por
esfuerzo: cada apartado del examen vale en proporción a los casos que tiene, de modo que
**todos los casos valen lo mismo**.

`nota del apartado = (casos superados ÷ casos del apartado) × puntos del apartado`

`nota del examen = suma de los apartados`

### Así es el examen

**Biblioteca en SQLite** · entrega `src/biblioteca.py` · **50 min**

| # | Apartado | Casos | Puntos |
|:---:|---|:---:|:---:|
| **A** | Crear la tabla e insertar | 3 | **3,00** |
| **B** | Consultas | 5 | **5,00** |
| **C** | Borrado | 2 | **2,00** |
| | **TOTAL** | **10** | **10,00** |

Esta tabla viene en el enunciado, así que sabes desde el primer minuto **qué vale cada
parte** y por dónde empezar si vas justo de tiempo.

!!! warning "El examen se reparte sin tests"
    La carpeta `tests/` viene vacía. La especificación son los **docstrings** de cada
    función y los ejemplos del enunciado. Por eso conviene que en el simulacro te
    acostumbres a resolver leyendo el docstring y no el test.

### Así se corrige

Alguien que entrega el examen con **8 de los 10 casos** superados
—se le ha escapado el apartado **C**, donde falla 2 de
2 casos—:

| # | Apartado | Casos superados | Puntos |
|:---:|---|:---:|---|
| A | Crear la tabla e insertar | 3 / 3 | 3,00 / 3,00 |
| B | Consultas | 5 / 5 | 5,00 / 5,00 |
| C | Borrado | 0 / 2 | 0,00 / 2,00  ← |
| | | | **NOTA: 8,00** |

La corrección es automática: se monta un proyecto con la batería completa más el fichero
entregado, se ejecuta y se reparte la nota con esa cuenta. **Nadie interpreta nada.**

Además recibes un informe con los casos concretos que han fallado, con el valor que
esperaba y el que devolvió tu función.

!!! note "Los tres requisitos de la entrega"
    No puntúan por separado, pero forman parte de la especificación:

    1. Entregar **el fichero de `src/`**, con ese nombre.
    2. `mypy src` sin errores.
    3. Cada función con su **docstring**.

    Un fichero que no compila o que no se puede importar da **0 casos superados**, así que
    en la práctica valen mucho más que unos puntos.

---

### Material de apoyo de la unidad

- **[Proyecto de la unidad](../proyectos/ud6/README.md)** — `inventario`, 13 tests.
- **[Simulacro de examen](../simulacros/ra6/README.md)** — `museo`, 11 tests.
