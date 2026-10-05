# Unidad 1 · Estructura del programa y elementos del lenguaje

> **Módulo:** CMO-313 · Fundamentos de programación
> **Resultado de aprendizaje:** RA1 · **Duración:** 8 h · **Peso:** 15 %
> **Examen:** test de código (primer trimestre)

Al final de esta unidad vas a tener esto funcionando en tu ordenador:

```text
Producto: Camisa
Unidades: 3
Precio:   19.95

Base            59.85
IVA (21%)       12.57
-------------------
TOTAL           72.42
```

Un programa que pregunta, calcula y presenta un resultado con buen aspecto. **No es un
ejemplo de juguete**: es exactamente el tipo de programa que se escribe en una empresa el
primer día, y contiene todas las piezas del lenguaje que necesitas para lo que viene
después.

Lo vamos a construir **poco a poco, en seis pasos**. Cada sección añade una pieza y termina
con el programa un poco más completo que antes.

---

## Mapa de la unidad

<figure markdown>
  ![Mapa de la unidad](../assets/diagramas/ud1-mapa.svg#only-light)
  ![Mapa de la unidad](../assets/diagramas/ud1-mapa-dark.svg#only-dark)
  <figcaption>Del problema al programa, y las piezas del lenguaje que intervienen.</figcaption>
</figure>

### Los seis pasos

| # | Qué añades | Con qué acaba el programa |
|:---:|---|---|
| **1** | La estructura de todo programa | Saluda y muestra un mensaje |
| **2** | Variables para guardar datos | Guarda producto, unidades y precio |
| **3** | Operadores para calcular | Calcula la base y el IVA |
| **4** | Leer datos del teclado | Pregunta los datos al usuario |
| **5** | Mostrar con formato | Presenta el ticket alineado |
| **6** | Constantes y comentarios | Queda limpio y legible |

### Antes de empezar

Necesitas **Python y VS Code instalados y un entorno virtual creado**. Eso se monta en la
sesión 2, en clase y entre todos, y está explicado paso a paso en
**[Puesta en marcha](../recursos/puesta-en-marcha.md)**.

!!! tip "Cómo leer esta unidad"
    **Con el editor abierto al lado.** Cada ejemplo está pensado para copiarlo y ejecutarlo.
    Leer código sin ejecutarlo no sirve de nada: el ordenador hace cosas que no esperas, y
    esa sorpresa es la que enseña.

    Los ejercicios están **todos juntos al final**, agrupados por tema y con su solución.
    Haz los de un tema en cuanto termines de leerlo.

---

## 1. Tu primer programa

Programar es **escribir instrucciones precisas para que un ordenador resuelva un
problema**. El ordenador no entiende ni improvisa: hace exactamente lo que le dices, en el
orden que se lo dices.

Esa literalidad es la primera lección del curso. **La mayoría de los errores no son del
ordenador: son instrucciones nuestras que no decían lo que creíamos.**

> **Analogía.** Un programa es una **receta de cocina**. Los *datos* son los ingredientes,
> el *algoritmo* son los pasos («bate dos huevos, añade harina…») y el *programa* es esa
> receta escrita en un idioma que la cocina entiende.

### 1.1 Todo programa tiene tres bloques

<figure markdown>
  ![Entrada, proceso, salida](../assets/diagramas/ud1-eps.svg#only-light)
  ![Entrada, proceso, salida](../assets/diagramas/ud1-eps-dark.svg#only-dark)
  <figcaption>Entrada, proceso y salida: la estructura de cualquier programa.</figcaption>
</figure>

| Bloque | Qué hace | En nuestro ticket |
|---|---|---|
| **Entrada** | Recoge los datos | producto, unidades, precio |
| **Proceso** | Los transforma | calcula base, IVA y total |
| **Salida** | Muestra el resultado | imprime el ticket |

Reconocer estos tres bloques en un problema es lo primero que hay que hacer, **antes de
escribir código**. Si no sabes cuáles son las entradas y cuál es la salida, no sabes qué
programa tienes que escribir.

### 1.2 El programa más pequeño que funciona

Crea un fichero `ticket.py` y escribe esto:

```python
print("Ticket de compra")
```

Ejecútalo:

```bash
python ticket.py
```

```text
Ticket de compra
```

Ya está: **ese es un programa**. `print()` es la instrucción que muestra algo por pantalla,
y el texto va entre comillas.

### 1.3 Un ejemplo resuelto, línea a línea

Vamos a marcar los tres bloques con comentarios, para verlos:

```python
# ── Entrada ──
producto = "Camisa"

# ── Proceso ──
mensaje = "Has elegido: " + producto

# ── Salida ──
print(mensaje)
```

```text
Has elegido: Camisa
```

Tres líneas de código y los tres bloques identificados. Fíjate en que:

- **El orden importa.** Si pones el `print` arriba, el programa falla: todavía no existe
  `mensaje`.
- El `+` entre textos los **pega** (se llama *concatenar*).
- Lo que empieza por `#` es un **comentario**: Python lo ignora. Es para quien lee.

### 1.4 Compilado o interpretado

| | **Compilado** | **Interpretado** |
|---|---|---|
| Cómo funciona | Traduce **todo** antes de ejecutar | Ejecuta **línea a línea** |
| Ejemplos | C, C++, Rust | **Python**, JavaScript |
| Ventaja | Muy rápido al ejecutarse | Flexible, rápido de probar |

Usamos **Python 3**: interpretado, de sintaxis limpia y con una comunidad enorme. Que sea
interpretado tiene una consecuencia práctica muy útil: **puedes probar una línea y ver
inmediatamente qué hace**.

!!! success "Lo que ya sabes hacer"
    Escribir y ejecutar un programa, mostrar texto por pantalla y reconocer los tres
    bloques de cualquier problema. Ejercicios del **tema 1**, al final de la unidad.

---

## 2. Variables: guardar datos

Una **variable** es un nombre que apunta a un valor. Guarda algo para usarlo después.

> **Analogía.** Una variable es una **etiqueta pegada a una caja**. La etiqueta es el
> nombre (`precio`) y dentro está el valor (`19.95`). Puedes cambiar el contenido de la
> caja sin cambiar la etiqueta.

### 2.1 Crear y usar variables

```python
producto = "Camisa"
unidades = 3
precio = 19.95

print(producto, unidades, precio)
```

```text
Camisa 3 19.95
```

El signo `=` **no** es «igual» en sentido matemático: significa «guarda a la derecha en el
nombre de la izquierda». Se lee de derecha a izquierda.

### 2.2 Los cuatro tipos básicos

| Tipo | Qué guarda | Ejemplo |
|---|---|---|
| `str` | texto (*string*) | `"Camisa"` |
| `int` | número entero | `3` |
| `float` | número con decimales | `19.95` |
| `bool` | verdadero o falso | `True`, `False` |

El tipo **no se declara**: Python lo deduce del valor. Puedes verlo con `type()`:

```python
print(type("Camisa"))   # <class 'str'>
print(type(3))          # <class 'int'>
print(type(19.95))      # <class 'float'>
print(type(True))       # <class 'bool'>
```

<figure markdown>
  ![Variables en memoria](../assets/diagramas/ud1-memoria.svg#only-light)
  ![Variables en memoria](../assets/diagramas/ud1-memoria-dark.svg#only-dark)
  <figcaption>Cada variable es un nombre que apunta a un valor guardado en memoria.</figcaption>
</figure>

### 2.3 Un ejemplo resuelto: reasignar

```python
precio = 19.95
print(precio)        # 19.95

precio = 24.50       # la misma etiqueta, otro valor
print(precio)        # 24.5

print(type(precio))  # <class 'float'>
```

Dos cosas que sorprenden la primera vez:

- `24.50` se muestra como `24.5`. Python no guarda los ceros de adorno; en la sección 5
  veremos cómo mostrarlo con dos decimales.
- El valor anterior **se pierde**. Si lo necesitas, guárdalo en otra variable antes.

### 2.4 Anotar el tipo (y por qué conviene)

En este módulo escribimos el tipo de cada variable. No es obligatorio para Python, pero es
como se trabaja en cualquier empresa:

```python
producto: str = "Camisa"
unidades: int = 3
precio: float = 19.95
```

Eso `: str`, `: int`, `: float` son **anotaciones de tipo**. Python **las ignora al
ejecutar**: sirven para documentar y para que una herramienta llamada `mypy` compruebe que
todo cuadra sin tener que ejecutar el programa. Está explicado en
[Puesta en marcha](../recursos/puesta-en-marcha.md#6-las-anotaciones-de-tipo-y-mypy).

!!! warning "Anotar no valida"
    Esto **no da error** al ejecutar, aunque sea una mentira evidente:

    ```python
    edad: int = "veinte"      # Python no protesta
    ```

    Quien protesta es `mypy`. Python confía en ti.

!!! success "Lo que ya sabes hacer"
    Guardar los datos del ticket en variables con su tipo anotado. Ejercicios del
    **tema 2**.

---

## 3. Operadores: calcular

Ya tienes los datos guardados. Ahora hay que **hacer cuentas** con ellos.

### 3.1 Aritméticos

| Operador | Qué hace | Ejemplo | Resultado |
|:---:|---|---|---|
| `+` `-` `*` | suma, resta, multiplicación | `3 * 19.95` | `59.85` |
| `/` | división, **siempre decimal** | `7 / 2` | `3.5` |
| `//` | división **entera** | `7 // 2` | `3` |
| `%` | **resto** de la división | `7 % 2` | `1` |
| `**` | potencia | `2 ** 3` | `8` |

Los dos que más cuesta interiorizar son `//` y `%`, y son utilísimos:

```python
segundos = 3725

minutos = segundos // 60      # 62   ¿cuántos minutos enteros caben?
sobran = segundos % 60        # 5    ¿qué se queda fuera?

print(minutos, sobran)
```

```text
62 5
```

!!! warning "`/` siempre devuelve decimal"
    ```python
    print(6 / 3)          # 2.0   ¡con decimal, aunque sea exacto!
    print(type(6 / 3))    # <class 'float'>
    print(6 // 3)         # 2     este sí es entero
    ```

### 3.2 Comparar y combinar

| Operador | Qué pregunta |
|:---:|---|
| `==` `!=` | ¿son iguales? ¿son distintos? |
| `<` `>` `<=` `>=` | ¿menor? ¿mayor? |
| `and` | ¿se cumplen **las dos**? |
| `or` | ¿se cumple **alguna**? |
| `not` | lo contrario |

El resultado de una comparación es un `bool`:

```python
unidades = 3
print(unidades > 0)              # True
print(unidades > 0 and unidades < 10)   # True
```

!!! danger "`=` no es `==`"
    `=` **guarda** un valor. `==` **compara**. Confundirlos es el error de sintaxis más
    repetido del curso.

### 3.3 Precedencia: el orden de las operaciones

Python respeta el orden matemático de siempre: primero `**`, después `*` `/` `//` `%`, y al
final `+` `-`.

```python
print(10 - 2 ** 3)        # 2     la potencia primero: 10 - 8
print((10 - 2) ** 3)      # 512   los paréntesis mandan
```

<figure markdown>
  ![Precedencia de operadores](../assets/diagramas/ud1-precedencia.svg#only-light)
  ![Precedencia de operadores](../assets/diagramas/ud1-precedencia-dark.svg#only-dark)
  <figcaption>De arriba abajo: lo de arriba se evalúa antes.</figcaption>
</figure>

!!! tip "Usa paréntesis aunque no hagan falta"
    `base + base * 0.21` funciona, pero `base + (base * 0.21)` se lee mejor. El código lo
    vas a leer mucha más veces de las que lo escribes.

### 3.4 Un ejemplo resuelto: el ticket calcula

```python
producto: str = "Camisa"
unidades: int = 3
precio: float = 19.95

base: float = unidades * precio
iva: float = base * 21 / 100
total: float = base + iva

print(producto, unidades, precio)
print(base, iva, total)
```

```text
Camisa 3 19.95
59.849999999999994 12.568499999999998 72.4185
```

Funciona… pero esos decimales son horribles. **Eso no es un error tuyo**: es como el
ordenador guarda los números con decimales. Lo arreglamos en la sección 5, dándole formato
a la salida.

!!! success "Lo que ya sabes hacer"
    Calcular la base, el IVA y el total. Ejercicios del **tema 3**.

---

## 4. Leer datos del teclado

Hasta ahora los datos estaban escritos en el código. Un programa de verdad **los pregunta**.

### 4.1 `input()`

```python
producto = input("Producto: ")
print("Has elegido:", producto)
```

```text
Producto: Camisa
Has elegido: Camisa
```

El texto entre paréntesis es la pregunta que ve el usuario.

### 4.2 La trampa: `input()` SIEMPRE devuelve texto

Aquí falla casi todo el mundo la primera vez:

```python
unidades = input("Unidades: ")      # el usuario escribe 3
print(unidades + 1)
```

```text
Unidades: 3
TypeError: can only concatenate str (not "int") to str
```

Python no se ha equivocado. `unidades` **no vale 3**, vale `"3"`, que es el **texto** tres.
Y a un texto no se le puede sumar un número.

!!! danger "El error más repetido del curso"
    Todo lo que llega de `input()` es `str`. **Si vas a calcular con él, hay que
    convertirlo.**

### 4.3 Convertir: `int()` y `float()`

| Función | Convierte a | Ejemplo |
|---|---|---|
| `int(x)` | entero | `int("3")` → `3` |
| `float(x)` | decimal | `float("19.95")` → `19.95` |
| `str(x)` | texto | `str(3)` → `"3"` |

```python
unidades = int(input("Unidades: "))     # convertido al leerlo
print(unidades + 1)
```

```text
Unidades: 3
4
```

Dos comportamientos que conviene conocer:

```python
print(int(9.99))        # 9    int() TRUNCA, no redondea
print(round(9.99))      # 10   round() sí redondea
print(int("3.5"))       # ValueError: no puede con el punto
print(float("3.5"))     # 3.5  este sí
```

!!! tip "Convierte al leer, no al calcular"
    ```python
    unidades = int(input("Unidades: "))     # bien: ya es número
    ```
    Mejor que dejarlo en texto y convertirlo en cada cuenta. Un dato mal tipado se propaga
    por todo el programa.

### 4.4 Un ejemplo resuelto: el ticket pregunta

```python
producto: str = input("Producto: ")
unidades: int = int(input("Unidades: "))
precio: float = float(input("Precio:   "))

base: float = unidades * precio
iva: float = base * 21 / 100
total: float = base + iva

print(base, iva, total)
```

```text
Producto: Camisa
Unidades: 3
Precio:   19.95
59.849999999999994 12.568499999999998 72.4185
```

!!! success "Lo que ya sabes hacer"
    Un programa que pregunta los datos y calcula con ellos. Ejercicios del **tema 4**.

---

## 5. Mostrar el resultado con formato

Solo falta que el ticket tenga buen aspecto. Y esto no es cosmética: **en los exámenes la
salida se compara carácter a carácter**, así que el formato exacto es parte del ejercicio.

### 5.1 f-strings

Una **f-string** es un texto que empieza por `f` y puede llevar variables entre llaves:

```python
producto = "Camisa"
unidades = 3

print(f"{unidades} x {producto}")
```

```text
3 x Camisa
```

Es más corto y más legible que ir pegando trozos con `+`, y no hay que convertir nada a
texto.

### 5.2 Decimales: `:.2f`

Detrás de la variable, dos puntos y el formato:

```python
total = 72.4185

print(f"{total:.2f}")      # 72.42
```

`:.2f` significa «decimal con **2** cifras después del punto». Es el formato del dinero, y
lo vas a usar constantemente.

### 5.3 Alinear en columnas

| Formato | Qué hace |
|---|---|
| `:<12` | alinea a la **izquierda** en 12 caracteres |
| `:>8` | alinea a la **derecha** en 8 |
| `:^10` | **centra** en 10 |
| `:>8.2f` | derecha, 8 de ancho, 2 decimales |
| `:,` | separador de miles |

```python
print(f"{'Base':<12}{59.85:>8.2f}")
print(f"{'IVA (21%)':<12}{12.5685:>8.2f}")
```

```text
Base           59.85
IVA (21%)      12.57
```

!!! tip "Los números, a la derecha"
    Alineados a la derecha las unidades quedan una debajo de otra y la tabla se lee de un
    vistazo. Ese es el detalle que separa una salida profesional de una improvisada.

### 5.4 Un ejemplo resuelto: el ticket terminado

```python
producto: str = input("Producto: ")
unidades: int = int(input("Unidades: "))
precio: float = float(input("Precio:   "))

base: float = unidades * precio
iva: float = base * 21 / 100
total: float = base + iva

print()
print(f"{'Base':<12}{base:>8.2f}")
print(f"{'IVA (21%)':<12}{iva:>8.2f}")
print("-" * 20)
print(f"{'TOTAL':<12}{total:>8.2f}")
```

```text
Producto: Camisa
Unidades: 3
Precio:   19.95

Base           59.85
IVA (21%)      12.57
--------------------
TOTAL          72.42
```

**Ese es el programa del principio de la unidad**, y lo has construido tú en cinco pasos.

!!! success "Lo que ya sabes hacer"
    Presentar resultados con el formato exacto que se pide. Ejercicios del **tema 5**.

---

## 6. Dejarlo limpio: constantes, nombres y comentarios

El programa funciona. Ahora hay que dejarlo de forma que **dentro de un mes lo entiendas**
—o que lo entienda quien lo herede—. Esto no es un adorno: es la diferencia entre código
que se puede mantener y código que se tira.

### 6.1 Constantes

El `21` de nuestro programa es el IVA. Aparece suelto en medio de un cálculo y no dice qué
es. Eso se llama **número mágico** y es un problema: si mañana cambia el IVA, hay que ir a
buscarlo.

Una **constante** es un valor con nombre que no cambia. Por convenio se escribe en
MAYÚSCULAS:

```python
IVA: int = 21

iva = base * IVA / 100
```

Ahora se lee, y si cambia se toca **en un solo sitio**.

!!! note "En Python es un acuerdo, no una regla"
    Python te deja cambiar una constante; nadie te lo impide. Las MAYÚSCULAS son una señal
    para quien lee el código: «esto no se toca».

### 6.2 Nombres

| Regla | Bien | Mal |
|---|---|---|
| Empieza por letra o `_` | `precio`, `_tmp` | `2dias` |
| Solo letras, números y `_` | `precio_final` | `precio-final` |
| No usar palabras reservadas | `grupo` | `class`, `for`, `if` |
| `snake_case`, en minúsculas | `precio_unidad` | `PrecioUnidad` |
| Que **diga qué es** | `unidades` | `x`, `dato`, `a2` |

La última es la importante. `precio_unidad` no cuesta más de escribir que `p` y te ahorra
diez minutos de releer dentro de dos semanas.

### 6.3 Comentarios

```python
# Un comentario de una línea

"""
Varias líneas, normalmente al principio
del fichero para explicar de qué va.
"""
```

Un comentario bueno explica **el porqué**, no el qué:

```python
precio = precio * 1.21     # ✗ multiplica por 1.21   (eso ya se ve)
precio = precio * 1.21     # ✓ IVA general vigente en 2026
```

Cuando un comentario repite el código, sobra. Cuando explica una decisión, vale oro.

### 6.4 El programa terminado

```python
"""Ticket de compra con IVA."""

IVA: int = 21          # tipo general vigente

# ── Entrada ──
producto: str = input("Producto: ")
unidades: int = int(input("Unidades: "))
precio: float = float(input("Precio:   "))

# ── Proceso ──
base: float = unidades * precio
iva: float = base * IVA / 100
total: float = base + iva

# ── Salida ──
print()
print(f"{'Base':<12}{base:>8.2f}")
print(f"{'IVA (' + str(IVA) + '%)':<12}{iva:>8.2f}")
print("-" * 20)
print(f"{'TOTAL':<12}{total:>8.2f}")
```

Compáralo con el `print("Ticket de compra")` de la sección 1. Mismo programa, seis pasos.

!!! success "Lo que ya sabes hacer"
    Todo el RA1. Ejercicios del **tema 6**, y después el bloque de ejercicios largos y el
    simulacro.

---

## 7. Errores frecuentes

Ten esta tabla a mano: casi todos los fallos de esta unidad están aquí.

| Lo que ves | Qué significa | Cómo se arregla |
|---|---|---|
| `SyntaxError: invalid syntax` | Falta algo: un paréntesis, una comilla, los dos puntos | Mirar **la línea anterior** a la que señala |
| `NameError: name 'x' is not defined` | Usas una variable que no existe (o mal escrita) | Comprobar que se crea **antes** de usarla |
| `TypeError: can only concatenate str...` | Mezclas texto y número | Convertir con `int()` o `float()` |
| `ValueError: invalid literal for int()` | `int()` con algo que no es un número entero | Comprobar lo que escribe el usuario |
| `ZeroDivisionError` | División entre cero | Comprobar el divisor antes |
| `IndentationError` | Espacios de más o de menos al principio de la línea | Usar siempre 4 espacios, sin mezclar tabuladores |
| Sale `2.0` donde esperabas `2` | Has usado `/`, que siempre da decimal | Usar `//` si quieres entero |
| Sale `59.849999999999994` | Así guarda el ordenador los decimales | Dar formato con `:.2f` al mostrarlo |

!!! tip "Lee el error de abajo arriba"
    Python te dice al final **qué** ha pasado y justo encima **dónde**. Con esas dos líneas
    se resuelve la mayoría de los fallos, sin tocar nada más.

---

## 8. Ejercicios
Aquí están **todos los ejercicios de la unidad**, agrupados por el
tema al que corresponden y con la solución desplegable.

**Haz los de un tema en cuanto termines de leerlo.** Son cortos y solo usan lo que acabas
de ver, así que si algo no ha quedado claro lo descubres en el momento.

!!! warning "Intenta antes de desplegar"
    Abrir la solución sin haberlo intentado da sensación de aprender, y no enseña nada. Si
    llevas quince minutos sin avanzar, mírala. Si llevas dos, no.

### Tema 1 · Tu primer programa
**1.1.** Descompón en **entrada, proceso y salida** el cálculo del área de un rectángulo. No escribas código todavía: solo los tres bloques.
<details><summary>Solución</summary>

```text
Entrada:  base y altura (los pide el usuario)
Proceso:  area = base * altura
Salida:   mostrar el area por pantalla
```
</details>

**1.2.** Escribe en lenguaje natural el algoritmo para decidir si un número es **par**.
<details><summary>Solución</summary>

```text
1. Pedir un numero
2. Calcular el resto de dividirlo entre 2
3. Si el resto es 0 -> es par
4. Si no -> es impar
5. Mostrar el resultado
```
</details>

**1.3.** Ordena estos pasos del ciclo de desarrollo: *ejecutar*, *analizar el problema*, *escribir el código*, *corregir errores*, *diseñar el algoritmo*.
<details><summary>Solución</summary>

```text
1. Analizar el problema  (que me piden exactamente)
2. Disenar el algoritmo   (como lo resuelvo, en lenguaje natural)
3. Escribir el codigo     (traducirlo a Python)
4. Ejecutar               (probarlo de verdad)
5. Corregir errores       (y volver a ejecutar)
```
</details>

**1.4.** Escribe un programa con la estructura **entrada → proceso → salida** que pida el nombre del usuario y lo salude.
<details><summary>Solución</summary>

```python
# Entrada
nombre: str = input("¿Cómo te llamas? ")

# Proceso
saludo: str = f"¡Hola, {nombre}!"

# Salida
print(saludo)   # -> ¡Hola, Ada!
```
</details>

**1.5.** Pide dos números enteros y muestra su suma. Marca con comentarios dónde está cada bloque del ciclo.
<details><summary>Solución</summary>

```python
# Entrada
a: int = int(input("Primer número: "))
b: int = int(input("Segundo número: "))

# Proceso
suma: int = a + b

# Salida
print(f"La suma es {suma}")   # -> La suma es 12
```
</details>

**1.6.** Este programa está todo mezclado. Reescríbelo separando los tres bloques:

```python
print(f"Doble: {int(input('Número: ')) * 2}")
```
<details><summary>Solución</summary>

```python
# Entrada
numero: int = int(input("Número: "))

# Proceso
doble: int = numero * 2

# Salida
print(f"Doble: {doble}")   # -> Doble: 42

# Hace lo mismo, pero ahora se lee, se prueba y se corrige por partes.
```
</details>

### Tema 2 · Variables y tipos
**2.1.** Crea cuatro variables, una de cada tipo básico (`str`, `int`, `float`, `bool`), y muestra su valor y su tipo.
<details><summary>Solución</summary>

```python
nombre = "Ada"
edad = 36
altura = 1.68
matriculada = True

print(nombre, type(nombre))         # -> <class 'str'>
print(edad, type(edad))             # -> <class 'int'>
print(altura, type(altura))         # -> <class 'float'>
print(matriculada, type(matriculada))  # -> <class 'bool'>
```
</details>

**2.2.** Tienes `a = 5` y `b = 9`. Intercambia sus valores y compruébalo.
<details><summary>Solución</summary>

```python
a = 5
b = 9

a, b = b, a   # Python permite el intercambio directo

print(a, b)   # -> 9 5
```
</details>

**2.3.** ¿Qué **tipo** devuelven `7 / 2`, `7 // 2` y `7 % 2`? Predícelo antes de ejecutar.
<details><summary>Solución</summary>

```python
print(7 / 2, type(7 / 2))     # -> 3.5 <class 'float'>
print(7 // 2, type(7 // 2))   # -> 3 <class 'int'>
print(7 % 2, type(7 % 2))     # -> 1 <class 'int'>

# La division / SIEMPRE da float, aunque el resultado sea exacto: 6 / 2 -> 3.0
```
</details>

**2.4.** Escribe una función **tipada** `area_rectangulo(base, altura)` que devuelva el área.
<details><summary>Solución</summary>

```python
def area_rectangulo(base: float, altura: float) -> float:
    """Área de un rectángulo."""
    return base * altura

print(area_rectangulo(3, 4.5))   # -> 13.5
```
</details>

**2.5.** Anota los tipos de estas variables y ejecuta `mypy` sobre el fichero:

```python
nombre = "Ada"
edad = 36
notas = [7.5, 8.0]
```
<details><summary>Solución</summary>

```python
nombre: str = "Ada"
edad: int = 36
notas: list[float] = [7.5, 8.0]

print(nombre, edad, notas)   # -> Ada 36 [7.5, 8.0]

# En la terminal:  mypy fichero.py   ->  Success: no issues found
```
</details>

**2.6.** Escribe `iniciales(nombre, apellido)` que devuelva las iniciales en mayúsculas, con sus anotaciones de tipo.
<details><summary>Solución</summary>

```python
def iniciales(nombre: str, apellido: str) -> str:
    """Devuelve las iniciales, en mayúsculas y separadas por punto."""
    return f"{nombre[0].upper()}.{apellido[0].upper()}."

print(iniciales("ada", "lovelace"))   # -> A.L.
```
</details>

### Tema 3 · Operadores
**3.1.** Sin ejecutar, ¿cuánto valen `10 - 2 ** 3`, `(10 - 2) ** 3` y `10 % 4 * 2`? Compruébalo después.
<details><summary>Solución</summary>

```python
print(10 - 2 ** 3)      # -> 2      la potencia va primero
print((10 - 2) ** 3)    # -> 512    los parentesis mandan
print(10 % 4 * 2)       # -> 4      % y * tienen la misma prioridad: de izquierda a derecha
```
</details>

**3.2.** Comprueba si una persona de 20 años con carnet puede alquilar un coche (mínimo 21 años **y** carnet).
<details><summary>Solución</summary>

```python
edad: int = 20
tiene_carnet: bool = True

puede: bool = edad >= 21 and tiene_carnet

print(puede)   # -> False
```
</details>

**3.3.** Convierte 3725 segundos a horas, minutos y segundos usando `//` y `%`.
<details><summary>Solución</summary>

```python
total: int = 3725

horas: int = total // 3600
resto: int = total % 3600
minutos: int = resto // 60
segundos: int = resto % 60

print(f"{horas}h {minutos}m {segundos}s")   # -> 1h 2m 5s
```
</details>

### Tema 4 · Leer y convertir
**4.1.** Este programa falla. ¿Por qué? Arréglalo:

```python
edad = input("Edad: ")
print(edad + 1)
```
<details><summary>Solución</summary>

```python
# input() SIEMPRE devuelve texto: "20" + 1 mezcla str con int y lanza TypeError
edad: int = int(input("Edad: "))
print(edad + 1)   # -> 21
```
</details>

**4.2.** ¿Qué hace `int(9.99)`? ¿Y `round(9.99)`? Comprueba la diferencia.
<details><summary>Solución</summary>

```python
print(int(9.99))     # -> 9    int() TRUNCA: se queda con la parte entera
print(round(9.99))   # -> 10   round() REDONDEA al mas cercano
print(int(-2.7))     # -> -2   ojo: trunca hacia cero, no hacia abajo
```
</details>

**4.3.** El usuario escribe los decimales con coma (`3,5`). Conviértelo a `float` sin que reviente.
<details><summary>Solución</summary>

```python
texto: str = "3,5"

# float("3,5") lanza ValueError: en Python el separador decimal es el punto
numero: float = float(texto.replace(",", "."))

print(numero)   # -> 3.5
```
</details>

### Tema 5 · Formato de salida
**5.1.** Muestra el número `3.14159` con **dos decimales** y el precio `1234.5` con dos decimales y separador de miles.
<details><summary>Solución</summary>

```python
pi: float = 3.14159
precio: float = 1234.5

print(f"{pi:.2f}")        # -> 3.14
print(f"{precio:,.2f}")   # -> 1,234.50
```
</details>

**5.2.** Muestra estos tres productos en columnas: el nombre alineado a la izquierda en 12 huecos y el precio a la derecha en 8, con dos decimales.
<details><summary>Solución</summary>

```python
productos = [("Camisa", 19.9), ("Pantalón", 34.5), ("Gorra", 7.25)]

for nombre, precio in productos:
    print(f"{nombre:<12}{precio:>8.2f}")

# Camisa         19.90
# Pantalón       34.50
# Gorra           7.25
```
</details>

**5.3.** Pide un importe por teclado y muéstralo formateado como `Total:    45.00 €`.
<details><summary>Solución</summary>

```python
importe: float = float(input("Importe: "))
print(f"Total: {importe:>8.2f} €")   # -> Total:    45.00 €
```
</details>

### Tema 6 · Constantes, nombres y comentarios
**6.1.** Define el IVA como **constante** y calcula el precio final de un artículo de 80 €.
<details><summary>Solución</summary>

```python
IVA: int = 21          # constante: en MAYÚSCULAS porque no cambia

precio: float = 80.0
final: float = precio * (1 + IVA / 100)

print(f"{final:.2f}")   # -> 96.80
```
</details>

**6.2.** ¿Cuáles de estos nombres son válidos como variable? `total`, `2pagos`, `precio-final`, `_temp`, `for`, `añoNacimiento`.
<details><summary>Solución</summary>

```text
Validos:    total, _temp, anoNacimiento
No validos: 2pagos        -> no puede empezar por numero
            precio-final  -> el guion es el operador resta; usa precio_final
            for           -> es una palabra reservada del lenguaje
```
</details>

**6.3.** Este código no funciona porque usa una palabra reservada. Arréglalo:

```python
class = "1DAW"
print(class)
```
<details><summary>Solución</summary>

```python
# 'class' esta reservada para declarar clases: hay que renombrar la variable
grupo: str = "1DAW"
print(grupo)   # -> 1DAW
```
</details>

**6.4.** Añade un **docstring** de una línea a esta función:

```python
def doble(n: int) -> int:
    return n * 2
```
<details><summary>Solución</summary>

```python
def doble(n: int) -> int:
    """Devuelve el doble del número recibido."""
    return n * 2

print(doble.__doc__)   # -> Devuelve el doble del número recibido.
```
</details>

**6.5.** Estos comentarios sobran porque repiten lo que ya dice el código. Sustitúyelos por uno que explique **el porqué**:

```python
# suma 1 a i
i = i + 1
# multiplica por 1.21
precio = precio * 1.21
```
<details><summary>Solución</summary>

```python
i = 0
precio = 100.0

i = i + 1                 # (sin comentario: el codigo ya se lee solo)
precio = precio * 1.21    # IVA general del 21 % vigente en 2026

print(i, round(precio, 2))   # -> 1 121.0
```
</details>

**6.6.** Documenta un módulo `conversiones.py` con su docstring de módulo y una función documentada.
<details><summary>Solución</summary>

```python
"""Conversiones entre unidades de longitud."""


def metros_a_km(metros: float) -> float:
    """Convierte metros a kilómetros."""
    return metros / 1000

print(metros_a_km(2500))   # -> 2.5
```
</details>

### Actividades guiadas

Las hacemos en clase, pero tienes la solución para repasarlas después.

#### Actividad 1 — Ficha de una persona
Crea variables **tipadas** `nombre`, `edad`, `altura` y muéstralas con su tipo.
<details><summary>Solución</summary>

```python
nombre: str = "Ada"
edad: int = 36
altura: float = 1.68
print(nombre, type(nombre))
print(edad, type(edad))
print(altura, type(altura))
```
</details>

#### Actividad 2 — Área del círculo (constantes y operadores)
Define `PI` como constante y calcula el área de un círculo de radio 5.
<details><summary>Solución</summary>

```python
PI: float = 3.14159
radio: int = 5
area: float = PI * radio ** 2
print(f"Área: {area:.2f}")   # Área: 78.54
```
</details>

#### Actividad 3 — Función tipada de operaciones
Escribe `operaciones(a: int, b: int) -> None` que muestre suma, división entera, resto y potencia.
<details><summary>Solución</summary>

```python
def operaciones(a: int, b: int) -> None:
    print("Suma:", a + b)
    print("División entera:", a // b)
    print("Resto:", a % b)
    print("Potencia:", a ** b)

operaciones(17, 5)   # 22 / 3 / 2 / 1419857
```
</details>

#### Actividad 4 — Conversión y entrada
Pide dos enteros por teclado y muestra su suma (recuerda convertir).
<details><summary>Solución</summary>

```python
n1: int = int(input("Primer número: "))
n2: int = int(input("Segundo número: "))
print(f"Suma: {n1 + n2}")
```
</details>

---

### Ejercicios propuestos

Trabajo autónomo. ○ básico · ◐ medio · ● avanzado. **Anota los tipos** en todas tus soluciones y pásales `mypy`.

!!! warning "Intenta antes de desplegar"
    Leer la solución sin haberlo intentado da sensación de aprender, pero no enseña. Usa primero la pista.

**E1 ○ · Celsius a Fahrenheit.** `F = C · 9/5 + 32`.
<details><summary>Pista</summary>Convierte la entrada con <code>float()</code>.</details>
<details><summary>Solución</summary>

```python
c: float = float(input("Grados Celsius: "))
f: float = c * 9 / 5 + 32
print(f"{c} °C = {f:.1f} °F")
```
</details>

**E2 ○ · Rectángulo.** Pide base y altura y muestra área y perímetro.
<details><summary>Solución</summary>

```python
base: float = float(input("Base: "))
altura: float = float(input("Altura: "))
print(f"Área: {base * altura:.2f}")
print(f"Perímetro: {2 * (base + altura):.2f}")
```
</details>

**E3 ◐ · Segundos a h:m:s.**
<details><summary>Pista</summary>Usa <code>//</code> y <code>%</code> con 3600 y 60.</details>
<details><summary>Solución</summary>

```python
total: int = int(input("Segundos: "))
horas: int = total // 3600
minutos: int = (total % 3600) // 60
seg: int = total % 60
print(f"{horas}h {minutos}m {seg}s")   # 3661 -> 1h 1m 1s
```
</details>

**E4 ◐ · Descuento.** `DESCUENTO = 15` (constante).
<details><summary>Solución</summary>

```python
DESCUENTO: int = 15
precio: float = float(input("Precio: "))
final: float = precio - precio * DESCUENTO / 100
print(f"Precio final: {final:.2f} €")
```
</details>

**E5 ◐ · Media de tres notas** con función tipada.
<details><summary>Solución</summary>

```python
def media(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3

print(f"Media: {media(5, 7, 9):.2f}")   # 7.00
```
</details>

**E6 ● · Cambio de monedas.** Importe en céntimos → monedas de 50, 20, 10, 5, 2, 1.
<details><summary>Pista</summary>Divide con <code>//</code> y guarda el resto con <code>%</code> para la siguiente moneda.</details>
<details><summary>Solución</summary>

```python
c: int = int(input("Céntimos: "))
for valor in (50, 20, 10, 5, 2, 1):
    print(f"{valor}c: {c // valor}")
    c = c % valor
```
*(Usa un `for`, que verás en la UD3; también vale repetir seis bloques.)*
</details>

**E7 ◐ · Línea de ticket.** `linea_ticket(producto: str, unidades: int, precio: float) -> str` devuelve una línea como `Camisa        2 x  19.90 =    39.80 €`: el producto a la izquierda en 12 huecos, las unidades a la derecha en 3, el precio en 6 con 2 decimales y el importe en 8.
<details><summary>Pista</summary>Una sola f-string con cuatro campos: <code>:&lt;12</code>, <code>:&gt;3</code>, <code>:&gt;6.2f</code> y <code>:&gt;8.2f</code>.</details>
<details><summary>Solución</summary>

```python
def linea_ticket(producto: str, unidades: int, precio: float) -> str:
    """Línea de ticket alineada en columnas."""
    importe: float = unidades * precio
    return f"{producto:<12}{unidades:>3} x {precio:>6.2f} = {importe:>8.2f} €"
```
</details>

**E8 ● · Desglose de una compra.** `desglose(unidades: int, precio: float) -> tuple[float, float, float]` devuelve la base, el IVA y el total, **redondeados a 2 decimales**. El IVA es una constante del 21 %.
<details><summary>Pista</summary><code>round(valor, 2)</code> en cada uno, y devuelve los tres separados por comas: eso ya es una tupla.</details>
<details><summary>Solución</summary>

```python
IVA: int = 21


def desglose(unidades: int, precio: float) -> tuple[float, float, float]:
    """Base, IVA y total de una compra, redondeados a 2 decimales."""
    base: float = unidades * precio
    iva: float = base * IVA / 100
    return round(base, 2), round(iva, 2), round(base + iva, 2)
```
</details>

---

---

## 9. Simulacro tipo test

El examen de esta unidad es un **test de código**: 12 preguntas de opción múltiple sobre
fragmentos como los que has visto en la teoría.

Tienes un simulacro con **8 preguntas por cada uno de los seis temas** —48 en total— con la
respuesta y la explicación desplegables:

**[Simulacro tipo test RA1](../simulacros/ra1/README.md)**

!!! tip "Cómo sacarle partido"
    Haz **un tema cada vez**, justo después de leerlo y hacer sus ejercicios. No los 48 de
    golpe el día antes: así sabes qué tema tienes flojo cuando todavía hay margen.

    Y no ejecutes el código hasta haber contestado. Después sí: pasa por Python las que
    hayas fallado y mira por qué.

---

## 10. Proyecto de la unidad

Toda la práctica de esta unidad se hace sobre un **proyecto base**: una calculadora de presupuestos con IVA. Está montado
con la estructura real de un proyecto Python y trae una **batería de tests** que puedes
ejecutar en cualquier momento para ver si va todo bien.

**[Proyecto Presupuesto de tienda →](../proyectos/ud1/README.md)**

```
proyecto-ud1/
├── src/      ← tu código (funciones con TODO)
└── tests/    ← 16 tests que comprueban tu trabajo
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

## 11. Retos opcionales

- **R1.** Amplía E5 para que, además de la media, diga `Aprobado`/`Suspenso` comparándola con 5.
- **R2.** Investiga `divmod(a, b)` (devuelve cociente y resto a la vez) y reescribe E3 con él.
- **R3.** Formatea un pequeño ticket con los precios alineados a la derecha (`:>8`), en columnas.
- **R4.** Añade anotaciones de tipo a **todos** tus ejercicios y consigue que `mypy` diga *Success* en cada uno.

- **R5.** Convierte una cantidad de segundos introducida por teclado a días, horas, minutos y segundos, y muéstralo como `2d 3h 04m 05s`.
- **R6.** Formatea un ticket de tres productos con los importes alineados a la derecha y una línea de total separada por guiones del mismo ancho.
---

---

## 12. Autoevaluación rápida

<details><summary>1. ¿Qué muestra <code>print(7 // 2)</code>?</summary><code>3</code> (división entera).</details>
<details><summary>2. ¿Qué tipo devuelve siempre <code>input()</code>?</summary><code>str</code>.</details>
<details><summary>3. ¿Por qué falla <code>"5" + 1</code>?</summary>Mezcla <code>str</code> e <code>int</code> (<code>TypeError</code>).</details>
<details><summary>4. Diferencia entre <code>=</code> y <code>==</code>.</summary><code>=</code> asigna; <code>==</code> compara.</details>
<details><summary>5. ¿Comprueba Python las anotaciones de tipo al ejecutar?</summary>No; las comprueba <b>mypy</b> de forma estática.</details>
<details><summary>6. ¿Para qué sirve un entorno virtual?</summary>Aislar los paquetes de cada proyecto para que no se mezclen.</details>
<details><summary>7. ¿Qué comando guarda las dependencias?</summary><code>pip freeze > requirements.txt</code>.</details>

---

---

## 13. Glosario

| Término | Definición |
|---|---|
| **Algoritmo** | Pasos para resolver un problema, independientes del lenguaje. |
| **Variable** | Nombre que guarda un valor y puede cambiar. |
| **Tipo** | Clase de dato: `int`, `float`, `str`, `bool`. |
| **Anotación de tipo** | Indicación `: tipo` que documenta y verifica con mypy. |
| **Literal / Constante** | Valor escrito directamente / valor que no debe cambiar. |
| **Operador / Expresión** | Símbolo que opera / combinación que produce un resultado. |
| **Casting** | Conversión de tipo (`int()`, `float()`, `str()`). |
| **f-string** | Cadena con formato `f"...{valor}..."`. |
| **Entorno virtual (venv)** | Copia aislada de Python por proyecto. |
| **pip** | Gestor de paquetes de Python. |
| **mypy** | Herramienta que comprueba los tipos sin ejecutar. |

---

---

## 14. Cómo se evalúa esta unidad (RA1)

El RA1 es del **primer trimestre**, y ahí el examen es un **test de 12 preguntas de
opción múltiple**. Pero no de definiciones: **todas las preguntas son de código**.

### Cómo son las preguntas

Se te da un fragmento y tienes que decir qué hace. Hay cuatro formas:

| Tipo | Qué te piden |
|---|---|
| **Qué imprime** | Seguir un programa de 5–12 líneas y dar la salida exacta, carácter a carácter. |
| **Qué error da** | Identificar la excepción: `TypeError`, `ValueError`, `UnboundLocalError`… |
| **Cuál es correcta** | Cuatro versiones de una función; solo una pasa todos los casos. |
| **Cuál es falsa** | Una función y cuatro pares «llamada → resultado»; uno de ellos miente. |

No son preguntas de una línea. Son fragmentos del mismo tipo que los ejercicios que haces:
presupuestos con IVA y descuento, tickets con formato, conversión de lo que escribe el
usuario, medias con la lista vacía. Y las cuatro opciones son **resultados reales de errores
concretos**, así que por descarte no se acierta: hay que seguir el cálculo.

Es exactamente lo que haces en clase cuando lees un error o predices un resultado antes de
ejecutar. Temas del RA1: tipos y variables · conversión de tipos · operadores y precedencia · constantes y nombres · formato de salida.

### Cómo se puntúa

| | |
|---|---|
| Acierto | **+0.83** puntos |
| Error | **−0.28** puntos |
| En blanco | 0 |

`nota = (aciertos − errores ÷ 3) × 0.83`, con un mínimo de 0.

Se resta un tercio por error porque hay cuatro opciones: así **contestar al azar no
compensa**. La regla práctica es sencilla:

- Si lo sabes, marca.
- Si dudas **entre dos**, marca: sigue saliéndote a cuenta.
- Si no tienes ni idea, **déjalo en blanco**.

### Un ejemplo de corrección

| Alumno | Aciertos | Errores | En blanco | Cuenta | Nota |
|---|:---:|:---:|:---:|---|:---:|
| Lo lleva bien | 10 | 2 | 0 | (10 − 0,67) × 0.83 | **7,78** |
| Va justo | 8 | 4 | 0 | (8 − 1,33) × 0.83 | **5,56** |
| Prudente | 6 | 0 | 6 | (6 − 0) × 0.83 | **5,00** |
| A ciegas | 3 | 9 | 0 | (3 − 3) × 0.83 | **0,00** |

Fíjate en las dos últimas filas: quien contesta solo lo que sabe aprueba, y quien marca a
voleo se queda a cero. **No es lo mismo dudar que adivinar.**

### Cómo prepararte

1. Los **ejercicios de sección** y los **ejercicios largos**: el test pregunta justo eso.
2. El **proyecto de la unidad**: escribir el código es lo que te enseña a leerlo.
3. El **[test de práctica](../simulacros/ra1/README.md)**, con las mismas 12 preguntas
   de formato y las respuestas al final.

!!! tip "Lee el código antes de ejecutarlo"
   Durante el curso, cada vez que vayas a ejecutar algo, predice primero qué va a salir.
   Ese hábito es literalmente el examen.

!!! note "En el segundo y tercer trimestre cambia"
    A partir del RA3 los exámenes son **retos de programación**: se escribe código y se
    corrige con una batería de casos de prueba. El test es solo para arrancar.

---

### Material de apoyo de la unidad

- **[Proyecto de la unidad](../proyectos/ud1/README.md)** — `presupuesto`, 16 tests.
- **[Test de práctica](../simulacros/ra1/README.md)** — 12 preguntas de código, con respuestas.
- **[Entorno de trabajo](../recursos/entorno.md)** — chuleta de `venv`, `pip` y `mypy`.
