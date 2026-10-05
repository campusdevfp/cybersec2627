# Unidad 5 · Entrada/salida y ficheros

> **Módulo:** CMO-313 · Fundamentos de programación
> **Resultado de aprendizaje:** RA5 · **Duración:** 6 h · **Peso:** 10 %
> **Lenguaje:** Python 3 (tipado)

Todos tus programas hasta ahora tenían un problema: **al cerrarlos, los datos desaparecían**. Esta unidad lo resuelve. Aprenderás a guardar información en ficheros y a recuperarla después, que es lo que convierte un ejercicio en una aplicación de verdad.

---

## Mapa de la unidad

<figure markdown>
  ![Mapa de la unidad 5](../assets/diagramas/ud5-mapa.svg#only-light)
  ![Mapa de la unidad 5](../assets/diagramas/ud5-mapa-dark.svg#only-dark)
  <figcaption>Los ficheros permiten que los datos sobrevivan al programa.</figcaption>
</figure>

### Qué vas a saber hacer al terminar

- [ ] Dar formato profesional a la salida por consola (columnas alineadas).
- [ ] Abrir ficheros correctamente con `with open(...)`.
- [ ] Escribir y leer **ficheros de texto**.
- [ ] Trabajar con **CSV** usando el módulo `csv`.
- [ ] Guardar y recuperar datos estructurados en **JSON**.
- [ ] Gestionar los errores típicos: fichero que no existe, permisos, codificación.

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

## 1. Salida por consola con formato

Ya conoces las f-strings. Aquí las llevamos al punto en que la salida parece profesional.

### 1.1 Alinear en columnas

```python
productos = [("Camisa", 19.99), ("Pantalón", 34.5), ("Gorra", 8.0)]

print(f"{'PRODUCTO':<12}{'PRECIO':>10}")
print("-" * 22)
for nombre, precio in productos:
    print(f"{nombre:<12}{precio:>10.2f}")
```

```text
PRODUCTO        PRECIO
----------------------
Camisa           19.99
Pantalón         34.50
Gorra             8.00
```

| Formato | Efecto |
|---|---|
| `:<12` | alinea a la **izquierda** en 12 caracteres |
| `:>10` | alinea a la **derecha** en 10 |
| `:^10` | **centra** en 10 |
| `:>10.2f` | derecha, 10 de ancho, 2 decimales |
| `:,` | separador de miles |

!!! tip "Los números, siempre a la derecha"
    Alineados a la derecha, las unidades quedan una debajo de otra y la tabla se lee de un vistazo.

> **Reto rápido 1.** Muestra tres nombres a la izquierda en 15 caracteres y sus edades a la derecha en 5.

## 2. Abrir ficheros: `with open(...)`

### 2.1 La forma correcta

```python
with open("datos.txt", "w", encoding="utf-8") as fichero:
    fichero.write("Hola\n")
# aquí el fichero YA está cerrado, automáticamente
```

Tres cosas, y las tres importan:

| Parte | Para qué |
|---|---|
| `with` | **cierra el fichero solo**, incluso si hay un error |
| `"w"` | el **modo** de apertura |
| `encoding="utf-8"` | para que las tildes y la ñ no se rompan |

!!! danger "Sin `with`, tarde o temprano pierdes datos"
    ```python
    f = open("datos.txt", "w")
    f.write("Hola")        # si algo falla aquí, el fichero queda abierto
    f.close()              # ...y esto no se ejecuta: se pierde lo escrito
    ```
    **Usa siempre `with`.**

### 2.2 Modos de apertura

| Modo | Qué hace | Cuidado |
|:---:|---|---|
| `"r"` | **leer** (por defecto) | error si no existe |
| `"w"` | **escribir** | **borra** el contenido anterior |
| `"a"` | **añadir** al final | no borra |
| `"x"` | crear nuevo | error si ya existe |

!!! warning "`w` borra sin avisar"
    Abrir con `"w"` un fichero que ya tiene datos lo deja **vacío** al instante. Si quieres conservar lo anterior, usa `"a"`.

> **Reto rápido 2.** ¿Qué modo usarías para un fichero de registro (log) al que se van añadiendo líneas? *(Respuesta: `"a"`.)*

## 3. Ficheros de texto

### 3.1 Escribir

```python
lineas = ["Ada", "Linus", "Grace"]

with open("nombres.txt", "w", encoding="utf-8") as f:
    for nombre in lineas:
        f.write(nombre + "\n")      # \n = salto de línea
```

!!! tip "`write()` no añade el salto de línea"
    A diferencia de `print()`, hay que ponerlo a mano con `\n`. Si lo olvidas, todo queda pegado en una sola línea.

### 3.2 Leer

Tres formas, según lo que necesites:

```python
# a) todo el contenido en una cadena
with open("nombres.txt", encoding="utf-8") as f:
    contenido: str = f.read()

# b) una lista con todas las líneas
with open("nombres.txt", encoding="utf-8") as f:
    lineas: list[str] = f.readlines()

# c) línea a línea (la mejor para ficheros grandes)
with open("nombres.txt", encoding="utf-8") as f:
    for linea in f:
        print(linea.rstrip())       # rstrip quita el \n final
```

!!! warning "Acuérdate de `rstrip()`"
    Cada línea leída **incluye el `\n`**. Si comparas `linea == "Ada"` fallará, porque en realidad vale `"Ada\n"`. Límpiala con `linea.rstrip()`.

### 3.3 Si el fichero no existe

```python
try:
    with open("nombres.txt", encoding="utf-8") as f:
        contenido = f.read()
except FileNotFoundError:
    print("El fichero no existe todavía")
    contenido = ""
```

---

> **Reto rápido 3.** Escribe tu nombre en `yo.txt`, ciérralo y vuelve a leerlo mostrando el contenido **sin** el salto de línea final. *(Pista: `.strip()`.)*

## 4. Ficheros CSV

Un **CSV** (*comma-separated values*) es un fichero de texto con datos en forma de tabla: una fila por línea y las columnas separadas por comas. Es lo que exporta cualquier hoja de cálculo.

```text
nombre,telefono,email
Ada,600111222,ada@ejemplo.com
Linus,600333444,linus@ejemplo.com
```

Se puede tratar como texto, pero el módulo `csv` gestiona solo los casos peliagudos (comas dentro de un campo, comillas…).

### 4.1 Escribir un CSV

```python
import csv

contactos = [
    ["Ada", "600111222", "ada@ejemplo.com"],
    ["Linus", "600333444", "linus@ejemplo.com"],
]

with open("contactos.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre", "telefono", "email"])   # cabecera
    escritor.writerows(contactos)                        # todas las filas
```

!!! tip "`newline=\"\"` no es opcional"
    Sin él, en Windows aparece una línea en blanco entre cada fila. Póngase siempre al abrir un CSV.

### 4.2 Leer un CSV

```python
import csv

with open("contactos.csv", encoding="utf-8") as f:
    lector = csv.reader(f)
    cabecera = next(lector)          # se salta la primera fila
    for fila in lector:
        nombre, telefono, email = fila
        print(f"{nombre:<10}{telefono:>12}")
```

### 4.3 Con nombres de columna: `DictReader`

Más legible, porque accedes por nombre en vez de por posición:

```python
import csv

with open("contactos.csv", encoding="utf-8") as f:
    for fila in csv.DictReader(f):
        print(fila["nombre"], fila["email"])
```

> Todo lo que se lee de un CSV es **texto**. Si una columna es numérica, hay que convertirla: `int(fila["edad"])`.

> **Reto rápido 3.** ¿Por qué `csv.reader` es mejor que hacer `linea.split(",")`? *(Porque gestiona las comas que van dentro de un campo entrecomillado.)*

## 5. JSON

**JSON** guarda datos con estructura (diccionarios y listas anidados), no solo tablas. Es el formato que usan casi todas las APIs web.

```python
import json

datos = {
    "nombre": "Ada",
    "edad": 36,
    "lenguajes": ["Python", "C"],
}

# guardar
with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

# recuperar
with open("datos.json", encoding="utf-8") as f:
    recuperado = json.load(f)

print(recuperado["nombre"])          # Ada
print(recuperado["lenguajes"][0])    # Python
```

| Parámetro | Para qué |
|---|---|
| `indent=2` | lo escribe con sangría, legible para personas |
| `ensure_ascii=False` | conserva tildes y ñ en lugar de escaparlas |

### CSV o JSON, ¿cuál?

| Usa **CSV** si… | Usa **JSON** si… |
|---|---|
| los datos son una tabla plana | hay estructura anidada |
| se van a abrir en Excel | los consume otro programa |
| todas las filas tienen los mismos campos | los campos varían |

---

> **Reto rápido 5.** Guarda `{"modulo": "CMO-313", "horas": 50}` en un JSON legible y comprueba abriendo el fichero que se entiende a simple vista.

## 6. Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| `FileNotFoundError` | el fichero no existe o la ruta está mal | contrólalo con `try/except` |
| Se borró el contenido | abriste con `"w"` | usa `"a"` para añadir |
| Todo en una sola línea | falta `\n` en `write()` | añádelo |
| `Ada\n` al comparar | la línea conserva el salto | usa `.rstrip()` |
| Tildes raras (`Ã¡`) | falta el encoding | `encoding="utf-8"` siempre |
| Líneas en blanco en el CSV | falta `newline=""` | añádelo al abrir |
| `TypeError` al sumar del CSV | los datos leídos son texto | convierte con `int()`/`float()` |
| El fichero queda bloqueado | no usaste `with` | usa `with` |

---

---

## 7. Ejercicios

Aquí están **todos los ejercicios de la unidad**, agrupados por el
tema al que corresponden y con la solución desplegable.

**Haz los de un tema en cuanto termines de leerlo.** No esperes al final: son cortos y solo
usan lo que acabas de ver, así que si algo no ha quedado claro lo descubres en el momento y
no tres semanas después.

!!! warning "Intenta antes de desplegar"
    Abrir la solución sin haberlo intentado da sensación de aprender, y no enseña nada. Si
    llevas quince minutos sin avanzar, mírala. Si llevas dos, no.


### Tema 1 · Salida con formato

**1.1.** Muestra una tabla de tres productos con el nombre a la izquierda (14 huecos) y el precio a la derecha con dos decimales (8 huecos).
<details><summary>Solución</summary>

```python
productos = [("Camisa", 19.9), ("Pantalón", 34.5), ("Gorra", 7.25)]

for nombre, precio in productos:
    print(f"{nombre:<14}{precio:>8.2f}")

# -> Camisa           19.90
# -> Pantalón         34.50
# -> Gorra             7.25
```
</details>

**1.2.** Añade a esa tabla una **cabecera** y una línea separadora del mismo ancho.
<details><summary>Solución</summary>

```python
ANCHO: int = 22

print(f"{'Producto':<14}{'Precio':>8}")
print("-" * ANCHO)
print(f"{'Camisa':<14}{19.9:>8.2f}")

# -> Producto        Precio
# -> ----------------------
# -> Camisa           19.90
```
</details>

**1.3.** Muestra `1234567.891` con separador de miles y dos decimales, y un porcentaje del `0.1567` con un decimal.
<details><summary>Solución</summary>

```python
print(f"{1234567.891:,.2f}")   # -> 1,234,567.89
print(f"{0.1567:.1%}")        # -> 15.7%
```
</details>


**1.4.** Muestra un recibo de tres líneas con el concepto a la izquierda en 16 huecos y el importe a la derecha en 9 con dos decimales, y una línea de total separada por guiones.
<details><summary>Solución</summary>

```python
ANCHO: int = 25

conceptos = [("Cuota mensual", 39.9), ("Material", 12.0), ("Descuento", -5.5)]

for concepto, importe in conceptos:
    print(f"{concepto:<16}{importe:>9.2f}")

total = sum(i for _, i in conceptos)
print("-" * ANCHO)
print(f"{'TOTAL':<16}{total:>9.2f}")

# -> Cuota mensual       39.90
# -> Material            12.00
# -> Descuento           -5.50
# -> -------------------------
# -> TOTAL               46.40
```
</details>


### Tema 2 · Abrir ficheros

**2.1.** Escribe un texto en un fichero y vuelve a leerlo, usando `with`.
<details><summary>Solución</summary>

```python
with open("nota.txt", "w", encoding="utf-8") as f:
    f.write("Hola desde Python\n")

with open("nota.txt", encoding="utf-8") as f:
    print(f.read().strip())   # -> Hola desde Python
```
</details>

**2.2.** ¿Qué diferencia hay entre los modos `"w"` y `"a"`? Compruébalo.
<details><summary>Solución</summary>

```python
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("primera\n")

with open("log.txt", "w", encoding="utf-8") as f:
    f.write("segunda\n")     # "w" MACHACA: la primera línea ya no está

with open("log.txt", "a", encoding="utf-8") as f:
    f.write("tercera\n")     # "a" AÑADE al final

with open("log.txt", encoding="utf-8") as f:
    print(f.read().strip())

# -> segunda
# -> tercera
```
</details>

**2.3.** ¿Por qué se usa `with` en vez de `open()` y `close()`? Explícalo y escribe el equivalente sin `with`.
<details><summary>Solución</summary>

```python
# Sin with, hay que acordarse de cerrar... y si salta un error por el medio,
# el close() no se ejecuta y el fichero se queda abierto (o a medio escribir).
f = open("datos.txt", "w", encoding="utf-8")
try:
    f.write("contenido")
finally:
    f.close()

# Con with, Python cierra SIEMPRE al salir del bloque, haya error o no:
with open("datos.txt", encoding="utf-8") as g:
    print(g.read())   # -> contenido
```
</details>


**2.4.** Escribe en un fichero, léelo y **añade** una línea más, comprobando después que están las dos.
<details><summary>Solución</summary>

```python
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("primera\n")

with open("notas.txt", "a", encoding="utf-8") as f:
    f.write("segunda\n")

with open("notas.txt", encoding="utf-8") as f:
    print(f.read().strip())

# -> primera
# -> segunda
```
</details>


### Tema 3 · Ficheros de texto

**3.1.** Escribe tres líneas en un fichero y luego cuéntalas al leerlo.
<details><summary>Solución</summary>

```python
with open("nombres.txt", "w", encoding="utf-8") as f:
    for nombre in ["Ada", "Alan", "Grace"]:
        f.write(nombre + "\n")

with open("nombres.txt", encoding="utf-8") as f:
    lineas = f.readlines()

print(len(lineas))   # -> 3
```
</details>

**3.2.** Lee un fichero línea a línea quitando el salto de línea final.
<details><summary>Solución</summary>

```python
with open("nombres.txt", "w", encoding="utf-8") as f:
    f.write("Ada\nAlan\n")

with open("nombres.txt", encoding="utf-8") as f:
    for linea in f:
        print(f"[{linea.strip()}]")   # sin strip() saldría el \n dentro del corchete

# -> [Ada]
# -> [Alan]
```
</details>

**3.3.** Lee un fichero que puede no existir sin que el programa se caiga.
<details><summary>Solución</summary>

```python
def leer(ruta: str) -> str:
    """Contenido del fichero; cadena vacía si no existe."""
    try:
        with open(ruta, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

print(repr(leer("no_existe.txt")))   # -> ''

# El fichero que no está es EL caso límite de esta unidad: sale en todos los tests.
```
</details>


**3.4.** Lee un fichero y devuelve la **última** línea, sin el salto final. Cadena vacía si el fichero está vacío o no existe.
<details><summary>Solución</summary>

```python
def ultima_linea(ruta: str) -> str:
    """Última línea del fichero; cadena vacía si no hay o no existe."""
    try:
        with open(ruta, encoding="utf-8") as f:
            lineas = f.read().splitlines()
    except FileNotFoundError:
        return ""
    if not lineas:
        return ""
    return lineas[-1]


with open("d.txt", "w", encoding="utf-8") as f:
    f.write("uno\ndos\ntres\n")

print(ultima_linea("d.txt"))          # -> tres
print(repr(ultima_linea("nada.txt")))  # -> ''
```
</details>


### Tema 4 · CSV

**4.1.** Guarda dos filas en un CSV con cabecera y vuelve a leerlas.
<details><summary>Solución</summary>

```python
import csv

filas = [("Camisa", 10), ("Gorra", 25)]

with open("stock.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre", "cantidad"])
    for nombre, cantidad in filas:
        escritor.writerow([nombre, cantidad])

with open("stock.csv", newline="", encoding="utf-8") as f:
    lector = csv.reader(f)
    next(lector)                       # saltar la cabecera
    print([fila for fila in lector])   # -> [['Camisa', '10'], ['Gorra', '25']]
```
</details>

**4.2.** En el ejercicio anterior la cantidad se lee como texto. Conviértela a `int` al cargar.
<details><summary>Solución</summary>

```python
import csv

with open("stock.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre", "cantidad"])
    escritor.writerow(["Camisa", 10])

with open("stock.csv", newline="", encoding="utf-8") as f:
    lector = csv.reader(f)
    next(lector, None)
    filas = [(fila[0], int(fila[1])) for fila in lector if fila]

print(filas)   # -> [('Camisa', 10)]

# Todo lo que sale de un CSV es TEXTO. Si no conviertes, "10" + 5 revienta.
```
</details>

**4.3.** Tu CSV sale con una línea en blanco entre cada fila. ¿Qué falta?
<details><summary>Solución</summary>

```python
import csv

# El culpable: abrir sin newline="". En Windows se escribe \r\n dos veces.
with open("bien.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerow(["a", "b"])

with open("bien.csv", encoding="utf-8") as f:
    contenido = f.read()

print("\n\n" in contenido)   # -> False   sin líneas en blanco
```
</details>


**4.4.** Lee un CSV y devuelve solo las filas cuya segunda columna supere un valor dado.
<details><summary>Solución</summary>

```python
import csv


def filtrar(ruta: str, minimo: int) -> list[tuple[str, int]]:
    """Filas cuya segunda columna supera el mínimo."""
    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector, None)
        return [(fila[0], int(fila[1])) for fila in lector
                if fila and int(fila[1]) > minimo]


with open("s.csv", "w", newline="", encoding="utf-8") as f:
    e = csv.writer(f)
    e.writerow(["nombre", "cantidad"])
    e.writerows([["Camisa", 10], ["Gorra", 3], ["Botas", 25]])

print(filtrar("s.csv", 5))   # -> [('Camisa', 10), ('Botas', 25)]
```
</details>


### Tema 5 · JSON

**5.1.** Guarda un diccionario en JSON legible y con tildes, y vuelve a cargarlo.
<details><summary>Solución</summary>

```python
import json

datos = {"nombre": "Ada Lovelace", "ciudad": "Londres", "años": 36}

with open("persona.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

with open("persona.json", encoding="utf-8") as f:
    print(json.load(f))   # -> {'nombre': 'Ada Lovelace', 'ciudad': 'Londres', 'años': 36}
```
</details>

**5.2.** Comprueba qué pasa **sin** `ensure_ascii=False` y qué pasa **sin** `indent=2`.
<details><summary>Solución</summary>

```python
import json

print(json.dumps({"año": 2026}))                     # -> {"a\u00f1o": 2026}
print(json.dumps({"año": 2026}, ensure_ascii=False))  # -> {"año": 2026}

print(json.dumps({"a": 1, "b": 2}))                  # -> {"a": 1, "b": 2}
print(json.dumps({"a": 1, "b": 2}, indent=2))        # en varias líneas, legible

# Los dos ficheros son JSON válido: la diferencia es que uno lo puede leer
# una persona y el otro no.
```
</details>

**5.3.** ¿Cuándo usarías CSV y cuándo JSON? Da un ejemplo de cada uno.
<details><summary>Solución</summary>

```text
CSV  -> datos TABULARES: muchas filas, siempre las mismas columnas.
        Ejemplo: el listado de ventas del mes, las notas de un grupo.
        Se abre en Excel y lo entiende cualquiera.

JSON -> datos con ESTRUCTURA: cosas dentro de cosas, campos opcionales.
        Ejemplo: la configuracion de una aplicacion, la respuesta de una API,
        una ficha con listas dentro.

Regla practica: si lo puedes dibujar como una tabla, CSV.
Si tiene forma de arbol, JSON.
```
</details>


**5.4.** Guarda una **lista de diccionarios** en JSON y vuelve a cargarla, comprobando que es exactamente la misma.
<details><summary>Solución</summary>

```python
import json

alumnos = [{"nombre": "Ada", "nota": 9.5}, {"nombre": "Alan", "nota": 8.0}]

with open("alumnos.json", "w", encoding="utf-8") as f:
    json.dump(alumnos, f, indent=2, ensure_ascii=False)

with open("alumnos.json", encoding="utf-8") as f:
    leidos = json.load(f)

print(leidos == alumnos)   # -> True
print(leidos[0]["nombre"])  # -> Ada

# JSON no solo guarda diccionarios: también listas, y listas de diccionarios.
```
</details>


### Actividades guiadas

#### Actividad 1 — Escribir un fichero
Guarda tres nombres, uno por línea, en `nombres.txt`.
<details><summary>Solución</summary>

```python
nombres: list[str] = ["Ada", "Linus", "Grace"]
with open("nombres.txt", "w", encoding="utf-8") as f:
    for n in nombres:
        f.write(n + "\n")
```
</details>

#### Actividad 2 — Leerlo y contarlo
Lee `nombres.txt` y muestra cuántas líneas tiene.
<details><summary>Solución</summary>

```python
with open("nombres.txt", encoding="utf-8") as f:
    lineas = [ln.rstrip() for ln in f]
print(f"{len(lineas)} nombres")
```
</details>

#### Actividad 3 — Tabla con formato
Muestra una lista de productos en columnas alineadas.
<details><summary>Solución</summary>

```python
productos = [("Camisa", 19.99), ("Gorra", 8.0)]
print(f"{'PRODUCTO':<12}{'PRECIO':>10}")
for nombre, precio in productos:
    print(f"{nombre:<12}{precio:>10.2f}")
```
</details>

#### Actividad 4 — CSV de ida y vuelta
Guarda dos contactos en CSV y vuelve a leerlos.
<details><summary>Solución</summary>

```python
import csv

with open("contactos.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["nombre", "telefono"])
    w.writerow(["Ada", "600111222"])
    w.writerow(["Linus", "600333444"])

with open("contactos.csv", encoding="utf-8") as f:
    for fila in csv.DictReader(f):
        print(fila["nombre"], fila["telefono"])
```
</details>

### Ejercicios propuestos

**E1 ○ · Guardar una lista.** `guardar(ruta: str, lineas: list[str]) -> None`.
<details><summary>Solución</summary>

```python
def guardar(ruta: str, lineas: list[str]) -> None:
    with open(ruta, "w", encoding="utf-8") as f:
        for ln in lineas:
            f.write(ln + "\n")
```
</details>

**E2 ○ · Leer una lista.** `leer(ruta: str) -> list[str]`, devolviendo `[]` si no existe.
<details><summary>Solución</summary>

```python
def leer(ruta: str) -> list[str]:
    try:
        with open(ruta, encoding="utf-8") as f:
            return [ln.rstrip() for ln in f]
    except FileNotFoundError:
        return []
```
</details>

**E3 ◐ · Añadir al final.** `anadir(ruta: str, linea: str) -> None` sin borrar lo anterior.
<details><summary>Solución</summary>

```python
def anadir(ruta: str, linea: str) -> None:
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(linea + "\n")
```
</details>

**E4 ◐ · Contar líneas.** `contar_lineas(ruta: str) -> int` (0 si no existe).
<details><summary>Solución</summary>

```python
def contar_lineas(ruta: str) -> int:
    try:
        with open(ruta, encoding="utf-8") as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return 0
```
</details>

**E5 ● · Media desde CSV.** Lee un CSV con columna `nota` y devuelve la media.
<details><summary>Pista</summary>Recuerda que <code>fila["nota"]</code> es texto: conviértelo con <code>float()</code>.</details>
<details><summary>Solución</summary>

```python
import csv

def media_csv(ruta: str) -> float:
    notas: list[float] = []
    with open(ruta, encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            notas.append(float(fila["nota"]))
    if not notas:
        return 0.0
    return sum(notas) / len(notas)
```
</details>

**E6 ○ · Guardar una lista de líneas.** `guardar_lineas(ruta: str, lineas: list[str]) -> None` escribe cada texto en una línea del fichero.
<details><summary>Pista</summary>Un <code>for</code> dentro del <code>with</code>, y acuérdate del <code>\n</code> al final de cada línea.</details>
<details><summary>Solución</summary>

```python
def guardar_lineas(ruta: str, lineas: list[str]) -> None:
    """Escribe cada texto en una línea del fichero."""
    with open(ruta, "w", encoding="utf-8") as f:
        for linea in lineas:
            f.write(linea + "\n")
```
</details>

**E7 ◐ · Configuración con valores por defecto.** `cargar_config(ruta: str) -> dict` lee un JSON de configuración. Si el fichero **no existe**, devuelve `{"idioma": "es", "tema": "claro"}`.
<details><summary>Pista</summary>Captura <code>FileNotFoundError</code> y devuelve ahí el diccionario por defecto.</details>
<details><summary>Solución</summary>

```python
import json

POR_DEFECTO: dict = {"idioma": "es", "tema": "claro"}


def cargar_config(ruta: str) -> dict:
    """Configuración del fichero; los valores por defecto si no existe."""
    try:
        with open(ruta, encoding="utf-8") as f:
            return dict(json.load(f))
    except FileNotFoundError:
        return dict(POR_DEFECTO)
```
</details>

**E8 ● · Añadir una fila a un CSV.** `anadir_fila(ruta: str, fila: list) -> None` añade una fila al CSV. Si el fichero **no existe todavía**, lo crea escribiendo antes la cabecera `nombre,nota`.
<details><summary>Pista</summary><code>os.path.exists(ruta)</code> te dice si hay que escribir la cabecera. Abre en modo <code>"a"</code> y no olvides <code>newline=""</code>.</details>
<details><summary>Solución</summary>

```python
import csv
import os

CABECERA: list[str] = ["nombre", "nota"]


def anadir_fila(ruta: str, fila: list) -> None:
    """Añade una fila al CSV, creándolo con cabecera si no existía."""
    nuevo: bool = not os.path.exists(ruta)
    with open(ruta, "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        if nuevo:
            escritor.writerow(CABECERA)
        escritor.writerow(fila)
```
</details>

---

---

## 8. Práctica tipo examen

Los ejercicios de arriba tienen la solución a la vista. Lo que viene
ahora **no**: aquí se comprueba si sabes hacerlo solo, que es lo que mide el examen.

Son dos escalones, y en este orden:

| | Qué es | Cómo sabes si va bien |
|---|---|---|
| **Proyecto de la unidad** | Un proyecto Python completo, para trabajar con calma | Sus tests, que ejecutas tú |
| **Simulacro** | Mismo formato, tamaño y rúbrica que el examen, contrarreloj | Sus tests, y la tabla de apartados |

---

## 9. Proyecto de la unidad

Toda la práctica de esta unidad se hace sobre un **proyecto base**: una agenda que guarda y recupera datos en CSV y JSON. Está montado
con la estructura real de un proyecto Python y trae una **batería de tests** que puedes
ejecutar en cualquier momento para ver si va todo bien.

**[Proyecto Agenda de contactos →](../proyectos/ud5/README.md)**

```
proyecto-ud5/
├── src/      ← tu código (funciones con TODO)
└── tests/    ← 10 tests que comprueban tu trabajo
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

## 10. Simulacro de examen

Cuando tengas el proyecto terminado, mídete: el **simulacro** es un examen de mentira con
**el mismo formato, tamaño y rúbrica** que el de verdad — y con los tests publicados.

**[Simulacro RA5 · Recetario en CSV y JSON →](../simulacros/ra5/README.md)** · 13 tests · 45–50 min

Hazlo **contrarreloj y sin ayuda**, como si fuera el examen. Al terminar, aplica la rúbrica
y tendrás una estimación bastante fiel de tu nota.

!!! warning "El examen de verdad va sin tests"
    Allí solo tendrás los **docstrings** y unos ejemplos. Por eso, en el simulacro, intenta
    resolver cada función leyendo solo su docstring y mira el test únicamente cuando falle.

---

---

## 11. Retos opcionales

- **R1.** Programa que lea un CSV de notas y escriba otro CSV añadiendo la columna `apto`.
- **R2.** Registro (log): función que añada una línea con fecha y hora usando `datetime`.
- **R3.** Convierte un CSV a JSON y comprueba que al volver atrás obtienes lo mismo.

- **R4.** Programa que lea un fichero de texto y escriba otro con las líneas numeradas.
- **R5.** Diario: función que añada una entrada al final de un fichero con la fecha y la hora delante, usando `datetime`.
- **R6.** Lee un CSV de productos y escribe un JSON con el mismo contenido; comprueba que al volver del JSON al CSV obtienes exactamente el fichero de partida.
---

---

## 12. Autoevaluación rápida

<details><summary>1. ¿Por qué usar <code>with open(...)</code>?</summary>Cierra el fichero automáticamente, incluso si hay un error.</details>
<details><summary>2. Diferencia entre los modos <code>"w"</code> y <code>"a"</code>.</summary><code>"w"</code> borra el contenido; <code>"a"</code> añade al final.</details>
<details><summary>3. ¿Qué excepción salta si el fichero no existe?</summary><code>FileNotFoundError</code>.</details>
<details><summary>4. ¿Por qué <code>newline=""</code> al abrir un CSV?</summary>Para que no aparezcan líneas en blanco entre filas.</details>
<details><summary>5. ¿De qué tipo son los datos leídos de un CSV?</summary>Texto (<code>str</code>): hay que convertirlos.</details>
<details><summary>6. ¿Cuándo JSON en vez de CSV?</summary>Cuando los datos tienen estructura anidada, no forma de tabla.</details>

---

---

## 13. Glosario

| Término | Definición |
|---|---|
| **Fichero de texto** | Archivo con caracteres legibles. |
| **Modo de apertura** | `r` leer, `w` escribir, `a` añadir, `x` crear. |
| **`with`** | Bloque que cierra el recurso automáticamente. |
| **Encoding** | Cómo se codifican los caracteres (`utf-8`). |
| **CSV** | Texto con valores separados por comas: una tabla. |
| **JSON** | Formato de datos estructurados y anidados. |
| **Persistencia** | Que los datos sobrevivan al cierre del programa. |

---

---

## 14. Cómo se evalúa esta unidad (RA5)

El examen es **100 % práctico**: se entrega un proyecto con las funciones vacías y una
especificación, y hay que escribir el código.

**La nota sale solo de los casos de prueba.** No hay puntos por presentación ni por
esfuerzo: cada apartado del examen vale en proporción a los casos que tiene, de modo que
**todos los casos valen lo mismo**.

`nota del apartado = (casos superados ÷ casos del apartado) × puntos del apartado`

`nota del examen = suma de los apartados`

### Así es el examen

**Inventario en CSV y JSON** · entrega `src/inventario.py` · **50 min**

| # | Apartado | Casos | Puntos |
|:---:|---|:---:|:---:|
| **A** | Formato de salida | 1 | **0,83** |
| **B** | Ficheros CSV | 7 | **5,83** |
| **C** | Ficheros JSON | 4 | **3,34** |
| | **TOTAL** | **12** | **10,00** |

Esta tabla viene en el enunciado, así que sabes desde el primer minuto **qué vale cada
parte** y por dónde empezar si vas justo de tiempo.

!!! warning "El examen se reparte sin tests"
    La carpeta `tests/` viene vacía. La especificación son los **docstrings** de cada
    función y los ejemplos del enunciado. Por eso conviene que en el simulacro te
    acostumbres a resolver leyendo el docstring y no el test.

### Así se corrige

Alguien que entrega el examen con **9 de los 12 casos** superados
—se le ha escapado el apartado **B**, donde falla 3 de
7 casos—:

| # | Apartado | Casos superados | Puntos |
|:---:|---|:---:|---|
| A | Formato de salida | 1 / 1 | 0,83 / 0,83 |
| B | Ficheros CSV | 4 / 7 | 3,33 / 5,83  ← |
| C | Ficheros JSON | 4 / 4 | 3,34 / 3,34 |
| | | | **NOTA: 7,50** |

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
