# Simulacro tipo test · RA2 — Funciones y librerías

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


## Definir y llamar funciones

**1.** ¿Qué imprime este programa?

```python
IVA = 21


def con_iva(precio):
    print(round(precio * (1 + IVA / 100), 2))


resultado = con_iva(25.0)
print(resultado)
```

- **a)** `30.25 ⏎ 30.25`
- **b)** `30.25 ⏎ None`
- **c)** `None ⏎ 30.25`
- **d)** `25 ⏎ None`

<details><summary>Respuesta</summary>

**b)** `30.25 ⏎ None`

</details>

**2.** ¿Qué error lanza este programa?

```python
def media(notas):
    print(sum(notas) / len(notas))


total = media([5.0, 7.0]) * 2
print(total)
```

- **a)** `TypeError`
- **b)** `NameError`
- **c)** `AttributeError`
- **d)** `ValueError`

<details><summary>Respuesta</summary>

**a)** `TypeError`

</details>

**3.** ¿Qué imprime?

```python
def base(unidades, precio):
    return unidades * precio


def con_iva(importe):
    return round(importe * 1.21, 2)


print(con_iva(base(3, 10.0)))
```

- **a)** `None`
- **b)** `18.15`
- **c)** `36.3`
- **d)** `TypeError`

<details><summary>Respuesta</summary>

**c)** `36.3`

</details>

**4.** ¿Qué imprime?

```python
def medidas(base, altura):
    """Área y perímetro de un rectángulo."""
    return base * altura, 2 * (base + altura)


print(medidas(4.0, 3.0))
```

- **a)** `12.0 14.0`
- **b)** `12.0`
- **c)** `(12.0, 14.0)`
- **d)** `[12.0, 14.0]`

<details><summary>Respuesta</summary>

**c)** `(12.0, 14.0)`

</details>

**5.** ¿Qué imprime?

```python
def medidas(base, altura):
    return base * altura, 2 * (base + altura)


area, perimetro = medidas(4.0, 3.0)
print(area, perimetro)
```

- **a)** `(12.0, 14.0)`
- **b)** `12.0`
- **c)** `TypeError`
- **d)** `12.0 14.0`

<details><summary>Respuesta</summary>

**d)** `12.0 14.0`

</details>

**6.** ¿Qué imprime?

```python
def doble(n):
    return n * 2
    return n * 4


print(doble(5))
```

- **a)** `10`
- **b)** `None`
- **c)** `10\n20`
- **d)** `20`

<details><summary>Respuesta</summary>

**a)** `10`

</details>

**7.** ¿Qué imprime?

```python
def importe(unidades, precio):
    """Importe de una línea."""
    return unidades * precio


resultado = importe(3, 19.95)
print(round(resultado, 2))
```

- **a)** `TypeError`
- **b)** `None`
- **c)** `59.85`
- **d)** `3`

<details><summary>Respuesta</summary>

**c)** `59.85`

La función devuelve con `return`, así que el resultado se puede guardar y usar.
</details>

**8.** ¿Qué imprime?

```python
def saludar(nombre):
    print(f"Hola, {nombre}")


saludar("Ada")
saludar("Alan")
```

- **a)** `Hola, Ada ⏎ Hola, Alan`
- **b)** `Hola, Ada`
- **c)** `Hola, Alan`
- **d)** `None`

<details><summary>Respuesta</summary>

**a)** `Hola, Ada ⏎ Hola, Alan`

Una función se escribe una vez y se llama tantas veces como haga falta. Ese es todo el motivo de usarlas.
</details>


## Parámetros

**9.** ¿Qué imprime?

```python
def con_impuesto(base, tipo=21):
    """Importe con el impuesto aplicado."""
    return base * (1 + tipo / 100)


print(f"{con_impuesto(100.0):.2f} | {con_impuesto(100.0, 30):.2f}")
```

- **a)** `121.00 | 121.00`
- **b)** `TypeError`
- **c)** `121.00 | 130.00`
- **d)** `130.00 | 130.00`

<details><summary>Respuesta</summary>

**c)** `121.00 | 130.00`

</details>

**10.** ¿Qué imprime?

```python
def con_impuesto(base, tipo=21):
    return base * (1 + tipo / 100)


print(f"{con_impuesto(tipo=21, base=100.0):.2f}")
```

- **a)** `121.00`
- **b)** `100.00`
- **c)** `TypeError`
- **d)** `110.00`

<details><summary>Respuesta</summary>

**a)** `121.00`

</details>

**11.** ¿Qué error lanza?

```python
def linea(etiqueta="Total", valor):
    return f"{etiqueta}: {valor:.2f}"


print(linea("Base", 10.0))
```

- **a)** `NameError`
- **b)** `TypeError`
- **c)** `SyntaxError`
- **d)** `ValueError`

<details><summary>Respuesta</summary>

**c)** `SyntaxError`

</details>

**12.** ¿Qué error lanza?

```python
def area_triangulo(base, altura):
    """Área de un triángulo."""
    return base * altura / 2


print(area_triangulo(10.0))
```

- **a)** `TypeError`
- **b)** `ValueError`
- **c)** `IndexError`
- **d)** `NameError`

<details><summary>Respuesta</summary>

**a)** `TypeError`

</details>

**13.** ¿Qué imprime?

```python
def potencia(base, exponente=3):
    return float(base ** exponente)


print(potencia(2), potencia(2, 10))
```

- **a)** `8.0 8.0`
- **b)** `1024.0 1024.0`
- **c)** `8.0 1024.0`
- **d)** `TypeError`

<details><summary>Respuesta</summary>

**c)** `8.0 1024.0`

</details>

**14.** ¿Qué imprime?

```python
def acumular(lista, valor):
    """Añade el valor a la lista."""
    lista.append(valor)
    return lista


original = [1, 2]
nueva = acumular(original, 3)
print(original)
print(nueva)
```

- **a)** `[1, 2] ⏎ [1, 2, 3]`
- **b)** `[1, 2] ⏎ [1, 2]`
- **c)** `TypeError`
- **d)** `[1, 2, 3] ⏎ [1, 2, 3]`

<details><summary>Respuesta</summary>

**d)** `[1, 2, 3] ⏎ [1, 2, 3]`

</details>

**15.** ¿Qué imprime?

```python
def linea(valor, etiqueta="Total"):
    return f"{etiqueta}: {valor:.2f}"


print(linea(30.0))
```

- **a)** `Total: 30.00`
- **b)** `Total: 30`
- **c)** `TypeError`
- **d)** `Base: 30.00`

<details><summary>Respuesta</summary>

**a)** `Total: 30.00`

El parámetro con valor por defecto se usa cuando no se pasa. Aquí solo se pasa el importe, así que la etiqueta vale «Total».
</details>

**16.** ¿Qué imprime?

```python
def linea(valor, etiqueta="Total"):
    return f"{etiqueta}: {valor:.2f}"


print(linea(etiqueta="Base", valor=30.0))
```

- **a)** `30.00: Base`
- **b)** `TypeError`
- **c)** `Base: 30.00`
- **d)** `Total: 30.00`

<details><summary>Respuesta</summary>

**c)** `Base: 30.00`

Al llamar por nombre el orden da igual, y se lee mucho mejor cuando hay varios parámetros.
</details>


## Ámbito de las variables

**17.** ¿Qué imprime?

```python
IVA = 21


def subir():
    IVA = 50
    return IVA


print(IVA, subir(), IVA)
```

- **a)** `50 50 50`
- **b)** `NameError`
- **c)** `21 50 21`
- **d)** `21 21 21`

<details><summary>Respuesta</summary>

**c)** `21 50 21`

</details>

**18.** ¿Qué imprime?

```python
IVA = 21


def subir():
    global IVA
    IVA = 50
    return IVA


print(IVA, subir(), IVA)
```

- **a)** `50 50 50`
- **b)** `21 50 50`
- **c)** `NameError`
- **d)** `21 50 21`

<details><summary>Respuesta</summary>

**b)** `21 50 50`

</details>

**19.** ¿Qué error lanza este programa?

```python
total = 0


def acumular(n):
    total = total + n
    return total


print(acumular(5))
```

- **a)** `NameError`
- **b)** `TypeError`
- **c)** `ValueError`
- **d)** `UnboundLocalError`

<details><summary>Respuesta</summary>

**d)** `UnboundLocalError`

</details>

**20.** ¿Qué imprime?

```python
total = 0


def acumular(n):
    return total + n


print(acumular(5))
```

- **a)** `UnboundLocalError`
- **b)** `None`
- **c)** `5`
- **d)** `0`

<details><summary>Respuesta</summary>

**c)** `5`

</details>

**21.** ¿Qué imprime?

```python
contador = 0


def contar(lista):
    contador = len(lista)
    return contador


print(contar([1, 2, 3]), contador)
```

- **a)** `3 3`
- **b)** `0 3`
- **c)** `NameError`
- **d)** `3 0`

<details><summary>Respuesta</summary>

**d)** `3 0`

</details>

**22.** ¿Qué error lanza?

```python
def calcular(base):
    return base * (1 + IVA / 100)


print(calcular(100.0))
IVA = 21
```

- **a)** `AttributeError`
- **b)** `TypeError`
- **c)** `NameError`
- **d)** `UnboundLocalError`

<details><summary>Respuesta</summary>

**c)** `NameError`

</details>

**23.** ¿Qué imprime?

```python
unidades = 3


def cuantas():
    return unidades


print(cuantas())
```

- **a)** `None`
- **b)** `3`
- **c)** `0`
- **d)** `NameError`

<details><summary>Respuesta</summary>

**b)** `3`

Dentro de la función se lee la variable de fuera sin problema. Lo que no se puede es asignarle un valor sin declararla `global`.
</details>

**24.** ¿Qué imprime?

```python
total = 0


def calcular():
    total = 59.85
    return total


print(calcular())
print(total)
```

- **a)** `59.85 ⏎ 0`
- **b)** `NameError`
- **c)** `59.85 ⏎ 59.85`
- **d)** `0 ⏎ 0`

<details><summary>Respuesta</summary>

**a)** `59.85 ⏎ 0`

La asignación dentro de la función crea una variable **local**. La de fuera no se entera de nada.
</details>


## Listas

**25.** ¿Qué imprime?

```python
def media(notas):
    """Media; 0.0 si no hay notas."""
    if len(notas) == 0:
        return 0.0
    return sum(notas) / len(notas)


print(f"{media([5.0, 7.5, 9.0]):.2f}")
```

- **a)** `7.17`
- **b)** `21.5`
- **c)** `7.16`
- **d)** `7.166666666666667`

<details><summary>Respuesta</summary>

**a)** `7.17`

</details>

**26.** ¿Qué imprime?

```python
def media(notas):
    if len(notas) == 0:
        return 0.0
    return sum(notas) / len(notas)


print(media([]))
```

- **a)** `ZeroDivisionError`
- **b)** `0.0`
- **c)** `None`
- **d)** `0`

<details><summary>Respuesta</summary>

**b)** `0.0`

</details>

**27.** ¿Qué imprime?

```python
def aprobadas(notas):
    total = 0
    for n in notas:
        if n >= 5:
            total += 1
    return total


print(aprobadas([3.0, 6.5, 9.0, 4.0]), aprobadas([5.0]))
```

- **a)** `3 1`
- **b)** `2 1`
- **c)** `2 2`
- **d)** `1 1`

<details><summary>Respuesta</summary>

**b)** `2 1`

</details>

**28.** ¿Qué imprime?

```python
notas = [5.0, 7.0, 9.0, 4.0]

ultima = notas[-1]
primera = notas[0]

print(ultima)
```

- **a)** `4.0`
- **b)** `10.0`
- **c)** `IndexError`
- **d)** `0.0`

<details><summary>Respuesta</summary>

**a)** `4.0`

</details>

**29.** ¿Qué imprime?

```python
def resumen(notas):
    """Mínimo, máximo y media."""
    if len(notas) == 0:
        return 0.0, 0.0, 0.0
    return min(notas), max(notas), sum(notas) / len(notas)


print(resumen([5.0, 7.0, 9.0, 4.0]))
```

- **a)** `[4.0, 9.0, 6.25]`
- **b)** `(9.0, 4.0, 6.25)`
- **c)** `(4.0, 9.0, 6.0)`
- **d)** `(4.0, 9.0, 6.25)`

<details><summary>Respuesta</summary>

**d)** `(4.0, 9.0, 6.25)`

</details>

**30.** ¿Qué imprime?

```python
def suma(numeros):
    total = 0
    for n in numeros:
        total = n
    return total


print(suma([1, 2, 3]))
```

- **a)** `6`
- **b)** `3`
- **c)** `0`
- **d)** `1`

<details><summary>Respuesta</summary>

**b)** `3`

</details>

**31.** Esta función está en tu proyecto. ¿Cuál de estos cuatro resultados **no** es el que devuelve?

```python
def media(notas: list[float]) -> float:
    """Media aritmética; 0.0 si la lista está vacía."""
    if len(notas) == 0:
        return 0.0
    return sum(notas) / len(notas)
```

- **a)** `media([5.0, 7.0])` devuelve `6.0`
- **b)** `media([10.0])` devuelve `10.0`
- **c)** `media([5.0, 7.5, 9.0])` devuelve `7.17`
- **d)** `media([])` devuelve `0.0`

<details><summary>Respuesta</summary>

**c)** `media([5.0, 7.5, 9.0]) → 7.17`

</details>

**32.** ¿Cuál de estos cuatro resultados **no** es el que devuelve la función?

```python
def contar_pares(numeros: list[int]) -> int:
    """Cuántos números pares hay en la lista."""
    total = 0
    for n in numeros:
        if n % 2 == 0:
            total += 1
    return total
```

- **a)** `contar_pares([1, 2, 3, 4])` devuelve `2`
- **b)** `contar_pares([])` devuelve `0`
- **c)** `contar_pares([0, -2, 7])` devuelve `2`
- **d)** `contar_pares([1, 3, 5])` devuelve `1`

<details><summary>Respuesta</summary>

**d)** `contar_pares([1, 3, 5]) → 1`

</details>


## Librería estándar

**33.** ¿Qué imprime?

```python
import math

valor = 47 / 10

print(math.ceil(valor), round(valor), math.floor(valor))
```

- **a)** `4 4 4`
- **b)** `5 4 4`
- **c)** `5 4 5`
- **d)** `5 5 4`

<details><summary>Respuesta</summary>

**d)** `5 5 4`

</details>

**34.** ¿Qué imprime?

```python
import math

valor = 44 / 10

print(math.ceil(valor), round(valor), math.floor(valor))
```

- **a)** `5 4 4`
- **b)** `4 5 4`
- **c)** `5 5 4`
- **d)** `4 4 4`

<details><summary>Respuesta</summary>

**a)** `5 4 4`

</details>

**35.** ¿Qué imprime?

```python
import math


def hipotenusa(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def area_circulo(r):
    return math.pi * r ** 2


print(hipotenusa(3.0, 4.0), f"{area_circulo(3.0):.2f}")
```

- **a)** `5 28.27`
- **b)** `5.0 28.27`
- **c)** `5.0 78.54`
- **d)** `25.0 28.27`

<details><summary>Respuesta</summary>

**b)** `5.0 28.27`

</details>

**36.** ¿Qué error lanza este programa?

```python
from math import sqrt


def hipotenusa(a, b):
    return sqrt(a ** 2 + b ** 2)


print(hipotenusa(3.0, 4.0))
print(pi)
```

- **a)** `AttributeError`
- **b)** `NameError`
- **c)** `ImportError`
- **d)** `TypeError`

<details><summary>Respuesta</summary>

**b)** `NameError`

</details>

**37.** ¿Qué imprime?

```python
import math


def cajas(unidades, por_caja):
    """Cajas necesarias para no dejar unidades fuera."""
    return math.ceil(unidades / por_caja)


print(cajas(47, 10))
```

- **a)** `4`
- **b)** `4.7`
- **c)** `5.0`
- **d)** `5`

<details><summary>Respuesta</summary>

**d)** `5`

</details>

**38.** ¿Qué imprime?

```python
import math

print(f"{math.pi:.4f}", f"{math.pi:.2f}")
```

- **a)** `3.1416 3.14`
- **b)** `3.14 3.1416`
- **c)** `3.14 3.14`
- **d)** `3.1416 3.1416`

<details><summary>Respuesta</summary>

**a)** `3.1416 3.14`

</details>

**39.** ¿Cuál de estos cuatro resultados **no** es el que devuelve la función?

```python
import math


def cajas(unidades: int, por_caja: int) -> int:
    """Cajas necesarias para no dejar unidades fuera."""
    return math.ceil(unidades / por_caja)
```

- **a)** `cajas(0, 5)` devuelve `1`
- **b)** `cajas(47, 10)` devuelve `5`
- **c)** `cajas(1, 5)` devuelve `1`
- **d)** `cajas(40, 10)` devuelve `4`

<details><summary>Respuesta</summary>

**a)** `cajas(0, 5) → 1`

</details>

**40.** ¿Cuál cuenta bien los aprobados, contando el 5 como aprobado?

**a)**

```python
def aprobados(notas: list[float]) -> int:
    """Cuántas notas llegan a 5."""
    total = 0
    for n in notas:
        total += 1
    return total
```

**b)**

```python
def aprobados(notas: list[float]) -> int:
    """Cuántas notas llegan a 5."""
    total = 0
    for n in notas:
        if n > 5:
            total += 1
    return total
```

**c)**

```python
def aprobados(notas: list[float]) -> int:
    """Cuántas notas llegan a 5."""
    for n in notas:
        if n >= 5:
            return 1
    return 0
```

**d)**

```python
def aprobados(notas: list[float]) -> int:
    """Cuántas notas llegan a 5."""
    total = 0
    for n in notas:
        if n >= 5:
            total += 1
    return total
```


<details><summary>Respuesta</summary>

**d)** `def aprobados(notas: list[float]) -> int: ⏎     """Cuántas notas llegan a 5.""" ⏎     total = 0 ⏎     for n in notas: ⏎         if n >= 5: ⏎             total += 1 ⏎     return total`

</details>


## Módulos y `__main__`

**41.** La función recibe una lista y **no debe modificarla**. ¿Cuál lo cumple?

**a)**

```python
def con_extra(notas: list[float], extra: float) -> list[float]:
    """Devuelve una lista nueva con el extra añadido."""
    nueva = notas
    nueva.append(extra)
    return nueva
```

**b)**

```python
def con_extra(notas: list[float], extra: float) -> list[float]:
    """Devuelve una lista nueva con el extra añadido."""
    return notas + [extra]
```

**c)**

```python
def con_extra(notas: list[float], extra: float) -> list[float]:
    """Devuelve una lista nueva con el extra añadido."""
    notas += [extra]
    return notas
```

**d)**

```python
def con_extra(notas: list[float], extra: float) -> list[float]:
    """Devuelve una lista nueva con el extra añadido."""
    notas.append(extra)
    return notas
```


<details><summary>Respuesta</summary>

**b)** `def con_extra(notas: list[float], extra: float) -> list[float]: ⏎     """Devuelve una lista nueva con el extra añadido.""" ⏎     return notas + [extra]`

</details>

**42.** ¿Qué imprime al ejecutar este fichero directamente?

```python
if __name__ == "__main__":
    print("soy el principal")
```

- **a)** `importado`
- **b)** `no imprime nada`
- **c)** `soy el principal`
- **d)** `NameError`

<details><summary>Respuesta</summary>

**c)** `soy el principal`

Al lanzar el fichero, `__name__` vale `"__main__"`. Al importarlo valdría el nombre del módulo, y el bloque no se ejecutaría.
</details>

**43.** ¿Qué imprime?

```python
print(__name__)
```

- **a)** `modulos`
- **b)** `main`
- **c)** `__main__`
- **d)** `None`

<details><summary>Respuesta</summary>

**c)** `__main__`

Es la variable que permite distinguir «me están ejecutando» de «me están importando».
</details>

**44.** ¿Qué imprime?

```python
"""Utilidades de cálculo."""


def doble(n):
    """Devuelve el doble."""
    return n * 2


print(doble.__doc__)
```

- **a)** `Devuelve el doble.`
- **b)** `None`
- **c)** `42`
- **d)** `Utilidades de cálculo.`

<details><summary>Respuesta</summary>

**a)** `Devuelve el doble.`

`__doc__` guarda el docstring. El del módulo (la primera cadena del fichero) y el de la función son distintos: aquí se pide el de la función.
</details>

**45.** ¿Qué imprime al ejecutar este fichero directamente?

```python
def doble(n):
    return n * 2


if __name__ == "__main__":
    print(doble(21))
```

- **a)** `no imprime nada`
- **b)** `42`
- **c)** `None`
- **d)** `NameError`

<details><summary>Respuesta</summary>

**b)** `42`

Se lanza directamente, así que `__name__` vale `"__main__"` y el bloque de prueba sí se ejecuta.
</details>

**46.** ¿Qué imprime?

```python
print(__name__ == "__main__")
```

- **a)** `NameError`
- **b)** `False`
- **c)** `True`
- **d)** `__main__`

<details><summary>Respuesta</summary>

**c)** `True`

Al ejecutar el fichero, la comparación es verdadera. Al importarlo sería falsa.
</details>

**47.** ¿Por qué este módulo da problemas al importarlo? ¿Qué imprime al ejecutarlo?

```python
def doble(n):
    return n * 2


print(doble(21))
```

- **a)** `ImportError`
- **b)** `42`
- **c)** `None`
- **d)** `no imprime nada`

<details><summary>Respuesta</summary>

**b)** `42`

Sin el `if __name__ == "__main__":`, el `print` de prueba se ejecuta también al importar el módulo desde otro programa, que es justo lo que no se quiere.
</details>

**48.** ¿Qué error lanza este programa?

```python
import math


def area(radio):
    return pi * radio ** 2


print(area(1.0))
```

- **a)** `NameError`
- **b)** `ModuleNotFoundError`
- **c)** `ImportError`
- **d)** `AttributeError`

<details><summary>Respuesta</summary>

**a)** `NameError`

Se ha importado `math`, pero para usar algo de dentro hay que escribir `math.pi`. Sin el prefijo, ese nombre no existe.
</details>
