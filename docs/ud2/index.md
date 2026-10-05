# Unidad 2 · Programas sencillos: funciones y librerías

> **Módulo:** CMO-313 · Fundamentos de programación
> **Resultado de aprendizaje:** RA2 · **Duración:** 8 h · **Peso:** 15 %
> **Lenguaje:** Python 3 (tipado) · **Requisito:** haber superado la UD1

En la UD1 escribías programas «de un tirón»: leer, calcular, mostrar. Eso funciona con problemas pequeños, pero se vuelve inmanejable en cuanto crecen. Esta unidad enseña la herramienta que lo resuelve: **dividir el problema en funciones** y **reutilizar código ya hecho** mediante librerías.

---

## Mapa de la unidad

<figure markdown>
  ![Mapa de la unidad 2](../assets/diagramas/ud2-mapa.svg#only-light)
  ![Mapa de la unidad 2](../assets/diagramas/ud2-mapa-dark.svg#only-dark)
  <figcaption>Un problema grande se parte en funciones; las librerías aportan funciones ya hechas.</figcaption>
</figure>

### Qué vas a saber hacer al terminar

- [ ] Descomponer un problema en **funciones** con una responsabilidad clara.
- [ ] Definir funciones con **parámetros** y **valor de retorno**, anotando los tipos.
- [ ] Distinguir `return` de `print` (el error más común de esta unidad).
- [ ] Usar **parámetros por defecto** y llamadas por nombre.
- [ ] Entender el **ámbito** de las variables (local y global).
- [ ] Manejar **listas** para trabajar con conjuntos de datos.
- [ ] Importar y usar la **librería estándar** (`math`, `random`, `statistics`).
- [ ] Crear tu **propio módulo** e importarlo desde otro programa.

### Cómo se trabaja esta unidad

Igual que la UD1, y en este orden:

**lees la sección** → **reto rápido** → **ejercicios de esa sección** (con solución
desplegable, al final de cada una) → en clase, dudas y **actividades guiadas** (sección 10)
→ **proyecto** con sus tests → **test de práctica** → examen (que en este trimestre es un **test de código**).

!!! tip "Los ejercicios de sección son la clave"
    Están justo después de cada explicación y solo usan lo que acabas de leer. Hazlos en
    el momento: es lo que hace que el tiempo de clase se pueda dedicar a lo que cuesta.

---

## 1. Por qué funciones

Imagina que necesitas calcular la media de notas en cinco sitios distintos de un programa. Sin funciones, copias el cálculo cinco veces. Y cuando descubras un fallo, tendrás que corregirlo… cinco veces (y olvidarás alguna).

Una **función** es un trozo de código con nombre que hace **una cosa concreta** y puede reutilizarse cuantas veces quieras.

> **Analogía.** Una función es como una **receta con nombre**: «hacer masa». La escribes una vez y luego dices «hago masa» sin repetir los pasos. Le pasas ingredientes (parámetros) y te devuelve un resultado (return).

Las tres razones para usarlas:

| Razón | Qué significa |
|---|---|
| **No repetirse** | El código se escribe una vez y se usa muchas. |
| **Dividir el problema** | Un problema grande se convierte en varios pequeños que sí sabes resolver. |
| **Poder probarlo** | Una función se puede comprobar por separado (es lo que hacen tus tests). |

> **Reto rápido 1.** Piensa en el programa de la UD1 (presupuesto). ¿Qué parte convertirías en función y cómo la llamarías?

## 2. Definir y llamar funciones

### 2.1 La estructura

```python
def area_rectangulo(base: float, altura: float) -> float:
    """Devuelve el área de un rectángulo."""
    return base * altura
```

Pieza a pieza:

| Parte | Qué es |
|---|---|
| `def` | palabra reservada que inicia la definición |
| `area_rectangulo` | **nombre** (en `snake_case`, describe lo que hace) |
| `base: float, altura: float` | **parámetros** con su tipo: los datos que necesita |
| `-> float` | el tipo que **devuelve** |
| `"""..."""` | *docstring*: qué hace la función |
| `return` | **devuelve** el resultado a quien la llamó |

Para **usarla** (llamarla):

```python
resultado: float = area_rectangulo(3.0, 4.0)
print(resultado)        # 12.0
```

!!! warning "El error nº 1 de esta unidad: `return` no es `print`"
    ```python
    def suma_mal(a: int, b: int) -> None:
        print(a + b)          # ✗ muestra, pero no devuelve

    def suma_bien(a: int, b: int) -> int:
        return a + b          # ✓ devuelve: puedes usar el resultado
    ```
    Con `suma_mal` no puedes hacer `total = suma_mal(2, 3) * 10`, porque `total` valdría `None`. **La función calcula y devuelve; quien la llama decide si lo muestra.**

### 2.2 Funciones que no devuelven nada

Algunas funciones solo *hacen* algo (mostrar por pantalla, por ejemplo). Se anotan con `-> None`:

```python
def saludar(nombre: str) -> None:
    print(f"Hola, {nombre}")

saludar("Ada")          # Hola, Ada
```

### 2.3 Devolver varios valores

Con una tupla, separando por comas:

```python
def area_y_perimetro(base: float, altura: float) -> tuple[float, float]:
    return base * altura, 2 * (base + altura)

area, perimetro = area_y_perimetro(4, 3)    # 12.0  y  14.0
```

> **Reto rápido 2.** Escribe `cuadrado(n: int) -> int` que devuelva el cuadrado de un número. Llámala con 7 y muestra el resultado.

## 3. Parámetros

### 3.1 Posicionales y por nombre

```python
def presentar(nombre: str, edad: int) -> str:
    return f"{nombre} tiene {edad} años"

print(presentar("Ada", 36))              # por posición
print(presentar(edad=36, nombre="Ada"))  # por nombre: el orden da igual
```

### 3.2 Parámetros por defecto

Un parámetro puede tener valor por defecto; entonces es opcional al llamar:

```python
def precio_con_iva(precio: float, iva: int = 21) -> float:
    return precio * (1 + iva / 100)

print(precio_con_iva(100))        # 121.0  (usa 21)
print(precio_con_iva(100, 10))    # 110.0  (usa 10)
```

!!! tip "Los parámetros con valor por defecto van al final"
    `def f(a, b=2, c)` es un error de sintaxis. Primero los obligatorios, después los opcionales.

> **Reto rápido 3.** Añade a `presentar` un parámetro `saludo: str = "Hola"` y haz que el texto empiece por él.

## 4. Ámbito de las variables

Una variable creada **dentro** de una función solo existe ahí: es **local**. Cuando la función termina, desaparece.

```python
def calcular() -> int:
    total = 10        # variable LOCAL
    return total

calcular()
print(total)          # ✗ NameError: 'total' no existe fuera
```

Las variables de fuera son **globales** y sí se pueden *leer* desde dentro:

```python
IVA = 21                       # global (constante)

def con_iva(precio: float) -> float:
    return precio * (1 + IVA / 100)   # puede leer IVA
```

!!! warning "No modifiques variables globales desde una función"
    Existe la palabra `global`, pero usarla convierte el programa en algo imposible de seguir. **Lo correcto es pasar los datos por parámetro y devolver el resultado.** Una función que solo depende de sus parámetros se llama *función pura* y es la más fácil de probar.

> **Reto rápido 4.** ¿Qué imprime este código? *(Piensa antes de ejecutarlo.)*
> ```python
> x = 5
> def cambiar() -> None:
>     x = 99
> cambiar()
> print(x)
> ```
> *(Respuesta: `5`. La `x` de dentro es otra variable distinta.)*

## 5. Listas: trabajar con varios datos

Hasta ahora cada variable guardaba **un** valor. Una **lista** guarda **muchos** bajo un solo nombre:

```python
notas: list[float] = [5.0, 7.5, 9.0, 4.5]

print(notas[0])        # 5.0    primer elemento (se empieza en 0)
print(notas[-1])       # 4.5    último
print(len(notas))      # 4      cuántos hay
```

Operaciones básicas:

```python
notas.append(6.0)      # añadir al final
print(sum(notas))      # 32.0   suma de todos
print(max(notas))      # 9.0    el mayor
print(min(notas))      # 4.5    el menor
```

Con esto ya puedes escribir funciones que reciben listas:

```python
def media(numeros: list[float]) -> float:
    return sum(numeros) / len(numeros)

print(media([5.0, 7.5, 9.0]))      # 7.166666666666667
```

!!! warning "Cuidado con la lista vacía"
    `media([])` provoca `ZeroDivisionError`, porque `len([])` es 0. En la UD3 aprenderás a controlarlo; de momento, tenlo presente.

> **Reto rápido 5.** Escribe `cuantos(numeros: list[int]) -> int` que devuelva cuántos elementos tiene la lista.

## 6. Librerías: código ya escrito

Una **librería** (o módulo) es un conjunto de funciones ya hechas que puedes usar. Python trae muchas incluidas: es la **librería estándar**.

### 6.1 Importar

```python
import math

print(math.sqrt(16))      # 4.0     raíz cuadrada
print(math.pi)            # 3.141592653589793
print(math.floor(3.7))    # 3       redondea hacia abajo
print(math.ceil(3.2))     # 4       redondea hacia arriba
```

También puedes importar solo lo que necesitas:

```python
from math import sqrt, pi

print(sqrt(25))     # 5.0    ya no hace falta escribir math.
```

### 6.2 Tres librerías útiles ya

```python
import random
print(random.randint(1, 6))        # número al azar entre 1 y 6
print(random.choice(["a", "b"]))   # elemento al azar de una lista

import statistics
print(statistics.mean([2, 4, 6]))     # 4      media
print(statistics.median([1, 5, 9]))   # 5      mediana
```

!!! tip "Antes de programar algo, mira si ya existe"
    `statistics.mean()` ya calcula medias. Escribir tu propia versión está bien **para aprender**, pero en un proyecto real se usa la librería: está probada por miles de personas.

### 6.3 Tu propio módulo

Cualquier fichero `.py` es un módulo importable. Si creas `utilidades.py`:

```python
# utilidades.py
def doble(n: int) -> int:
    return n * 2

def triple(n: int) -> int:
    return n * 3
```

lo usas desde otro fichero de la misma carpeta:

```python
# principal.py
import utilidades

print(utilidades.doble(5))     # 10
```

o importando funciones sueltas:

```python
from utilidades import doble, triple
print(doble(5), triple(5))     # 10 15
```

> **Reto rápido 6.** Crea `mis_utiles.py` con una función `mitad(n: float) -> float` e impórtala desde otro fichero.

## 7. `if __name__ == "__main__":`

Cuando importas un módulo, Python **ejecuta todo su código suelto**. Si tu fichero tiene pruebas o `input()` fuera de las funciones, se dispararán al importarlo, que no es lo que quieres.

La solución es este guardián:

```python
def doble(n: int) -> int:
    return n * 2

if __name__ == "__main__":
    # esto SOLO se ejecuta si lanzas este fichero directamente
    print(doble(21))
```

- Si ejecutas `python utilidades.py` → se ejecuta el bloque.
- Si haces `import utilidades` desde otro sitio → **no** se ejecuta.

!!! tip "Regla práctica de esta unidad"
    En un módulo de funciones, **todo el código suelto va dentro de ese `if`**. Tus tests importan el fichero, así que si dejas un `input()` fuera, se quedarán colgados.

---

> **Reto rápido 7.** Coge un fichero con una función `saluda()` y añádele `if __name__ == "__main__":` con una llamada de prueba. Impórtalo desde otro fichero y comprueba que no se ejecuta nada.

## 8. Cómo descomponer un problema

El método, paso a paso:

1. **Escribe qué hay que hacer** en frases cortas.
2. Cada frase con un verbo claro → **una función**.
3. Decide qué **necesita** cada una (parámetros) y qué **da** (return).
4. Escríbelas y **pruébalas por separado**.
5. Monta el programa principal llamándolas.

**Ejemplo.** «Calcular la nota final de un alumno a partir de sus notas, y decir si aprueba.»

```python
def media(notas: list[float]) -> float:
    """Devuelve la media de una lista de notas."""
    return sum(notas) / len(notas)


def aprueba(nota: float) -> bool:
    """Indica si una nota es de aprobado."""
    return nota >= 5


def main() -> None:
    notas: list[float] = [6.0, 7.0, 4.0]
    nota_final: float = media(notas)
    print(f"Media: {nota_final:.2f}")
    print("Aprobado" if aprueba(nota_final) else "Suspenso")


if __name__ == "__main__":
    main()
```

Fíjate: `media` y `aprueba` **no muestran nada**; devuelven datos. Solo `main` imprime. Esa separación es la clave y es lo que permite probarlas automáticamente.

---

> **Reto rápido 8.** Enumera (sin código) las funciones en que partirías «calcular la factura de la luz» a partir de la lectura anterior, la actual y el precio del kWh. *(Solución: una para el consumo, otra para el importe y otra para mostrarlo.)*

## 9. Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| La función devuelve `None` | usaste `print` en vez de `return` | devuelve el valor con `return` |
| `TypeError: takes 2 positional arguments but 3 were given` | llamas con más argumentos de los definidos | revisa los parámetros |
| `NameError` al usar una variable de la función | es **local**, no existe fuera | devuélvela con `return` |
| `ModuleNotFoundError` | el módulo no existe o está en otra carpeta | mismo directorio y nombre exacto |
| El test se queda colgado | hay un `input()` suelto en el módulo | mételo en `if __name__ == "__main__":` |
| `ZeroDivisionError` en `media` | lista vacía | contémplalo (UD3) |

---

---

## 10. Ejercicios

Aquí están **todos los ejercicios de la unidad**, agrupados por el
tema al que corresponden y con la solución desplegable.

**Haz los de un tema en cuanto termines de leerlo.** No esperes al final: son cortos y solo
usan lo que acabas de ver, así que si algo no ha quedado claro lo descubres en el momento y
no tres semanas después.

!!! warning "Intenta antes de desplegar"
    Abrir la solución sin haberlo intentado da sensación de aprender, y no enseña nada. Si
    llevas quince minutos sin avanzar, mírala. Si llevas dos, no.


### Tema 1 · Por qué funciones

**1.1.** Este código repite lo mismo tres veces. Reescríbelo con **una sola función**:

```python
print(f"Hola, Ada")
print(f"Hola, Alan")
print(f"Hola, Grace")
```
<details><summary>Solución</summary>

```python
def saludar(nombre: str) -> None:
    """Saluda a la persona indicada."""
    print(f"Hola, {nombre}")

saludar("Ada")     # -> Hola, Ada
saludar("Alan")    # -> Hola, Alan
saludar("Grace")   # -> Hola, Grace

# Si mañana cambia el saludo, se toca en UN sitio, no en tres.
```
</details>

**1.2.** Nombra bien estas funciones. ¿Qué problema tiene cada nombre? `f1`, `hacer_cosas`, `calcular`.
<details><summary>Solución</summary>

```text
f1           -> no dice nada; en dos semanas no recordaras que hacia
hacer_cosas  -> demasiado vago: si hace 'cosas' en plural, probablemente
                deberian ser varias funciones
calcular     -> calcular, si, pero ¿que? Falta el complemento

Buenos nombres: verbo + complemento, en minusculas y con guion bajo:
    calcular_iva, media_notas, es_par, formatear_precio
```
</details>

**1.3.** Escribe la función más pequeña posible que evite repetir el cálculo del IVA en un programa que factura tres artículos.
<details><summary>Solución</summary>

```python
IVA: int = 21


def con_iva(precio: float) -> float:
    """Devuelve el precio con el IVA aplicado."""
    return precio * (1 + IVA / 100)

print(f"{con_iva(10):.2f}")   # -> 12.10
print(f"{con_iva(25):.2f}")   # -> 30.25
print(f"{con_iva(99):.2f}")   # -> 119.79
```
</details>


### Tema 2 · Definir y llamar funciones

**2.1.** Escribe `es_par(n)` que devuelva `True` o `False`, con sus tipos y su docstring.
<details><summary>Solución</summary>

```python
def es_par(n: int) -> bool:
    """Indica si un número es par."""
    return n % 2 == 0

print(es_par(4))   # -> True
print(es_par(7))   # -> False
```
</details>

**2.2.** ¿Qué diferencia hay entre estas dos funciones? Ejecútalas y mira lo que devuelven.

```python
def a(x): print(x * 2)
def b(x): return x * 2
```
<details><summary>Solución</summary>

```python
def a(x: int) -> None:
    """Muestra el doble por pantalla."""
    print(x * 2)


def b(x: int) -> int:
    """Devuelve el doble."""
    return x * 2

resultado_a = a(5)   # -> 10   (lo imprime la propia funcion)
resultado_b = b(5)

print(resultado_a)   # -> None   a() no devuelve nada
print(resultado_b)   # -> 10     b() SI devuelve, y por eso se puede reutilizar
print(b(5) + b(3))   # -> 16     esto con a() seria imposible
```
</details>

**2.3.** Escribe `mayor(a, b)` que devuelva el mayor de dos números, sin usar `max()`.
<details><summary>Solución</summary>

```python
def mayor(a: float, b: float) -> float:
    """Devuelve el mayor de los dos números."""
    if a > b:
        return a
    return b

print(mayor(3, 9))     # -> 9
print(mayor(-2, -7))   # -> -2
print(mayor(4, 4))     # -> 4
```
</details>


### Tema 3 · Parámetros

**3.1.** Escribe `presentar(nombre, ciudad)` y llámala **por posición** y **por nombre**.
<details><summary>Solución</summary>

```python
def presentar(nombre: str, ciudad: str) -> str:
    """Frase de presentación."""
    return f"{nombre} vive en {ciudad}"

print(presentar("Ada", "Londres"))                     # -> Ada vive en Londres
print(presentar(ciudad="Madrid", nombre="Alan"))       # -> Alan vive en Madrid

# Por nombre el orden da igual, y se lee mucho mejor cuando hay varios parametros.
```
</details>

**3.2.** Añade a `saludar(nombre, saludo)` un **valor por defecto** para que `saludo` sea `"Hola"` si no se indica.
<details><summary>Solución</summary>

```python
def saludar(nombre: str, saludo: str = "Hola") -> str:
    """Saluda con el saludo indicado (Hola por defecto)."""
    return f"{saludo}, {nombre}"

print(saludar("Ada"))                 # -> Hola, Ada
print(saludar("Ada", "Buenas"))       # -> Buenas, Ada
```
</details>

**3.3.** Escribe `potencia(base, exponente)` con `exponente` a 2 por defecto, y comprueba que los parámetros con valor por defecto van **al final**.
<details><summary>Solución</summary>

```python
def potencia(base: float, exponente: int = 2) -> float:
    """Eleva la base al exponente indicado (al cuadrado por defecto)."""
    return base ** exponente

print(potencia(5))      # -> 25
print(potencia(2, 10))  # -> 1024

# def potencia(exponente=2, base): ...  -> SyntaxError
# Los parametros con valor por defecto tienen que ir SIEMPRE al final.
```
</details>


### Tema 4 · Ámbito de las variables

**4.1.** ¿Qué imprime este programa? Piénsalo antes de ejecutarlo.

```python
x = 10
def f():
    x = 99
f()
print(x)
```
<details><summary>Solución</summary>

```python
x = 10


def f() -> None:
    x = 99          # esta x es NUEVA y solo vive dentro de f()
    print("dentro:", x)   # -> dentro: 99

f()
print("fuera:", x)   # -> fuera: 10

# Asignar dentro de una funcion crea una variable local: la de fuera no se toca.
```
</details>

**4.2.** Esta función no funciona porque usa una variable que no existe fuera. Arréglala pasándola como parámetro:

```python
def mostrar_total():
    print(total)
```
<details><summary>Solución</summary>

```python
def mostrar_total(total: float) -> None:
    """Muestra el total recibido."""
    print(f"Total: {total:.2f}")

mostrar_total(42.5)   # -> Total: 42.50

# Todo lo que la funcion necesita entra por parametros: asi es independiente
# y se puede probar sola.
```
</details>

**4.3.** Escribe `acumular(lista, valor)` que devuelva una **lista nueva** con el valor añadido, sin modificar la original.
<details><summary>Solución</summary>

```python
def acumular(lista: list[int], valor: int) -> list[int]:
    """Devuelve una lista nueva con el valor añadido al final."""
    return lista + [valor]

original = [1, 2]
nueva = acumular(original, 3)

print(original)   # -> [1, 2]
print(nueva)      # -> [1, 2, 3]
```
</details>


### Tema 5 · Listas

**5.1.** Crea una lista con cinco notas, muestra la primera, la última y cuántas hay.
<details><summary>Solución</summary>

```python
notas: list[float] = [5.0, 7.5, 9.0, 4.25, 6.0]

print(notas[0])     # -> 5.0
print(notas[-1])    # -> 6.0     el -1 es el ultimo, sin contar
print(len(notas))   # -> 5
```
</details>

**5.2.** Escribe `suma_lista(numeros)` que sume una lista **sin usar `sum()`**.
<details><summary>Solución</summary>

```python
def suma_lista(numeros: list[float]) -> float:
    """Suma todos los elementos de la lista."""
    total: float = 0.0
    for n in numeros:
        total = total + n
    return total

print(suma_lista([1, 2, 3, 4]))   # -> 10.0
print(suma_lista([]))             # -> 0.0
```
</details>

**5.3.** Escribe `media(numeros)` que devuelva `0.0` si la lista está vacía.
<details><summary>Solución</summary>

```python
def media(numeros: list[float]) -> float:
    """Media aritmética; 0.0 si la lista está vacía."""
    if len(numeros) == 0:
        return 0.0
    return sum(numeros) / len(numeros)

print(media([5.0, 7.0, 9.0]))   # -> 7.0
print(media([]))                # -> 0.0

# Sin el if, la lista vacia provoca ZeroDivisionError. Es el caso limite
# que mas se olvida y el que casi siempre esta en los tests.
```
</details>


### Tema 6 · Librería estándar

**6.1.** Calcula la raíz cuadrada de 144 y el área de un círculo de radio 3 usando `math`.
<details><summary>Solución</summary>

```python
import math

print(math.sqrt(144))            # -> 12.0
print(f"{math.pi * 3 ** 2:.2f}")  # -> 28.27
```
</details>

**6.2.** Necesitas redondear **siempre hacia arriba** el número de cajas para 47 unidades que van de 10 en 10. Búscalo en `math`.
<details><summary>Solución</summary>

```python
import math

unidades: int = 47
por_caja: int = 10

cajas: int = math.ceil(unidades / por_caja)

print(cajas)   # -> 5

# 47 / 10 = 4.7  ->  con round() saldrian 5, pero con 44 unidades round() daria 4
# y se quedarian 4 unidades fuera. ceil() nunca deja a nadie fuera.
```
</details>

**6.3.** Muestra la fecha de hoy en formato `dd/mm/aaaa` con el módulo `datetime`.
<details><summary>Solución</summary>

```python
from datetime import date

hoy = date.today()
print(hoy.strftime("%d/%m/%Y"))

# Antes de escribir tu propia funcion, mira si ya existe en la libreria estandar:
# viene instalada, esta probada por medio mundo y no hay que mantenerla.
```
</details>


### Tema 7 · Módulos y `__main__`

**7.1.** Añade a un módulo con la función `doble()` el bloque `if __name__ == "__main__":` para poder probarlo directamente.
<details><summary>Solución</summary>

```python
"""Módulo de ejemplo."""


def doble(n: int) -> int:
    """Devuelve el doble."""
    return n * 2


if __name__ == "__main__":
    # Esto solo se ejecuta si lanzas ESTE fichero, no al importarlo
    print(doble(21))   # -> 42
```
</details>

**7.2.** ¿Qué pasa si otro fichero hace `import mimodulo` y el módulo tiene un `print()` suelto al final?
<details><summary>Solución</summary>

```text
Que ese print() se ejecuta al importar, aunque el otro fichero solo queria
usar una funcion. Efectos raros al importar = programa dificil de reutilizar.

Por eso las pruebas y los ejemplos van dentro de:

    if __name__ == "__main__":
        ...

Al importar, __name__ vale "mimodulo" y el bloque no se ejecuta.
Al lanzarlo directamente, __name__ vale "__main__" y si se ejecuta.
```
</details>

**7.3.** Comprueba qué vale `__name__` cuando ejecutas el fichero directamente.
<details><summary>Solución</summary>

```python
print(__name__)   # -> __main__

if __name__ == "__main__":
    print("Me han lanzado directamente")   # -> Me han lanzado directamente
```
</details>


### Tema 8 · Descomponer un problema

**8.1.** Descompón en funciones el problema «calcular la nota final de un alumno a partir de sus notas y decir si aprueba». No escribas el cuerpo todavía: solo las firmas.
<details><summary>Solución</summary>

```python
def media(notas: list[float]) -> float:
    """Media de las notas."""
    ...


def redondear_nota(nota: float) -> float:
    """Nota redondeada a dos decimales."""
    ...


def aprueba(nota: float) -> bool:
    """Indica si la nota llega a 5."""
    ...

# Tres funciones pequenas, cada una con UNA responsabilidad y cada una probable
# por separado. Eso es descomponer.
```
</details>

**8.2.** Ahora escribe el cuerpo de esas tres funciones y encadénalas.
<details><summary>Solución</summary>

```python
def media(notas: list[float]) -> float:
    """Media de las notas; 0.0 si no hay."""
    if len(notas) == 0:
        return 0.0
    return sum(notas) / len(notas)


def redondear_nota(nota: float) -> float:
    """Nota redondeada a dos decimales."""
    return round(nota, 2)


def aprueba(nota: float) -> bool:
    """Indica si la nota llega a 5."""
    return nota >= 5

notas = [7.0, 4.5, 6.25]
final = redondear_nota(media(notas))

print(final)           # -> 5.92
print(aprueba(final))  # -> True
```
</details>

**8.3.** Esta función hace demasiadas cosas. Pártela en dos:

```python
def procesar(notas):
    m = sum(notas) / len(notas)
    print(f"Media: {m:.2f}")
```
<details><summary>Solución</summary>

```python
def media(notas: list[float]) -> float:
    """Solo calcula."""
    if len(notas) == 0:
        return 0.0
    return sum(notas) / len(notas)


def mostrar_media(notas: list[float]) -> None:
    """Solo muestra."""
    print(f"Media: {media(notas):.2f}")

mostrar_media([5.0, 8.0])   # -> Media: 6.50

# Calcular y mostrar son dos responsabilidades. Separadas, media() se puede
# probar con un test y reutilizar en cualquier otro sitio.
```
</details>


### Actividades guiadas

#### Actividad 1 — Tu primera función
Escribe `saludo(nombre: str) -> str` que **devuelva** (no imprima) `"Hola, Ada"`.
<details><summary>Solución</summary>

```python
def saludo(nombre: str) -> str:
    return f"Hola, {nombre}"

print(saludo("Ada"))     # Hola, Ada
```
</details>

#### Actividad 2 — Varias operaciones
Escribe `operaciones(a: int, b: int) -> tuple[int, int, int]` que devuelva suma, resta y producto.
<details><summary>Solución</summary>

```python
def operaciones(a: int, b: int) -> tuple[int, int, int]:
    return a + b, a - b, a * b

s, r, p = operaciones(7, 3)
print(s, r, p)      # 10 4 21
```
</details>

#### Actividad 3 — Usar una librería
Con `math`, escribe `hipotenusa(a: float, b: float) -> float`.
<details><summary>Solución</summary>

```python
import math

def hipotenusa(a: float, b: float) -> float:
    return math.sqrt(a ** 2 + b ** 2)

print(hipotenusa(3, 4))     # 5.0
```
</details>

#### Actividad 4 — Trabajar con listas
Escribe `resumen(numeros: list[float]) -> tuple[float, float, float]` que devuelva media, mínimo y máximo.
<details><summary>Solución</summary>

```python
def resumen(numeros: list[float]) -> tuple[float, float, float]:
    return sum(numeros) / len(numeros), min(numeros), max(numeros)

print(resumen([4.0, 8.0, 6.0]))     # (6.0, 4.0, 8.0)
```
</details>

### Ejercicios propuestos

**E1 ○ · Área del círculo.** `area_circulo(radio: float) -> float` usando `math.pi`.
<details><summary>Solución</summary>

```python
import math

def area_circulo(radio: float) -> float:
    return math.pi * radio ** 2
```
</details>

**E2 ○ · Conversión.** `a_fahrenheit(celsius: float) -> float`.
<details><summary>Solución</summary>

```python
def a_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32
```
</details>

**E3 ◐ · Precio final.** `precio_final(precio: float, iva: int = 21, descuento: int = 0) -> float`: aplica primero el descuento y después el IVA.
<details><summary>Pista</summary>Calcula el precio con descuento y sobre ese resultado aplica el IVA.</details>
<details><summary>Solución</summary>

```python
def precio_final(precio: float, iva: int = 21, descuento: int = 0) -> float:
    con_descuento = precio * (1 - descuento / 100)
    return con_descuento * (1 + iva / 100)

print(precio_final(100))            # 121.0
print(precio_final(100, 21, 10))    # 108.9
```
</details>

**E4 ◐ · Contar pares.** `cuenta_pares(numeros: list[int]) -> int`.
<details><summary>Pista</summary>Recorre con un bucle y usa <code>% 2 == 0</code>. También vale <code>sum(1 for n in numeros if n % 2 == 0)</code>.</details>
<details><summary>Solución</summary>

```python
def cuenta_pares(numeros: list[int]) -> int:
    total = 0
    for n in numeros:
        if n % 2 == 0:
            total += 1
    return total
```
</details>

**E5 ◐ · Módulo propio.** Crea `estadistica.py` con `media`, `maximo` y `minimo`, e impórtalo desde `principal.py`.
<details><summary>Solución</summary>

```python
# estadistica.py
def media(numeros: list[float]) -> float:
    return sum(numeros) / len(numeros)

def maximo(numeros: list[float]) -> float:
    return max(numeros)

def minimo(numeros: list[float]) -> float:
    return min(numeros)
```
```python
# principal.py
import estadistica

datos = [4.0, 8.0, 6.0]
print(estadistica.media(datos))     # 6.0
```
</details>

**E6 ● · Redondeo a múltiplo.** `redondear_a(valor: float, multiplo: int = 5) -> int`: redondea al múltiplo más cercano.
<details><summary>Pista</summary><code>round(valor / multiplo) * multiplo</code></details>
<details><summary>Solución</summary>

```python
def redondear_a(valor: float, multiplo: int = 5) -> int:
    return round(valor / multiplo) * multiplo

print(redondear_a(23))       # 25
print(redondear_a(23, 10))   # 20
```
</details>

**E7 ◐ · Contar pares.** `contar_pares(numeros: list[int]) -> int` devuelve cuántos números pares hay en la lista.
<details><summary>Pista</summary>Un acumulador a 0 y un <code>for</code>; el resto de dividir entre 2 te dice si es par.</details>
<details><summary>Solución</summary>

```python
def contar_pares(numeros: list[int]) -> int:
    """Cuántos números pares hay en la lista."""
    total: int = 0
    for n in numeros:
        if n % 2 == 0:
            total += 1
    return total
```
</details>

**E8 ● · Resumen estadístico.** `resumen(numeros: list[float]) -> tuple[float, float, float]` devuelve mínimo, máximo y media. Con la lista vacía devuelve `(0.0, 0.0, 0.0)`.
<details><summary>Pista</summary>Resuelve primero el caso de la lista vacía y sal con <code>return</code>; así el resto del código ya puede dar por hecho que hay datos.</details>
<details><summary>Solución</summary>

```python
def resumen(numeros: list[float]) -> tuple[float, float, float]:
    """Mínimo, máximo y media; (0.0, 0.0, 0.0) si la lista está vacía."""
    if len(numeros) == 0:
        return 0.0, 0.0, 0.0
    return min(numeros), max(numeros), sum(numeros) / len(numeros)
```
</details>

---

---

## 11. Simulacro tipo test

El examen de esta unidad es un **test de código**. Tienes uno de
práctica con **8 preguntas por cada tema** de la unidad y la respuesta explicada:

**[Simulacro tipo test RA2](../simulacros/ra2/README.md)**

Hazlo cuando termines los ejercicios, contrarreloj y sin ordenador. Después comprueba en
Python las que hayas fallado: ahí es donde de verdad se aprende.

---

## 12. Proyecto de la unidad

Toda la práctica de esta unidad se hace sobre un **proyecto base**: un paquete de funciones reutilizables en tres módulos. Está montado
con la estructura real de un proyecto Python y trae una **batería de tests** que puedes
ejecutar en cualquier momento para ver si va todo bien.

**[Proyecto Biblioteca de utilidades →](../proyectos/ud2/README.md)**

```
proyecto-ud2/
├── src/      ← tu código (funciones con TODO)
└── tests/    ← 31 tests que comprueban tu trabajo
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

## 13. Retos opcionales

- **R1.** Añade a P1 una función `mediana(numeros: list[float]) -> float` sin usar `statistics`.
- **R2.** Investiga `*args` y escribe `suma_todos(*numeros)` que sume cuantos números le pases.
- **R3.** Compara tu `media` con `statistics.mean` sobre la misma lista: ¿dan exactamente lo mismo?

- **R4.** Escribe `es_primo(n)` sin usar librerías y pruébala con los números del 1 al 20.
- **R5.** Crea tu propio módulo `texto.py` con tres funciones de utilidad (contar vocales, invertir, quitar espacios) e impórtalo desde otro programa.
- **R6.** Investiga `random.sample()` y escribe una función que devuelva 6 números distintos del 1 al 49.
---

---

## 14. Autoevaluación rápida

<details><summary>1. ¿Qué diferencia hay entre <code>return</code> y <code>print</code>?</summary><code>return</code> devuelve el valor a quien llamó (se puede seguir usando); <code>print</code> solo lo muestra.</details>
<details><summary>2. ¿Qué devuelve una función sin <code>return</code>?</summary><code>None</code>.</details>
<details><summary>3. ¿Se puede leer una variable global desde una función?</summary>Sí, leerla sí. Modificarla es mala práctica: mejor pasarla por parámetro.</details>
<details><summary>4. ¿Para qué sirve <code>if __name__ == "__main__":</code>?</summary>Para que el código suelto solo se ejecute al lanzar el fichero directamente, no al importarlo.</details>
<details><summary>5. ¿Cómo se importa solo <code>sqrt</code> de <code>math</code>?</summary><code>from math import sqrt</code></details>
<details><summary>6. ¿Qué vale <code>len([3, 5, 7])</code>?</summary><code>3</code>.</details>

---

---

## 15. Glosario

| Término | Definición |
|---|---|
| **Función** | Bloque de código con nombre que hace una tarea y puede devolver un resultado. |
| **Parámetro / argumento** | Dato que la función declara / valor concreto que se le pasa. |
| **`return`** | Devuelve un valor y termina la función. |
| **Función pura** | Solo depende de sus parámetros y no toca nada de fuera. |
| **Ámbito** | Zona donde existe una variable (local o global). |
| **Lista** | Colección ordenada de valores: `[1, 2, 3]`. |
| **Módulo / librería** | Fichero (o conjunto) con funciones reutilizables. |
| **`import`** | Trae a tu programa el contenido de un módulo. |

---

---

## 16. Cómo se evalúa esta unidad (RA2)

El RA2 es del **primer trimestre**, y ahí el examen es un **test de 12 preguntas de
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
ejecutar. Temas del RA2: `return` frente a `print` · parámetros y valores por defecto · ámbito · listas · librería estándar · módulos y `__main__`.

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
3. El **[test de práctica](../simulacros/ra2/README.md)**, con las mismas 12 preguntas
   de formato y las respuestas al final.

!!! tip "Lee el código antes de ejecutarlo"
   Durante el curso, cada vez que vayas a ejecutar algo, predice primero qué va a salir.
   Ese hábito es literalmente el examen.

!!! note "En el segundo y tercer trimestre cambia"
    A partir del RA3 los exámenes son **retos de programación**: se escribe código y se
    corrige con una batería de casos de prueba. El test es solo para arrancar.
