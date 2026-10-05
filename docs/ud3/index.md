# Unidad 3 · Estructuras de control, excepciones y depuración

> **Módulo:** CMO-313 · Fundamentos de programación
> **Resultado de aprendizaje:** RA3 · **Duración:** 12 h · **Peso:** 25 %
> **Lenguaje:** Python 3 (tipado) · **La unidad más importante del módulo**

Hasta ahora tus programas iban en línea recta: siempre las mismas instrucciones, en el mismo orden. Aquí aprenden a **decidir** (hacer una cosa u otra según los datos) y a **repetir** (hacer algo muchas veces sin escribirlo muchas veces). Con esto ya puedes escribir prácticamente cualquier programa.

Es la unidad de **mayor peso** del módulo (25 %), y con razón: todo lo que venga después la usa.

---

## Mapa de la unidad

<figure markdown>
  ![Mapa de la unidad 3](../assets/diagramas/ud3-mapa.svg#only-light)
  ![Mapa de la unidad 3](../assets/diagramas/ud3-mapa-dark.svg#only-dark)
  <figcaption>Decidir, repetir y no romperse cuando llegan datos inesperados.</figcaption>
</figure>

### Qué vas a saber hacer al terminar

- [ ] Tomar decisiones con `if` / `elif` / `else`.
- [ ] Repetir con `while` (mientras se cumpla algo) y con `for` (para cada elemento).
- [ ] Usar `break` y `continue` con criterio.
- [ ] Recorrer listas y diccionarios.
- [ ] **Controlar errores** con `try` / `except` para que el programa no se caiga.
- [ ] **Validar** la entrada del usuario.
- [ ] Depurar: encontrar por qué un programa no hace lo que crees.

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

## 1. Decidir: `if`, `elif`, `else`

### 1.1 La forma básica

```python
nota: float = 7.0

if nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

Lo importante de la sintaxis de Python:

- La condición termina en **dos puntos** `:`.
- El bloque que depende de ella va **indentado** (4 espacios). La indentación **no es decorativa**: es lo que marca qué pertenece al `if`.

```python
if nota >= 5:
    print("Aprobado")        # dentro del if
print("Fin")                 # fuera: se ejecuta siempre
```

### 1.2 Varias opciones con `elif`

```python
nota: float = 7.0

if nota >= 9:
    calificacion = "Sobresaliente"
elif nota >= 7:
    calificacion = "Notable"
elif nota >= 6:
    calificacion = "Bien"
elif nota >= 5:
    calificacion = "Suficiente"
else:
    calificacion = "Insuficiente"

print(calificacion)          # Notable
```

!!! tip "El orden importa"
    Python comprueba de arriba abajo y se queda en **la primera** condición verdadera. Por eso se ponen de mayor a menor: si empezaras por `nota >= 5`, un 9 entraría ahí y nunca llegaría a «Sobresaliente».

### 1.3 Condiciones compuestas

```python
edad: int = 20
tiene_carnet: bool = True

if edad >= 18 and tiene_carnet:
    print("Puede conducir")

if not tiene_carnet or edad < 18:
    print("No puede conducir")
```

> **Error clásico:** `if edad >= 18 and <= 65` no es válido. Hay que repetir la variable: `if edad >= 18 and edad <= 65`. *(En Python también vale `if 18 <= edad <= 65`.)*

> **Reto rápido 1.** Escribe un `if` que muestre `"Par"` o `"Impar"` según un número.

## 2. Repetir con `while`

`while` repite **mientras** una condición sea verdadera:

```python
contador: int = 1
while contador <= 3:
    print(contador)
    contador = contador + 1     # ¡imprescindible!
```

Salida: `1`, `2`, `3`.

!!! danger "El bucle infinito"
    Si olvidas modificar la variable de la condición, el bucle **no termina nunca**:
    ```python
    contador = 1
    while contador <= 3:
        print(contador)       # ✗ contador nunca cambia
    ```
    Se corta con `Ctrl+C`. Siempre que escribas un `while`, pregúntate: *¿qué hace que esta condición acabe siendo falsa?*

### 2.1 El patrón «menú»

Es el uso más habitual y el que aparece en el examen:

```python
opcion: str = ""
while opcion != "0":
    print("1 - Saludar")
    print("0 - Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        print("¡Hola!")
print("Adiós")
```

> **Reto rápido 2.** Escribe un `while` que muestre los números del 10 al 1 (cuenta atrás).

## 3. Repetir con `for`

`for` recorre **cada elemento** de una colección. Es el bucle preferido cuando sabes sobre qué iteras.

```python
notas: list[float] = [5.0, 7.5, 9.0]

for nota in notas:
    print(nota)
```

### 3.1 `range()`: repetir un número de veces

```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8  (de dos en dos)
    print(i)
```

!!! tip "`range(n)` llega hasta n-1"
    `range(5)` da cinco valores: del 0 al 4. Es el mismo criterio que los índices de las listas.

### 3.2 Acumular

Patrón fundamental: una variable que va creciendo dentro del bucle.

```python
notas: list[float] = [5.0, 7.5, 9.0]

total: float = 0.0
for nota in notas:
    total = total + nota        # también: total += nota

print(f"Suma: {total}")         # 21.5
print(f"Media: {total / len(notas):.2f}")
```

### 3.3 Contar con condición

```python
aprobados: int = 0
for nota in notas:
    if nota >= 5:
        aprobados += 1
print(aprobados)      # 3
```

### 3.4 `while` o `for`, ¿cuál?

| Usa… | Cuando… |
|---|---|
| `for` | recorres una lista o repites un nº **conocido** de veces |
| `while` | repites **hasta que pase algo** (menús, validaciones) |

> **Reto rápido 3.** Con un `for` y `range`, suma los números del 1 al 100. *(Resultado: 5050.)*

## 4. Diccionarios

Una lista guarda valores por posición; un **diccionario** los guarda por **clave**:

```python
alumno: dict[str, str] = {
    "nombre": "Ada",
    "grupo": "1DAW",
}

print(alumno["nombre"])         # Ada
alumno["edad"] = "20"           # añadir
```

Recorrerlo:

```python
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")
```

> Acceder a una clave que no existe da `KeyError`. Para evitarlo: `alumno.get("edad", "desconocida")`.

---

> **Reto rápido 4.** Crea un diccionario con tres provincias y su prefijo telefónico, y muestra el de una de ellas.

## 5. `break` y `continue`

- **`break`** sale del bucle inmediatamente.
- **`continue`** salta a la siguiente vuelta.

```python
for n in [1, 2, 3, 4, 5]:
    if n == 4:
        break              # al llegar al 4, corta
    print(n)               # 1 2 3

for n in [1, 2, 3, 4, 5]:
    if n % 2 == 0:
        continue           # se salta los pares
    print(n)               # 1 3 5
```

!!! warning "Úsalos con moderación"
    Un `break` bien puesto aclara el código; cinco `break` repartidos lo vuelven imposible de seguir. Si puedes expresarlo en la condición del bucle, mejor.

> **Reto rápido 4.** Recorre `[3, 8, 2, 9, 4]` y para en cuanto encuentres un número mayor que 5, mostrándolo.

## 6. Excepciones: que el programa no se caiga

Ya conoces esto: si el usuario escribe `"hola"` cuando pides un número, el programa **se rompe**.

```python
edad = int(input("Edad: "))     # el usuario escribe "hola" → ValueError, programa muerto
```

### 6.1 `try` / `except`

```python
try:
    edad = int(input("Edad: "))
    print(f"Tienes {edad} años")
except ValueError:
    print("Eso no es un número")
```

- En `try` va el código que **puede fallar**.
- En `except` va **qué hacer si falla**. El programa continúa.

### 6.2 Capturar el error correcto

```python
try:
    resultado = 10 / int(input("Divisor: "))
except ValueError:
    print("No has escrito un número")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
```

!!! danger "No captures `Exception` a secas"
    ```python
    try:
        ...
    except:            # ✗ atrapa TODO, incluso errores tuyos de programación
        pass           # ✗ y encima los oculta
    ```
    Así, un fallo real (una variable mal escrita) se traga en silencio y no te enteras. **Captura la excepción concreta que esperas.**

### 6.3 `else` y `finally`

```python
try:
    numero = int(input("Número: "))
except ValueError:
    print("Entrada no válida")
else:
    print(f"El doble es {numero * 2}")   # solo si NO hubo error
finally:
    print("Fin")                          # siempre, haya error o no
```

### 6.4 El patrón «validar entrada»

La combinación de `while` + `try` que usarás una y otra vez:

```python
def pedir_entero(mensaje: str) -> int:
    """Pide un entero hasta que el usuario escriba uno válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida, inténtalo otra vez")
```

> **Reto rápido 5.** ¿Qué excepción lanza `int("3.5")`? *(Respuesta: `ValueError`; `int()` no acepta decimales en texto.)*

## 7. Depurar: encontrar el fallo

Depurar es averiguar **por qué** el programa no hace lo que crees. Tres herramientas, de menos a más:

### 7.1 `print` de diagnóstico

La más simple y muchas veces suficiente. Muestra el valor de las variables en puntos clave:

```python
for i, nota in enumerate(notas):
    print(f"[debug] i={i} nota={nota} total={total}")
```

Bórralos cuando termines.

### 7.2 El depurador del IDE

En VS Code: haz clic a la izquierda del número de línea para poner un **punto de ruptura** (breakpoint) y pulsa **F5**. El programa se detiene ahí y puedes:

| Tecla | Qué hace |
|---|---|
| **F10** | ejecuta la línea y pasa a la siguiente |
| **F11** | entra dentro de la función |
| **F5** | continúa hasta el siguiente punto de ruptura |

Mientras está parado, el panel **Variables** te enseña cuánto vale cada cosa **en ese instante**. Es incomparablemente mejor que llenar el código de `print`.

### 7.3 Leer el error de verdad

Cuando Python falla, te dice **el fichero, la línea y el tipo de error**. Lee siempre la **última** línea del mensaje: ahí está la causa.

```text
Traceback (most recent call last):
  File "programa.py", line 7, in <module>
    media = total / len(notas)
ZeroDivisionError: division by zero
```

Eso dice: línea 7, división entre cero → `len(notas)` vale 0 → la lista está vacía.

---

> **Reto rápido 7.** Provoca un `IndexError` a propósito (pide la posición 5 de una lista de 2), lee el *traceback* y di en qué línea está el fallo.

## 8. Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| `IndentationError` | indentación inconsistente | 4 espacios, siempre igual |
| El bucle no termina | no cambias la variable de la condición | modifícala dentro del `while` |
| `if x = 5` da error | `=` asigna, `==` compara | usa `==` |
| El `else` se ejecuta cuando no debe | condiciones en mal orden | ordena de más restrictiva a menos |
| `ZeroDivisionError` en medias | lista vacía | comprueba `len(lista) > 0` antes |
| `KeyError` | clave inexistente en el diccionario | usa `.get(clave, valor_por_defecto)` |
| El error se «traga» | `except:` genérico con `pass` | captura la excepción concreta |
| `range(1,5)` no llega al 5 | el final es exclusivo | usa `range(1, 6)` |

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


### Tema 1 · Decidir con `if`

**1.1.** Escribe `clasificar_nota(nota)` que devuelva `"Suspenso"`, `"Aprobado"`, `"Notable"` o `"Sobresaliente"`.
<details><summary>Solución</summary>

```python
def clasificar_nota(nota: float) -> str:
    """Clasifica una nota de 0 a 10."""
    if nota < 5:
        return "Suspenso"
    if nota < 7:
        return "Aprobado"
    if nota < 9:
        return "Notable"
    return "Sobresaliente"

print(clasificar_nota(4.9))   # -> Suspenso
print(clasificar_nota(5))     # -> Aprobado
print(clasificar_nota(9))     # -> Sobresaliente
```
</details>

**1.2.** Este código siempre dice «Menor». ¿Por qué? Arréglalo.

```python
edad = 20
if edad > 18:
    print("Mayor")
if edad < 18:
    print("Menor")
else:
    print("Menor")
```
<details><summary>Solución</summary>

```python
edad: int = 20

# El fallo: el else colgaba del SEGUNDO if, no del primero.
if edad >= 18:
    print("Mayor")   # -> Mayor
else:
    print("Menor")

# Una sola decision = un solo if/else. Encadenar ifs sueltos multiplica los casos
# y hace que se solapen sin darte cuenta.
```
</details>

**1.3.** Escribe `puede_votar(edad, nacionalidad)`: hace falta tener 18 o más **y** ser `"ES"`.
<details><summary>Solución</summary>

```python
def puede_votar(edad: int, nacionalidad: str) -> bool:
    """Indica si la persona puede votar."""
    return edad >= 18 and nacionalidad == "ES"

print(puede_votar(20, "ES"))   # -> True
print(puede_votar(17, "ES"))   # -> False
print(puede_votar(30, "FR"))   # -> False
```
</details>


### Tema 2 · Repetir con `while`

**2.1.** Muestra los números del 1 al 5 con un `while`.
<details><summary>Solución</summary>

```python
i: int = 1
while i <= 5:
    print(i, end=" ")
    i = i + 1     # SIN esta linea el bucle no termina nunca
print()   # -> 1 2 3 4 5
```
</details>

**2.2.** Escribe un `while` que sume números hasta que el usuario escriba `0`.
<details><summary>Solución</summary>

```python
total: int = 0
numero: int = int(input("Número (0 para acabar): "))

while numero != 0:
    total = total + numero
    numero = int(input("Número (0 para acabar): "))

print(f"Total: {total}")   # -> Total: 12
```
</details>

**2.3.** Este bucle es infinito. Encuentra el fallo:

```python
i = 0
while i < 3:
    print(i)
```
<details><summary>Solución</summary>

```python
i: int = 0
while i < 3:
    print(i)
    i = i + 1   # <- lo que faltaba: sin avanzar, la condicion nunca deja de cumplirse

# -> 0
# -> 1
# -> 2

# Regla: en todo while, pregúntate "¿qué línea hace que la condición acabe
# siendo falsa?". Si no la encuentras, es infinito.
```
</details>


### Tema 3 · Repetir con `for`

**3.1.** Recorre la lista `["Ada", "Alan", "Grace"]` y muestra cada nombre con su posición empezando en 1.
<details><summary>Solución</summary>

```python
nombres = ["Ada", "Alan", "Grace"]

for posicion, nombre in enumerate(nombres, start=1):
    print(f"{posicion}. {nombre}")

# -> 1. Ada
# -> 2. Alan
# -> 3. Grace
```
</details>

**3.2.** Suma los números del 1 al 100 con un `for` y `range()`.
<details><summary>Solución</summary>

```python
total: int = 0
for n in range(1, 101):   # 101 NO entra: range llega hasta el anterior
    total = total + n

print(total)   # -> 5050
```
</details>

**3.3.** Cuenta cuántas notas de la lista `[3.0, 6.5, 9.0, 4.0]` están aprobadas.
<details><summary>Solución</summary>

```python
notas = [3.0, 6.5, 9.0, 4.0]

aprobadas: int = 0
for nota in notas:
    if nota >= 5:
        aprobadas = aprobadas + 1

print(aprobadas)   # -> 2
```
</details>


### Tema 4 · Diccionarios

**4.1.** Crea un diccionario con el stock de tres productos y muestra el stock de uno de ellos.
<details><summary>Solución</summary>

```python
stock: dict[str, int] = {"camisa": 10, "gorra": 4, "pantalón": 7}

print(stock["gorra"])   # -> 4
print(len(stock))       # -> 3
```
</details>

**4.2.** Recorre el diccionario mostrando `producto: unidades`, y añade un producto nuevo.
<details><summary>Solución</summary>

```python
stock: dict[str, int] = {"camisa": 10, "gorra": 4}

stock["botas"] = 2   # añadir es asignar una clave que no existía

for producto, unidades in stock.items():
    print(f"{producto}: {unidades}")

# -> camisa: 10
# -> gorra: 4
# -> botas: 2
```
</details>

**4.3.** Consulta un producto que puede no existir sin que el programa reviente.
<details><summary>Solución</summary>

```python
stock: dict[str, int] = {"camisa": 10}

print(stock.get("gorra"))      # -> None
print(stock.get("gorra", 0))   # -> 0     valor por defecto: mucho más cómodo

# stock["gorra"] lanzaría KeyError. Con .get() decides tú qué pasa si no está.
```
</details>


### Tema 5 · `break` y `continue`

**5.1.** Busca el primer número negativo de una lista y sal del bucle en cuanto lo encuentres.
<details><summary>Solución</summary>

```python
numeros = [4, 7, -2, 9, -5]

for n in numeros:
    if n < 0:
        print(f"Primer negativo: {n}")   # -> Primer negativo: -2
        break
```
</details>

**5.2.** Suma solo los números positivos de una lista, saltándote el resto con `continue`.
<details><summary>Solución</summary>

```python
numeros = [4, -7, 2, -9, 5]

total: int = 0
for n in numeros:
    if n < 0:
        continue      # este no me interesa: al siguiente
    total = total + n

print(total)   # -> 11
```
</details>

**5.3.** ¿Cuál es la diferencia entre `break` y `continue`? Explícalo con una frase cada uno.
<details><summary>Solución</summary>

```text
break     -> ABANDONA el bucle entero. No se mira ni un elemento mas.
continue  -> se salta SOLO esta vuelta y sigue con la siguiente.

Truco para acordarse:
    break    = "he terminado, me voy"
    continue = "este no, el siguiente"
```
</details>


### Tema 6 · Excepciones

**6.1.** Pide un número por teclado y no dejes que el programa se caiga si escriben letras.
<details><summary>Solución</summary>

```python
texto: str = input("Número: ")

try:
    numero: int = int(texto)
    print(f"El doble es {numero * 2}")
except ValueError:
    print("Eso no es un número")   # -> Eso no es un número
```
</details>

**6.2.** Divide dos números controlando la división entre cero.
<details><summary>Solución</summary>

```python
def dividir(a: float, b: float) -> float:
    """División protegida; 0.0 si el divisor es cero."""
    try:
        return a / b
    except ZeroDivisionError:
        return 0.0

print(dividir(10, 2))   # -> 5.0
print(dividir(10, 0))   # -> 0.0
```
</details>

**6.3.** Este `except` es peligroso. ¿Por qué? Arréglalo:

```python
try:
    n = int(input())
except:
    pass
```
<details><summary>Solución</summary>

```python
try:
    n: int = int(input("Número: "))
    print(n)
except ValueError:
    print("Entrada no válida")   # -> Entrada no válida

# El except pelado se traga TODO: errores de tipado, de nombre, hasta el
# Ctrl+C. Y con 'pass' ademas no deja rastro: el programa falla en silencio
# y te vuelves loco buscando por que.
# Captura el error concreto que esperas y di algo cuando ocurra.
```
</details>


### Tema 7 · Depurar

**7.1.** Este código da un resultado raro. Añade `print()` para ver qué pasa en cada vuelta.

```python
total = 0
for n in [1, 2, 3]:
    total = n
print(total)
```
<details><summary>Solución</summary>

```python
total: int = 0
for n in [1, 2, 3]:
    total = n
    print(f"vuelta n={n} -> total={total}")   # el print que lo desvela

print("final:", total)   # -> final: 3

# -> vuelta n=1 -> total=1
# -> vuelta n=2 -> total=2
# -> vuelta n=3 -> total=3
# El fallo: total = n  machaca; lo correcto era  total = total + n
```
</details>

**7.2.** Localiza el fallo leyendo el traceback:

```
Traceback (most recent call last):
  File "a.py", line 3, in <module>
    print(notas[3])
IndexError: list index out of range
```
<details><summary>Solución</summary>

```text
El traceback se lee de ABAJO ARRIBA:

1. Ultima linea: el tipo de error -> IndexError: list index out of range
   Es decir: he pedido una posicion que no existe en la lista.
2. Justo encima: la linea culpable -> print(notas[3]) en a.py, linea 3.

Si la lista tiene 3 elementos, sus posiciones son 0, 1 y 2. La 3 no existe.
Solucion: usar notas[-1] para el ultimo, o comprobar len(notas) antes.
```
</details>

**7.3.** Escribe `elemento(lista, i)` que devuelva `None` en vez de reventar si la posición no existe.
<details><summary>Solución</summary>

```python
def elemento(lista: list[int], i: int) -> int | None:
    """Devuelve el elemento en la posición i, o None si no existe."""
    try:
        return lista[i]
    except IndexError:
        return None

print(elemento([1, 2, 3], 1))    # -> 2
print(elemento([1, 2, 3], 9))    # -> None
```
</details>


### Actividades guiadas

#### Actividad 1 — Clasificar una nota
Pide una nota y muestra su calificación (Insuficiente / Suficiente / Bien / Notable / Sobresaliente).
<details><summary>Solución</summary>

```python
nota: float = float(input("Nota: "))
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente")
```
</details>

#### Actividad 2 — Tabla de multiplicar
Pide un número y muestra su tabla del 1 al 10.
<details><summary>Solución</summary>

```python
n: int = int(input("Número: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```
</details>

#### Actividad 3 — Media de una lista con control
Calcula la media de una lista, pero devuelve `0.0` si está vacía.
<details><summary>Solución</summary>

```python
def media(numeros: list[float]) -> float:
    if len(numeros) == 0:
        return 0.0
    return sum(numeros) / len(numeros)
```
</details>

#### Actividad 4 — Entrada validada
Pide un número entero y no continúes hasta que sea válido.
<details><summary>Solución</summary>

```python
while True:
    try:
        numero: int = int(input("Número: "))
        break
    except ValueError:
        print("Entrada no válida")
print(f"Has escrito {numero}")
```
</details>

### Ejercicios propuestos

**E1 ○ · Mayor de dos.** `mayor(a: int, b: int) -> int`.
<details><summary>Solución</summary>

```python
def mayor(a: int, b: int) -> int:
    if a > b:
        return a
    return b
```
</details>

**E2 ○ · Contar hasta N.** Muestra los números del 1 a N, uno por línea.
<details><summary>Solución</summary>

```python
n: int = int(input())
for i in range(1, n + 1):
    print(i)
```
</details>

**E3 ◐ · Suma de pares.** `suma_pares(numeros: list[int]) -> int`.
<details><summary>Solución</summary>

```python
def suma_pares(numeros: list[int]) -> int:
    total = 0
    for n in numeros:
        if n % 2 == 0:
            total += n
    return total
```
</details>

**E4 ◐ · Buscar.** `posicion(numeros: list[int], buscado: int) -> int`: devuelve la posición o `-1`.
<details><summary>Pista</summary>Usa <code>enumerate</code> o <code>range(len(numeros))</code> y <code>return</code> en cuanto lo encuentres.</details>
<details><summary>Solución</summary>

```python
def posicion(numeros: list[int], buscado: int) -> int:
    for i, n in enumerate(numeros):
        if n == buscado:
            return i
    return -1
```
</details>

**E5 ◐ · División segura.** `dividir(a: float, b: float) -> float`: devuelve `0.0` si `b` es cero, usando `try/except`.
<details><summary>Solución</summary>

```python
def dividir(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return 0.0
```
</details>

**E6 ● · FizzBuzz.** Del 1 al N: múltiplos de 3 → `Fizz`, de 5 → `Buzz`, de ambos → `FizzBuzz`, resto → el número.
<details><summary>Pista</summary>Comprueba primero el caso de los dos a la vez.</details>
<details><summary>Solución</summary>

```python
n: int = int(input())
for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```
</details>

**E7 ◐ · Recuento de palabras.** `recuento(palabras: list[str]) -> dict[str, int]` devuelve cuántas veces aparece cada palabra.
<details><summary>Pista</summary>Recorre la lista y usa <code>.get(palabra, 0)</code> para partir de cero la primera vez que aparece cada una.</details>
<details><summary>Solución</summary>

```python
def recuento(palabras: list[str]) -> dict[str, int]:
    """Cuántas veces aparece cada palabra."""
    conteo: dict[str, int] = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo
```
</details>

**E8 ● · Validar una lista de notas.** `validar_notas(textos: list[str]) -> list[float]` convierte cada texto a número y **se queda solo** con los que son números válidos entre 0 y 10. Los demás se descartan sin que el programa se rompa.
<details><summary>Pista</summary>Un <code>try</code>/<code>except ValueError</code> dentro del bucle: si la conversión falla, <code>continue</code> y a por el siguiente.</details>
<details><summary>Solución</summary>

```python
def validar_notas(textos: list[str]) -> list[float]:
    """Notas válidas (0-10) de una lista de textos; descarta el resto."""
    validas: list[float] = []
    for texto in textos:
        try:
            nota = float(texto)
        except ValueError:
            continue
        if 0 <= nota <= 10:
            validas.append(nota)
    return validas
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

Toda la práctica de esta unidad se hace sobre un **proyecto base**: un analizador de notas que no se rompe con datos raros. Está montado
con la estructura real de un proyecto Python y trae una **batería de tests** que puedes
ejecutar en cualquier momento para ver si va todo bien.

**[Proyecto Gestor de notas →](../proyectos/ud3/README.md)**

```
proyecto-ud3/
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

## 12. Simulacro de examen

Cuando tengas el proyecto terminado, mídete: el **simulacro** es un examen de mentira con
**el mismo formato, tamaño y rúbrica** que el de verdad — y con los tests publicados.

**[Simulacro RA3 · Registro de pulsaciones →](../simulacros/ra3/README.md)** · 21 tests · 45–50 min

Hazlo **contrarreloj y sin ayuda**, como si fuera el examen. Al terminar, aplica la rúbrica
y tendrás una estimación bastante fiel de tu nota.

!!! warning "El examen de verdad va sin tests"
    Allí solo tendrás los **docstrings** y unos ejemplos. Por eso, en el simulacro, intenta
    resolver cada función leyendo solo su docstring y mira el test únicamente cuando falle.

---

---

## 13. Retos opcionales

- **R1.** Menú completo: añadir notas, ver media, listar y salir, con toda la entrada validada.
- **R2.** Adivina el número: el programa piensa uno con `random.randint(1, 100)` y te dice «mayor» o «menor» hasta acertar.
- **R3.** Cuenta cuántas veces aparece cada palabra en una frase, usando un diccionario.

- **R4.** Menú de consola con cuatro opciones que se repita hasta que el usuario elija salir, sin que ninguna entrada rara lo rompa.
- **R5.** Adivina el número: el programa piensa uno del 1 al 100 y va diciendo «mayor» o «menor» hasta acertar. Cuenta los intentos.
- **R6.** Cuenta las vocales de una frase usando un diccionario, y muestra el recuento ordenado de mayor a menor.
---

---

## 14. Autoevaluación rápida

<details><summary>1. ¿Qué imprime <code>for i in range(3)</code>?</summary><code>0</code>, <code>1</code>, <code>2</code>.</details>
<details><summary>2. ¿Cuándo usar <code>while</code> en vez de <code>for</code>?</summary>Cuando no sabes cuántas vueltas hará: repites hasta que ocurra algo.</details>
<details><summary>3. Diferencia entre <code>break</code> y <code>continue</code>.</summary><code>break</code> sale del bucle; <code>continue</code> salta a la siguiente vuelta.</details>
<details><summary>4. ¿Qué excepción lanza <code>int("hola")</code>?</summary><code>ValueError</code>.</details>
<details><summary>5. ¿Por qué es mala idea <code>except:</code> a secas?</summary>Atrapa todos los errores, incluidos los tuyos de programación, y los oculta.</details>
<details><summary>6. ¿Qué falla en <code>if edad >= 18 and <= 65</code>?</summary>Hay que repetir la variable: <code>edad >= 18 and edad <= 65</code>.</details>

---

---

## 15. Glosario

| Término | Definición |
|---|---|
| **Estructura de selección** | `if`/`elif`/`else`: elige qué código ejecutar. |
| **Estructura de repetición** | `while`/`for`: repite instrucciones. |
| **Iterar** | Recorrer los elementos de una colección. |
| **Acumulador** | Variable que va sumando dentro de un bucle. |
| **Excepción** | Error en tiempo de ejecución que interrumpe el programa. |
| **`try` / `except`** | Bloque que intenta algo y reacciona si falla. |
| **Diccionario** | Colección de pares clave → valor. |
| **Punto de ruptura** | Marca que detiene el programa en el depurador. |

---

---

## 16. Cómo se evalúa esta unidad (RA3)

El examen es **100 % práctico**: se entrega un proyecto con las funciones vacías y una
especificación, y hay que escribir el código.

**La nota sale solo de los casos de prueba.** No hay puntos por presentación ni por
esfuerzo: cada apartado del examen vale en proporción a los casos que tiene, de modo que
**todos los casos valen lo mismo**.

`nota del apartado = (casos superados ÷ casos del apartado) × puntos del apartado`

`nota del examen = suma de los apartados`

### Así es el examen

**Análisis de temperaturas** · entrega `src/temperaturas.py` · **50 min**

| # | Apartado | Casos | Puntos |
|:---:|---|:---:|:---:|
| **A** | `media()` | 3 | **1,58** |
| **B** | `maxima()` | 3 | **1,58** |
| **C** | `dias_calurosos()` | 3 | **1,58** |
| **D** | `clasificar()` | 6 | **3,16** |
| **E** | `a_numero()` | 4 | **2,10** |
| | **TOTAL** | **19** | **10,00** |

Esta tabla viene en el enunciado, así que sabes desde el primer minuto **qué vale cada
parte** y por dónde empezar si vas justo de tiempo.

!!! warning "El examen se reparte sin tests"
    La carpeta `tests/` viene vacía. La especificación son los **docstrings** de cada
    función y los ejemplos del enunciado. Por eso conviene que en el simulacro te
    acostumbres a resolver leyendo el docstring y no el test.

### Así se corrige

Alguien que entrega el examen con **17 de los 19 casos** superados
—se le ha escapado el apartado **C**, donde falla 2 de
3 casos—:

| # | Apartado | Casos superados | Puntos |
|:---:|---|:---:|---|
| A | `media()` | 3 / 3 | 1,58 / 1,58 |
| B | `maxima()` | 3 / 3 | 1,58 / 1,58 |
| C | `dias_calurosos()` | 1 / 3 | 0,53 / 1,58  ← |
| D | `clasificar()` | 6 / 6 | 3,16 / 3,16 |
| E | `a_numero()` | 4 / 4 | 2,10 / 2,10 |
| | | | **NOTA: 8,95** |

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
