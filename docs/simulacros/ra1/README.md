# Simulacro tipo test · RA1 — Elementos del lenguaje

El examen de esta unidad es un **test de 12 preguntas de opción múltiple sobre
código**: se te da un fragmento y tienes que decir qué imprime, qué error lanza o cuál de
cuatro versiones de una función es la correcta. **Ninguna pregunta es de definiciones.**

Aquí tienes **48 preguntas de práctica**, 8 por cada tema de la unidad, con la
respuesta y la explicación desplegables.

## Cómo sacarle partido

1. Haz **un tema cada vez**, justo después de leerlo y hacer sus ejercicios.
2. Contesta **sin ejecutar el código**. La gracia está en leerlo.
3. Despliega la respuesta y lee la explicación, aciertes o falles.
4. Después pasa por Python las que hayas fallado y compruébalo.

## Cómo se puntúa en el examen

| | |
|---|---|
| Acierto | **+0,83** puntos |
| Error | **−0,28** puntos |
| En blanco | 0 |

`nota = (aciertos − errores ÷ 3) × 0,83`, con un mínimo de 0.

Se resta porque hay cuatro opciones: **marcar al azar no compensa**. Si dudas entre dos,
marca; si no tienes ni idea, déjalo en blanco.

---


## Tu primer programa

**1.** ¿Qué imprime este programa?

```python
producto = "Camisa"
mensaje = "Has elegido: " + producto
print(mensaje)
```

- **a)** `Camisa`
- **b)** `TypeError`
- **c)** `Has elegido: Camisa`
- **d)** `Has elegido: producto`

<details><summary>Respuesta</summary>

**c)** `Has elegido: Camisa`

El `+` entre textos los pega. La variable `producto` se sustituye por su valor.
</details>

**2.** ¿Qué error lanza este programa?

```python
print(mensaje)
producto = "Camisa"
mensaje = "Has elegido: " + producto
```

- **a)** `NameError`
- **b)** `TypeError`
- **c)** `ValueError`
- **d)** `SyntaxError`

<details><summary>Respuesta</summary>

**a)** `NameError`

El `print` va antes de crear `mensaje`. Python ejecuta línea a línea: cuando llega al print, ese nombre todavía no existe.
</details>

**3.** ¿Qué imprime?

```python
unidades = 3
print(unidades, "unidades")
```

- **a)** `3unidades`
- **b)** `3 ⏎ unidades`
- **c)** `3 unidades`
- **d)** `TypeError`

<details><summary>Respuesta</summary>

**c)** `3 unidades`

`print` con varios argumentos separados por comas los muestra en una línea con un espacio entre ellos.
</details>

**4.** ¿Qué error lanza?

```python
unidades = 3
print(unidades + " unidades")
```

- **a)** `SyntaxError`
- **b)** `ValueError`
- **c)** `NameError`
- **d)** `TypeError`

<details><summary>Respuesta</summary>

**d)** `TypeError`

Con `+` no se pueden pegar un número y un texto. Con comas en el `print` sí funcionaría, o convirtiendo con `str()`.
</details>

**5.** ¿Qué imprime?

```python
print("-" * 8)
```

- **a)** `- * 8`
- **b)** `-`
- **c)** `8`
- **d)** `--------`

<details><summary>Respuesta</summary>

**d)** `--------`

Multiplicar un texto por un número lo repite. Es el truco para dibujar la línea separadora de un ticket.
</details>

**6.** ¿Qué imprime este programa?

```python
print("Ticket")
print("-" * 8)
print("Camisa")
```

- **a)** `Ticket ⏎ -------- ⏎ Camisa`
- **b)** `Ticket Camisa`
- **c)** `TypeError`
- **d)** `Ticket ⏎ Camisa`

<details><summary>Respuesta</summary>

**a)** `Ticket ⏎ -------- ⏎ Camisa`

Cada `print` escribe en una línea nueva. Multiplicar un texto lo repite, que es cómo se dibuja la línea separadora.
</details>

**7.** ¿Qué imprime? Fíjate en el orden de las líneas.

```python
unidades = 3
precio = 19.95
base = unidades * precio
print(round(base, 2))
```

- **a)** `0`
- **b)** `59.85`
- **c)** `NameError`
- **d)** `None`

<details><summary>Respuesta</summary>

**b)** `59.85`

Python ejecuta de arriba abajo. Cuando llega al `print`, `base` ya tiene el valor calculado en la línea anterior.
</details>

**8.** ¿Qué error lanza este programa?

```python
producto = "Camisa"
print(producto
```

- **a)** `TypeError`
- **b)** `NameError`
- **c)** `SyntaxError`
- **d)** `IndentationError`

<details><summary>Respuesta</summary>

**c)** `SyntaxError`

Falta el paréntesis de cierre. El error de sintaxis se detecta antes de ejecutar nada, y suele estar en la línea anterior a la que señala Python.
</details>


## Variables y tipos

**9.** ¿Qué imprime?

```python
a = 0.1 + 0.2
b = 0.3

print(round(a, 10) == b)
```

- **a)** `TypeError`
- **b)** `False`
- **c)** `True`
- **d)** `0.30000000000000004`

<details><summary>Respuesta</summary>

**c)** `True`

</details>

**10.** ¿Qué error lanza?

```python
base = 100.0
total = base * (1 + iva / 100)
IVA = 21
print(total)
```

- **a)** `TypeError`
- **b)** `NameError`
- **c)** `SyntaxError`
- **d)** `ValueError`

<details><summary>Respuesta</summary>

**b)** `NameError`

</details>

**11.** ¿Qué imprime?

```python
IVA = 21

precio = 10.0
con_iva = precio * (1 + IVA / 100)
precio = 20.0

print(f"{con_iva:.2f} {precio * (1 + IVA / 100):.2f}")
```

- **a)** `12.10 24.20`
- **b)** `12.10 12.10`
- **c)** `10.00 24.20`
- **d)** `24.20 24.20`

<details><summary>Respuesta</summary>

**a)** `12.10 24.20`

</details>

**12.** ¿Qué imprime?

```python
a = 5
b = 9
copia = a

a, b = b, a

print(a, b, copia + 4)
```

- **a)** `5 9 9`
- **b)** `5 9 5`
- **c)** `9 5 9`
- **d)** `9 5 5`

<details><summary>Respuesta</summary>

**c)** `9 5 9`

</details>

**13.** ¿Qué imprime?

```python
precio = 19.95
precio = 24.50
print(precio)
```

- **a)** `ValueError`
- **b)** `24.50`
- **c)** `19.95`
- **d)** `24.5`

<details><summary>Respuesta</summary>

**d)** `24.5`

Python no guarda los ceros de adorno: `24.50` y `24.5` son el mismo número. Para verlo con dos decimales hay que dar formato con `:.2f`.
</details>

**14.** ¿Qué imprime?

```python
resultado = 6 / 3
print(type(resultado))
```

- **a)** `<class 'int'>`
- **b)** `<class 'bool'>`
- **c)** `<class 'str'>`
- **d)** `<class 'float'>`

<details><summary>Respuesta</summary>

**d)** `<class 'float'>`

La división `/` devuelve `float` siempre, aunque el resultado sea exacto. Para obtener un entero hay que usar `//`.
</details>

**15.** ¿Qué imprime?

```python
a = "Camisa"
b = 19.95
a, b = b, a
print(a, b)
```

- **a)** `TypeError`
- **b)** `19.95 Camisa`
- **c)** `19.95 19.95`
- **d)** `Camisa 19.95`

<details><summary>Respuesta</summary>

**b)** `19.95 Camisa`

El intercambio simultáneo `a, b = b, a` cambia los dos valores a la vez, sin necesidad de una variable auxiliar.
</details>

**16.** ¿Qué imprime?

```python
hay_stock = 3 > 0
print(hay_stock, type(hay_stock))
```

- **a)** `False <class 'bool'>`
- **b)** `True <class 'int'>`
- **c)** `True <class 'bool'>`
- **d)** `1 <class 'int'>`

<details><summary>Respuesta</summary>

**c)** `True <class 'bool'>`

El resultado de una comparación es un valor de tipo `bool`: `True` o `False`.
</details>


## Operadores

**17.** ¿Qué imprime?

```python
IVA = 21

precio_unidad = 19.95
unidades = 3

subtotal = unidades * precio_unidad
iva = subtotal * IVA / 100

print(f"Subtotal: {subtotal:.2f} | IVA: {iva:.2f}")
```

- **a)** `Subtotal: 59.85 | IVA: 72.42`
- **b)** `Subtotal: 59.85 | IVA: 12.57`
- **c)** `Subtotal: 60.00 | IVA: 12.60`
- **d)** `Subtotal: 59.85 | IVA: 12.56`

<details><summary>Respuesta</summary>

**b)** `Subtotal: 59.85 | IVA: 12.57`

</details>

**18.** ¿Qué imprime?

```python
precio = 1.33
unidades = 2.25

importe = precio * unidades
print(f"{importe:.2f}")
```

- **a)** `3`
- **b)** `2.99`
- **c)** `3.00`
- **d)** `2.9925`

<details><summary>Respuesta</summary>

**b)** `2.99`

</details>

**19.** ¿Qué imprime este programa?

```python
PRECIO_CENTIMOS = 251

dinero = 800
unidades = dinero // PRECIO_CENTIMOS
resto = dinero % PRECIO_CENTIMOS

print(f"Quedan {unidades} unidades y sobran {resto} centimos")
```

- **a)** `Quedan 3 unidades y sobran 53 centimos`
- **b)** `Quedan 4 unidades y sobran 47 centimos`
- **c)** `Quedan 3 unidades y sobran 0.47 centimos`
- **d)** `Quedan 3 unidades y sobran 47 centimos`

<details><summary>Respuesta</summary>

**d)** `Quedan 3 unidades y sobran 47 centimos`

</details>

**20.** ¿Qué imprime?

```python
centimos = 287

m100 = centimos // 100
centimos = centimos % 100
m50 = centimos // 50
centimos = centimos % 50
m20 = centimos // 20
centimos = centimos % 20

print(m100, m50, m20, centimos)
```

- **a)** `2 1 1 17`
- **b)** `2 0 1 17`
- **c)** `2 1 0 17`
- **d)** `2 1 1 7`

<details><summary>Respuesta</summary>

**a)** `2 1 1 17`

</details>

**21.** ¿Qué imprime?

```python
a = 2
b = 3
c = 5

resultado = a + b * c - a ** b // c
print(resultado)
```

- **a)** `27`
- **b)** `21`
- **c)** `16`
- **d)** `17`

<details><summary>Respuesta</summary>

**c)** `16`

</details>

**22.** ¿Qué imprime?

```python
total = -7
partes = 2

print(total // partes, total % partes - 2)
```

- **a)** `-3 -1`
- **b)** `-3 1`
- **c)** `-4 1`
- **d)** `-4 -1`

<details><summary>Respuesta</summary>

**d)** `-4 -1`

</details>

**23.** ¿Qué imprime?

```python
edad = 17
carnet = True
acompanado = True

puede = edad >= 18 and carnet or acompanado
print(puede)
```

- **a)** `TypeError`
- **b)** `False`
- **c)** `None`
- **d)** `True`

<details><summary>Respuesta</summary>

**d)** `True`

</details>

**24.** ¿Qué imprime?

```python
edad = 17
carnet = True
acompanado = True

puede = edad >= 18 and (carnet or acompanado)
print(puede)
```

- **a)** `False`
- **b)** `TypeError`
- **c)** `None`
- **d)** `True`

<details><summary>Respuesta</summary>

**a)** `False`

</details>


## Leer y convertir

**25.** El usuario escribe `1.234,56`. ¿Qué imprime?

```python
texto = "1.234,56"

limpio = texto.replace(".", "")
limpio = limpio.replace(",", ".")
valor = float(limpio)

print(f"{valor:,.2f}")
```

- **a)** `ValueError`
- **b)** `1,234.56`
- **c)** `1234,56`
- **d)** `1.23`

<details><summary>Respuesta</summary>

**b)** `1,234.56`

</details>

**26.** ¿Qué error lanza este programa?

```python
cantidad = "12 unidades"
n = int(cantidad)
print(n * 2)
```

- **a)** `SyntaxError`
- **b)** `ValueError`
- **c)** `TypeError`
- **d)** `AttributeError`

<details><summary>Respuesta</summary>

**b)** `ValueError`

</details>

**27.** ¿Qué imprime?

```python
entrada_1 = "15"
entrada_2 = "2"

media = int(entrada_1) // int(entrada_2)
print(media)
```

- **a)** `7`
- **b)** `8`
- **c)** `7.5`
- **d)** `TypeError`

<details><summary>Respuesta</summary>

**a)** `7`

</details>

**28.** ¿Qué imprime?

```python
entrada_1 = "15"
entrada_2 = "2"

media = int(entrada_1) / int(entrada_2)
print(media)
```

- **a)** `'15' / '2'`
- **b)** `8`
- **c)** `7`
- **d)** `7.5`

<details><summary>Respuesta</summary>

**d)** `7.5`

</details>

**29.** ¿Qué imprime?

```python
edad = "20"
siguiente = edad + "5"
print(siguiente)
```

- **a)** `205`
- **b)** `TypeError`
- **c)** `2005`
- **d)** `25`

<details><summary>Respuesta</summary>

**a)** `205`

</details>

**30.** ¿Qué imprime?

```python
a = "10"
b = 10

print(a == b, int(a) == b)
```

- **a)** `False False`
- **b)** `True True`
- **c)** `True False`
- **d)** `False True`

<details><summary>Respuesta</summary>

**d)** `False True`

</details>

**31.** ¿Cuál de estos cuatro resultados **no** es el que devuelve la función?

```python
def a_entero(texto: str) -> int:
    """Convierte un texto a número entero."""
    return int(texto)
```

- **a)** `a_entero('0')` devuelve `0`
- **b)** `a_entero('-3')` devuelve `-3`
- **c)** `a_entero('07')` devuelve `0`
- **d)** `a_entero('7')` devuelve `7`

<details><summary>Respuesta</summary>

**c)** `a_entero('07') → 0`

</details>

**32.** El usuario puede escribir el decimal con coma o con punto. ¿Cuál convierte bien los cuatro casos?

**a)**

```python
def a_decimal(texto: str) -> float:
    """Convierte a float admitiendo coma o punto decimal."""
    return float(texto.replace(".", ","))
```

**b)**

```python
def a_decimal(texto: str) -> float:
    """Convierte a float admitiendo coma o punto decimal."""
    return float(texto.replace(",", "."))
```

**c)**

```python
def a_decimal(texto: str) -> float:
    """Convierte a float admitiendo coma o punto decimal."""
    return float(texto.strip(","))
```

**d)**

```python
def a_decimal(texto: str) -> float:
    """Convierte a float admitiendo coma o punto decimal."""
    return float(texto)
```


<details><summary>Respuesta</summary>

**b)** `def a_decimal(texto: str) -> float: ⏎     """Convierte a float admitiendo coma o punto decimal.""" ⏎     return float(texto.replace(",", "."))`

</details>


## Formato de salida

**33.** ¿Qué imprime? (los puntos marcan los espacios)

```python
producto = "Camisa"
unidades = 2
precio = 19.9

linea = f"{producto:<12}{unidades:>1} x {precio:>6.2f} = {unidades * precio:>7.2f}"
print(linea.replace(" ", "."))
```

- **a)** `Camisa......2.x..19.90.=...39.80`
- **b)** `Camisa......2 x..19.90 =...39.80`
- **c)** `Camisa......2.x..19.9..=...39.8.`
- **d)** `Camisa...2.x.19.90.=.39.80`

<details><summary>Respuesta</summary>

**a)** `Camisa......2.x..19.90.=...39.80`

</details>

**34.** ¿Qué imprime?

```python
print(f"{2.175:.2f}", f"{2.185:.2f}")
```

- **a)** `2.17 2.19`
- **b)** `2.18 2.18`
- **c)** `2.18 2.19`
- **d)** `2.17 2.18`

<details><summary>Respuesta</summary>

**a)** `2.17 2.19`

</details>

**35.** ¿Qué imprime?

```python
importe = 1234567.891
ratio = 0.1567

print(f"{importe:,.2f} | {ratio:.1%}")
```

- **a)** `1.234.567,89 | 15.7%`
- **b)** `1,234,567.89 | 15.7%`
- **c)** `1234567.89 | 15.67%`
- **d)** `1,234,567.89 | 0.2%`

<details><summary>Respuesta</summary>

**b)** `1,234,567.89 | 15.7%`

</details>

**36.** ¿Qué imprime?

```python
cuota = 39.9
material = 12.0
descuento = -5.5

total = cuota + material + descuento
print(f"Total: {total:>8.2f} EUR")
```

- **a)** `Total: 46.40 EUR`
- **b)** `Total:     46.4 EUR`
- **c)** `Total:46.40 EUR`
- **d)** `Total:    46.40 EUR`

<details><summary>Respuesta</summary>

**d)** `Total:    46.40 EUR`

</details>

**37.** ¿Qué imprime?

```python
aciertos = 2
total = 3

print(f"{aciertos / total:.2f}")
```

- **a)** `2/3`
- **b)** `0.7`
- **c)** `0.66`
- **d)** `0.67`

<details><summary>Respuesta</summary>

**d)** `0.67`

</details>

**38.** ¿Qué imprime?

```python
nota = 7

print(f"|{nota:>5.2f}|")
```

- **a)** `|    7|`
- **b)** `| 7.0 |`
- **c)** `| 7.00|`
- **d)** `|7.00 |`

<details><summary>Respuesta</summary>

**c)** `| 7.00|`

</details>

**39.** ¿Cuál de estos cuatro resultados **no** es el que devuelve la función?

```python
def formatear(etiqueta: str, valor: float) -> str:
    """Línea del tipo 'Total: 30.00 €'."""
    return f"{etiqueta}: {valor:.2f} €"
```

- **a)** `formatear('X', 0.0)` devuelve `'X: 0.00 €'`
- **b)** `formatear('Base', 1234.5)` devuelve `'Base: 1234.5 €'`
- **c)** `formatear('Total', 1.2)` devuelve `'Total: 1.20 €'`
- **d)** `formatear('Subtotal', 30.0)` devuelve `'Subtotal: 30.00 €'`

<details><summary>Respuesta</summary>

**b)** `formatear('Base', 1234.5) → 'Base: 1234.5 €'`

</details>

**40.** ¿Cuál devuelve la duración formateada exactamente como `1h 02m 05s`?

**a)**

```python
def duracion(segundos: int) -> str:
    """Duración con dos dígitos en minutos y segundos."""
    h = segundos // 3600
    resto = segundos % 3600
    return f"{h}h {resto // 60}m {resto % 60}s"
```

**b)**

```python
def duracion(segundos: int) -> str:
    """Duración con dos dígitos en minutos y segundos."""
    h = segundos / 3600
    resto = segundos % 3600
    return f"{h}h {resto // 60:02d}m {resto % 60:02d}s"
```

**c)**

```python
def duracion(segundos: int) -> str:
    """Duración con dos dígitos en minutos y segundos."""
    h = segundos // 3600
    return f"{h}h {segundos // 60:02d}m {segundos % 60:02d}s"
```

**d)**

```python
def duracion(segundos: int) -> str:
    """Duración con dos dígitos en minutos y segundos."""
    h = segundos // 3600
    resto = segundos % 3600
    return f"{h}h {resto // 60:02d}m {resto % 60:02d}s"
```


<details><summary>Respuesta</summary>

**d)** `def duracion(segundos: int) -> str: ⏎     """Duración con dos dígitos en minutos y segundos.""" ⏎     h = segundos // 3600 ⏎     resto = segundos % 3600 ⏎     return f"{h}h {resto // 60:02d}m {resto % 60:02d}s"`

</details>


## Constantes, nombres y comentarios

**41.** ¿Qué imprime este programa?

```python
IVA = 21
DESCUENTO = 15

precio = 80.0
unidades = 3

base = unidades * precio
base = base - base * DESCUENTO / 100
total = base * (1 + IVA / 100)

print(f"{total:.2f}")
```

- **a)** `205.70`
- **b)** `246.83`
- **c)** `246.84`
- **d)** `290.40`

<details><summary>Respuesta</summary>

**c)** `246.84`

</details>

**42.** El descuento se aplica **antes** del IVA. ¿Qué imprime?

```python
IVA = 21
DESCUENTO = 10

base = 100.0
con_descuento = base * (1 - DESCUENTO / 100)
total = con_descuento * (1 + IVA / 100)

print(f"{total:.2f}")
```

- **a)** `121.00`
- **b)** `108.89`
- **c)** `110.00`
- **d)** `108.90`

<details><summary>Respuesta</summary>

**d)** `108.90`

</details>

**43.** ¿Qué imprime este programa?

```python
IVA = 21

def subir():
    global IVA
    IVA = 50

subir()
print(IVA)
```

- **a)** `TypeError`
- **b)** `50`
- **c)** `21`
- **d)** `SyntaxError`

<details><summary>Respuesta</summary>

**b)** `50`

</details>

**44.** Esta función está en tu proyecto. ¿Cuál de estos cuatro resultados **no** es el que devuelve?

```python
IVA = 21


def calcular_iva(base: float) -> float:
    """Importe del IVA sobre la base."""
    return base * IVA / 100
```

- **a)** `calcular_iva(0.0)` devuelve `0.0`
- **b)** `calcular_iva(30.0)` devuelve `6.3`
- **c)** `calcular_iva(100.0)` devuelve `21.0`
- **d)** `calcular_iva(23.1)` devuelve `4.85`

<details><summary>Respuesta</summary>

**d)** `calcular_iva(23.1) → 4.85`

</details>

**45.** ¿Cuál de estos cuatro resultados **no** es el que devuelve la función?

```python
IVA = 21


def desglose(unidades: int, precio: float) -> tuple[float, float, float]:
    """Base, IVA y total, redondeados a 2 decimales."""
    base = unidades * precio
    iva = base * IVA / 100
    return round(base, 2), round(iva, 2), round(base + iva, 2)
```

- **a)** `desglose(0, 5.0)` devuelve `(0.0, 0.0, 0.0)`
- **b)** `desglose(3, 9.99)` devuelve `(29.97, 6.29, 36.27)`
- **c)** `desglose(1, 1.0)` devuelve `(1.0, 0.21, 1.21)`
- **d)** `desglose(2, 10.0)` devuelve `(20.0, 4.2, 24.2)`

<details><summary>Respuesta</summary>

**b)** `desglose(3, 9.99) → (29.97, 6.29, 36.27)`

</details>

**46.** Necesitas una función que aplique un descuento en porcentaje. ¿Cuál cumple los cuatro casos?

**a)**

```python
DESCUENTO = 15


def rebajar(precio: float) -> float:
    """Precio con el descuento aplicado, a 2 decimales."""
    return round(precio / (1 + DESCUENTO / 100), 2)
```

**b)**

```python
DESCUENTO = 15


def rebajar(precio: float) -> float:
    """Precio con el descuento aplicado, a 2 decimales."""
    return round(precio * (1 - DESCUENTO / 100), 2)
```

**c)**

```python
DESCUENTO = 15


def rebajar(precio: float) -> float:
    """Precio con el descuento aplicado, a 2 decimales."""
    return round(precio - DESCUENTO, 2)
```

**d)**

```python
DESCUENTO = 15


def rebajar(precio: float) -> float:
    """Precio con el descuento aplicado, a 2 decimales."""
    return round(precio * DESCUENTO / 100, 2)
```


<details><summary>Respuesta</summary>

**b)** `DESCUENTO = 15 ⏎  ⏎  ⏎ def rebajar(precio: float) -> float: ⏎     """Precio con el descuento aplicado, a 2 decimales.""" ⏎     return round(precio * (1 - DESCUENTO / 100), 2)`

</details>

**47.** ¿Qué imprime?

```python
IVA = 21

base = 59.85
total = base + base * IVA / 100
print(f"{total:.2f}")
```

- **a)** `59.85`
- **b)** `12.57`
- **c)** `TypeError`
- **d)** `72.42`

<details><summary>Respuesta</summary>

**d)** `72.42`

La constante se usa dentro del cálculo, igual que cualquier otra variable. Las MAYÚSCULAS son una señal para quien lee, no una regla del lenguaje.
</details>

**48.** ¿Qué error lanza este programa?

```python
for = 3
print(for)
```

- **a)** `TypeError`
- **b)** `ValueError`
- **c)** `SyntaxError`
- **d)** `NameError`

<details><summary>Respuesta</summary>

**c)** `SyntaxError`

`for` es una palabra reservada del lenguaje: no se puede usar como nombre de variable. Hay que renombrarla.
</details>
