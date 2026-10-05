# Unidad 4 · Fundamentos de la programación orientada a objetos

> **Módulo:** CMO-313 · Fundamentos de programación
> **Resultado de aprendizaje:** RA4 · **Duración:** 8 h · **Peso:** 15 %
> **Lenguaje:** Python 3 (tipado)

Hasta ahora has separado el programa en **funciones** (acciones) y has guardado los datos en variables sueltas. La programación orientada a objetos (POO) da un paso más: **junta los datos y las acciones que operan sobre ellos** en una sola pieza, el objeto.

Es el modelo con el que están escritos casi todos los programas grandes, y el que usarás en segundo curso constantemente.

---

## Mapa de la unidad

<figure markdown>
  ![Mapa de la unidad 4](../assets/diagramas/ud4-mapa.svg#only-light)
  ![Mapa de la unidad 4](../assets/diagramas/ud4-mapa-dark.svg#only-dark)
  <figcaption>Una clase define cómo son los objetos; la herencia permite especializarla.</figcaption>
</figure>

### Qué vas a saber hacer al terminar

- [ ] Distinguir **clase** de **objeto**.
- [ ] Definir una clase con `__init__`, atributos y métodos.
- [ ] Entender qué es `self` y por qué está en todos los métodos.
- [ ] Controlar el acceso a los atributos (**encapsulación**) con `property`.
- [ ] Crear clases derivadas mediante **herencia** y usar `super()`.
- [ ] Sobrescribir métodos y definir `__str__`.

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

## 1. Clase y objeto

Una **clase** es un molde: describe qué datos tiene algo y qué sabe hacer. Un **objeto** es cada ejemplar concreto creado a partir de ese molde.

> **Analogía.** La clase es el **plano de un piso**; los objetos son los pisos construidos con ese plano. Todos comparten la estructura, pero cada uno tiene sus propios muebles.

```python
class Coche:
    pass

mi_coche = Coche()          # un objeto
otro_coche = Coche()        # otro objeto distinto
```

| Concepto | Qué es | Ejemplo |
|---|---|---|
| **Clase** | El molde | `Coche` |
| **Objeto / instancia** | Un ejemplar | `mi_coche` |
| **Atributo** | Un dato del objeto | `marca`, `velocidad` |
| **Método** | Una acción del objeto | `describir()`, `acelerar()` |

---

> **Reto rápido 1.** Piensa en la clase `Libro`: ¿qué tres atributos tendría? ¿Y dos objetos concretos suyos? *(Solución: título, autor y año; «El Quijote» y «Rayuela».)*

## 2. Atributos y `__init__`

`__init__` es el **constructor**: se ejecuta automáticamente al crear el objeto y sirve para darle sus datos iniciales.

```python
class Coche:
    def __init__(self, marca: str, velocidad: int) -> None:
        self.marca = marca              # atributo del objeto
        self.velocidad = velocidad

mi_coche = Coche("Seat", 120)
print(mi_coche.marca)        # Seat
print(mi_coche.velocidad)    # 120
```

### 2.1 Qué es `self`

`self` es **el propio objeto**. Python lo pasa automáticamente como primer parámetro de todos los métodos, para que dentro sepas sobre qué objeto trabajas.

```python
mi_coche = Coche("Seat", 120)     # self será mi_coche
otro = Coche("Ford", 90)          # aquí self será otro
```

Por eso `self.marca` significa «la marca **de este** objeto».

!!! warning "Los tres errores de `self`"
    ```python
    class Coche:
        def __init__(marca):          # ✗ falta self
            self.marca = marca

        def describir(self) -> str:
            return marca              # ✗ falta self. delante

    mi_coche.describir(mi_coche)      # ✗ self no se pasa a mano
    ```
    Lo correcto: `def __init__(self, marca)`, `return self.marca`, y llamar `mi_coche.describir()`.

> **Reto rápido 1.** Crea una clase `Alumno` con atributos `nombre` y `nota`, y crea dos objetos.

## 3. Métodos

Un **método** es una función definida dentro de la clase. Siempre lleva `self` como primer parámetro.

```python
class Coche:
    def __init__(self, marca: str, velocidad: int) -> None:
        self.marca = marca
        self.velocidad = velocidad

    def describir(self) -> str:
        """Devuelve una descripción del coche."""
        return f"Coche {self.marca} a {self.velocidad} km/h"

    def acelerar(self, incremento: int) -> None:
        """Aumenta la velocidad."""
        self.velocidad = self.velocidad + incremento


mi_coche = Coche("Seat", 120)
print(mi_coche.describir())      # Coche Seat a 120 km/h
mi_coche.acelerar(20)
print(mi_coche.velocidad)        # 140
```

!!! tip "Métodos que consultan y métodos que modifican"
    `describir()` **devuelve** información (`-> str`).
    `acelerar()` **cambia** el objeto y no devuelve nada (`-> None`).
    Conviene no mezclar ambas cosas en un mismo método.

### 3.1 `__str__`: cómo se ve el objeto

Sin `__str__`, imprimir un objeto da algo ilegible:

```python
print(mi_coche)     # <__main__.Coche object at 0x7f8b1c0>
```

Definiéndolo, decides tú qué se muestra:

```python
class Coche:
    def __init__(self, marca: str) -> None:
        self.marca = marca

    def __str__(self) -> str:
        return f"Coche {self.marca}"

print(Coche("Seat"))     # Coche Seat
```

> **Reto rápido 2.** Añade a `Alumno` un método `aprueba(self) -> bool` que indique si su nota es ≥ 5.

## 4. Encapsulación: proteger los datos

Por defecto cualquiera puede tocar los atributos, incluso poniendo valores absurdos:

```python
mi_coche.velocidad = -500      # nadie lo impide: el objeto queda en un estado imposible
```

**Encapsular** es controlar cómo se accede a los datos del objeto.

### 4.1 La convención del guion bajo

En Python no existen atributos verdaderamente privados; se usa una **convención**:

| Nombre | Significado |
|---|---|
| `velocidad` | público: cualquiera puede usarlo |
| `_velocidad` | «uso interno, no lo toques desde fuera» |
| `__velocidad` | Python le cambia el nombre para dificultar el acceso |

### 4.2 `property`: la forma correcta

Permite validar al asignar, manteniendo una sintaxis cómoda:

```python
class Coche:
    def __init__(self, marca: str, velocidad: int) -> None:
        self.marca = marca
        self._velocidad = 0
        self.velocidad = velocidad      # pasa por el setter y valida

    @property
    def velocidad(self) -> int:
        """Velocidad actual en km/h."""
        return self._velocidad

    @velocidad.setter
    def velocidad(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("La velocidad no puede ser negativa")
        self._velocidad = valor


coche = Coche("Seat", 120)
print(coche.velocidad)        # 120   (llama al getter)
coche.velocidad = 140         # ✓     (llama al setter y valida)
coche.velocidad = -10         # ✗ ValueError
```

Lo bueno: **quien usa la clase no nota nada**, sigue escribiendo `coche.velocidad`. Pero ahora es imposible dejar el objeto en un estado inválido.

> **Reto rápido 3.** Protege la `nota` de `Alumno` para que solo admita valores entre 0 y 10.

## 5. Herencia

La **herencia** permite crear una clase nueva a partir de otra, aprovechando lo que ya tiene y añadiendo o cambiando lo que haga falta.

```python
class Vehiculo:
    def __init__(self, marca: str, velocidad: int) -> None:
        self.marca = marca
        self.velocidad = velocidad

    def describir(self) -> str:
        return f"Vehículo {self.marca} a {self.velocidad} km/h"


class Coche(Vehiculo):          # Coche hereda de Vehiculo
    def describir(self) -> str:  # sobrescribe el método
        return f"Coche {self.marca} a {self.velocidad} km/h"


class Moto(Vehiculo):
    def describir(self) -> str:
        return f"Moto {self.marca} a {self.velocidad} km/h"


print(Coche("Seat", 120).describir())    # Coche Seat a 120 km/h
print(Moto("Honda", 90).describir())     # Moto Honda a 90 km/h
```

`Coche` y `Moto` **no repiten** el `__init__`: lo heredan de `Vehiculo`.

Vocabulario: `Vehiculo` es la clase **base** (o padre); `Coche` y `Moto` son **derivadas** (o hijas). **Sobrescribir** es redefinir en la hija un método que ya existía en la madre.

### 5.1 `super()`: reutilizar lo de la clase base

Cuando la hija necesita añadir algo pero también quiere lo de la madre:

```python
class Camion(Vehiculo):
    def __init__(self, marca: str, velocidad: int, carga: float) -> None:
        super().__init__(marca, velocidad)     # ejecuta el __init__ de Vehiculo
        self.carga = carga                      # y añade lo suyo

    def describir(self) -> str:
        base = super().describir()              # aprovecha el texto de la madre
        return f"{base} con {self.carga} t de carga"
```

!!! tip "Cuándo usar herencia"
    Solo cuando puedas decir «**X es un** Y»: un coche **es un** vehículo. Si lo que quieres decir es «X **tiene un** Y» (un coche tiene un motor), eso no es herencia: es un atributo.

> **Reto rápido 4.** Crea `Bicicleta(Vehiculo)` que sobrescriba `describir()`.

## 6. Errores frecuentes

| Síntoma | Causa | Solución |
|---|---|---|
| `TypeError: __init__() takes 2 positional arguments but 3 were given` | falta `self` en la definición | `def __init__(self, ...)` |
| `NameError` dentro de un método | usaste `marca` en vez de `self.marca` | pon `self.` delante |
| `AttributeError: 'Coche' object has no attribute 'x'` | no se creó en `__init__` o hay una errata | créalo en el constructor |
| Al imprimir sale `<object at 0x…>` | falta `__str__` | defínelo |
| La clase hija pierde los atributos | olvidaste `super().__init__(...)` | llámalo al principio |
| El `property` entra en bucle infinito | dentro del setter asignas a `self.velocidad` | asigna a `self._velocidad` |

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


### Tema 1 · Clase y objeto

**1.1.** Explica con tus palabras la diferencia entre **clase** y **objeto**, con un ejemplo que no sea de programación.
<details><summary>Solución</summary>

```text
Clase  = el molde, el plano, la receta. Se escribe UNA vez.
Objeto = cada cosa concreta hecha con ese molde. Puede haber miles.

Ejemplo: la clase es el plano de un piso; los objetos son el 1ºA, el 1ºB,
el 2ºA... Todos tienen cocina y bano (los mismos atributos), pero cada uno
con sus propios valores: distinto propietario, distinto numero.

En codigo:
    class Piso:      <- el plano, se escribe una vez
    piso1 = Piso()   <- un piso concreto
    piso2 = Piso()   <- otro piso, independiente del anterior
```
</details>

**1.2.** Identifica la clase y los objetos en esta frase: «En el taller hay tres coches: un Ibiza rojo, un Clio azul y un Golf blanco».
<details><summary>Solución</summary>

```text
Clase:   Coche
Atributos: modelo, color
Objetos: tres instancias de Coche
         Coche("Ibiza", "rojo")
         Coche("Clio", "azul")
         Coche("Golf", "blanco")

Truco: los nombres COMUNES suelen ser clases (coche, alumno, factura);
los nombres PROPIOS o los ejemplares concretos son objetos.
```
</details>

**1.3.** Escribe la clase más pequeña posible, `Punto`, y crea dos objetos distintos.
<details><summary>Solución</summary>

```python
class Punto:
    """Un punto cualquiera."""


a = Punto()
b = Punto()

print(type(a).__name__)   # -> Punto
print(a is b)             # -> False   son dos objetos distintos
```
</details>


**1.4.** Escribe la clase más pequeña posible, `Perro`, y crea tres objetos. Comprueba que son tres cosas distintas aunque salgan del mismo molde.
<details><summary>Solución</summary>

```python
class Perro:
    """Un perro cualquiera."""


a = Perro()
b = Perro()
c = Perro()

print(a is b, b is c)          # -> False False
print(type(a) is type(b))      # -> True

# Mismo molde (misma clase), tres objetos independientes.
```
</details>


### Tema 2 · Atributos y `__init__`

**2.1.** Escribe la clase `Alumno` con `nombre` y `nota`, y crea dos alumnos.
<details><summary>Solución</summary>

```python
class Alumno:
    """Alumno con su nota."""

    def __init__(self, nombre: str, nota: float) -> None:
        self.nombre = nombre
        self.nota = nota


ada = Alumno("Ada", 9.5)
alan = Alumno("Alan", 7.0)

print(ada.nombre, ada.nota)     # -> Ada 9.5
print(alan.nombre, alan.nota)   # -> Alan 7.0
```
</details>

**2.2.** ¿Qué es `self`? Comprueba que cada objeto tiene sus **propios** atributos.
<details><summary>Solución</summary>

```python
class Contador:
    """Contador independiente."""

    def __init__(self) -> None:
        self.valor = 0   # self = ESTE objeto concreto, no la clase


a = Contador()
b = Contador()

a.valor = 10

print(a.valor)   # -> 10
print(b.valor)   # -> 0     b no se entera de nada: son objetos distintos
```
</details>

**2.3.** Añade a `Alumno` un atributo `grupo` con valor por defecto `"1DAW"`.
<details><summary>Solución</summary>

```python
class Alumno:
    """Alumno con su nota y su grupo."""

    def __init__(self, nombre: str, nota: float, grupo: str = "1DAW") -> None:
        self.nombre = nombre
        self.nota = nota
        self.grupo = grupo


print(Alumno("Ada", 9.5).grupo)          # -> 1DAW
print(Alumno("Alan", 7.0, "1DAM").grupo) # -> 1DAM
```
</details>

**2.4.** Este código falla. ¿Por qué?

```python
class Coche:
    def __init__(modelo):
        self.modelo = modelo
```
<details><summary>Solución</summary>

```python
class Coche:
    """Coche con modelo."""

    def __init__(self, modelo: str) -> None:   # faltaba self como PRIMER parámetro
        self.modelo = modelo


print(Coche("Ibiza").modelo)   # -> Ibiza

# Sin self, Python pasa el objeto en el primer hueco y 'modelo' acaba siendo
# el propio coche. El error tipico: "takes 1 positional argument but 2 were given".
```
</details>


### Tema 3 · Métodos

**3.1.** Añade a `Alumno` un método `aprueba()` que diga si llega a 5.
<details><summary>Solución</summary>

```python
class Alumno:
    """Alumno con su nota."""

    def __init__(self, nombre: str, nota: float) -> None:
        self.nombre = nombre
        self.nota = nota

    def aprueba(self) -> bool:
        """Indica si la nota llega a 5."""
        return self.nota >= 5


print(Alumno("Ada", 9.5).aprueba())   # -> True
print(Alumno("Alan", 3.0).aprueba())  # -> False
```
</details>

**3.2.** Añade `__str__` a `Alumno` para que `print(alumno)` muestre `Ada (9.50)`.
<details><summary>Solución</summary>

```python
class Alumno:
    """Alumno con su nota."""

    def __init__(self, nombre: str, nota: float) -> None:
        self.nombre = nombre
        self.nota = nota

    def __str__(self) -> str:
        return f"{self.nombre} ({self.nota:.2f})"


print(Alumno("Ada", 9.5))   # -> Ada (9.50)

# Sin __str__ saldria algo como <__main__.Alumno object at 0x7f...>
```
</details>

**3.3.** Escribe `Rectangulo` con métodos `area()` y `perimetro()`.
<details><summary>Solución</summary>

```python
class Rectangulo:
    """Rectángulo definido por su base y su altura."""

    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def area(self) -> float:
        """Área del rectángulo."""
        return self.base * self.altura

    def perimetro(self) -> float:
        """Perímetro del rectángulo."""
        return 2 * (self.base + self.altura)


r = Rectangulo(3, 4)
print(r.area())        # -> 12
print(r.perimetro())   # -> 14
```
</details>


**3.4.** Añade a `Rectangulo` un método `es_cuadrado()` que diga si la base y la altura coinciden.
<details><summary>Solución</summary>

```python
class Rectangulo:
    """Rectángulo definido por su base y su altura."""

    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def area(self) -> float:
        """Área del rectángulo."""
        return self.base * self.altura

    def es_cuadrado(self) -> bool:
        """Indica si los cuatro lados miden lo mismo."""
        return self.base == self.altura


print(Rectangulo(3, 3).es_cuadrado())   # -> True
print(Rectangulo(3, 4).es_cuadrado())   # -> False
```
</details>


### Tema 4 · Encapsulación con `property`

**4.1.** Convierte `nota` en una **property** que no admita valores fuera de 0–10.
<details><summary>Solución</summary>

```python
class Alumno:
    """Alumno con la nota validada."""

    def __init__(self, nombre: str, nota: float) -> None:
        self.nombre = nombre
        self._nota = 0.0
        self.nota = nota          # pasa por el setter: se valida también al crear

    @property
    def nota(self) -> float:
        """Nota del alumno."""
        return self._nota

    @nota.setter
    def nota(self, valor: float) -> None:
        if not 0 <= valor <= 10:
            raise ValueError("la nota debe estar entre 0 y 10")
        self._nota = valor


a = Alumno("Ada", 9.5)
print(a.nota)   # -> 9.5

try:
    a.nota = 11
except ValueError as e:
    print("Error:", e)   # -> Error: la nota debe estar entre 0 y 10
```
</details>

**4.2.** ¿Por qué el `__init__` debe asignar `self.nota = nota` y no `self._nota = nota`?
<details><summary>Solución</summary>

```text
Porque self.nota = nota pasa por el SETTER, y el setter es quien valida.

Si escribes self._nota = nota te saltas la validacion justo en el momento
mas peligroso: la creacion del objeto. Entonces esto colaria:

    Alumno("Ada", 500)   # nota imposible, y el objeto nace ya corrupto

Regla: dentro de __init__, asigna siempre por la property.
```
</details>

**4.3.** Añade a `Producto` una property `precio` que rechace negativos, y comprueba los dos momentos: al crear y al asignar.
<details><summary>Solución</summary>

```python
class Producto:
    """Producto con precio validado."""

    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self._precio = 0.0
        self.precio = precio

    @property
    def precio(self) -> float:
        """Precio del producto."""
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("el precio no puede ser negativo")
        self._precio = valor


try:
    Producto("Roto", -5)
except ValueError:
    print("rechazado al crear")     # -> rechazado al crear

p = Producto("Gorra", 10.0)
try:
    p.precio = -1
except ValueError:
    print("rechazado al asignar")   # -> rechazado al asignar

p.precio = 0
print(p.precio)   # -> 0     cero no es negativo: se acepta
```
</details>


**4.4.** Haz que la *property* `nota` acepte también el 0 y el 10 (los extremos), y compruébalo con los tres casos límite: 0, 10 y 10.1.
<details><summary>Solución</summary>

```python
class Alumno:
    """Alumno con la nota validada entre 0 y 10, extremos incluidos."""

    def __init__(self, nombre: str, nota: float) -> None:
        self.nombre = nombre
        self._nota = 0.0
        self.nota = nota

    @property
    def nota(self) -> float:
        """Nota del alumno."""
        return self._nota

    @nota.setter
    def nota(self, valor: float) -> None:
        if not 0 <= valor <= 10:          # <= en los dos lados: los extremos entran
            raise ValueError("la nota debe estar entre 0 y 10")
        self._nota = valor


print(Alumno("A", 0).nota)    # -> 0
print(Alumno("B", 10).nota)   # -> 10

try:
    Alumno("C", 10.1)
except ValueError:
    print("10.1 rechazado")   # -> 10.1 rechazado
```
</details>


### Tema 5 · Herencia

**5.1.** Crea `Vehiculo` con `describir()` y una clase `Moto` que **herede** y sobrescriba solo ese método.
<details><summary>Solución</summary>

```python
class Vehiculo:
    """Vehículo genérico."""

    def __init__(self, matricula: str) -> None:
        self.matricula = matricula

    def describir(self) -> str:
        """Descripción."""
        return f"Vehículo {self.matricula}"


class Moto(Vehiculo):
    """Motocicleta."""

    def describir(self) -> str:
        return f"Moto {self.matricula}"


print(Vehiculo("1234ABC").describir())   # -> Vehículo 1234ABC
print(Moto("5678XYZ").describir())       # -> Moto 5678XYZ

# Moto NO repite __init__: lo hereda tal cual.
```
</details>

**5.2.** Comprueba que `Moto` hereda de verdad, y que hereda el constructor sin repetirlo.
<details><summary>Solución</summary>

```python
class Vehiculo:
    """Vehículo genérico."""

    def __init__(self, matricula: str) -> None:
        self.matricula = matricula


class Moto(Vehiculo):
    """Motocicleta."""


print(issubclass(Moto, Vehiculo))       # -> True
print(isinstance(Moto("1234ABC"), Vehiculo))   # -> True
print(Moto("1234ABC").matricula)        # -> 1234ABC   el __init__ es heredado
```
</details>

**5.3.** Desde `Camion.describir()`, reutiliza lo que ya hace la clase base con `super()`.
<details><summary>Solución</summary>

```python
class Vehiculo:
    """Vehículo genérico."""

    def __init__(self, matricula: str) -> None:
        self.matricula = matricula

    def describir(self) -> str:
        """Descripción."""
        return f"Vehículo {self.matricula}"


class Camion(Vehiculo):
    """Camión con carga máxima."""

    def __init__(self, matricula: str, toneladas: float) -> None:
        super().__init__(matricula)      # reutiliza el __init__ del padre
        self.toneladas = toneladas

    def describir(self) -> str:
        return f"{super().describir()} · {self.toneladas} t"


print(Camion("1234ABC", 12.5).describir())   # -> Vehículo 1234ABC · 12.5 t
```
</details>

**5.4.** Este código repite el `__init__` en la clase derecha sin necesidad. Quítalo:

```python
class Coche(Vehiculo):
    def __init__(self, matricula):
        self.matricula = matricula
```
<details><summary>Solución</summary>

```python
class Vehiculo:
    """Vehículo genérico."""

    def __init__(self, matricula: str) -> None:
        self.matricula = matricula


class Coche(Vehiculo):
    """Coche: no aporta nada nuevo al constructor, así que no lo repite."""

    def describir(self) -> str:
        """Descripción."""
        return f"Coche {self.matricula}"


print(Coche("1234ABC").describir())   # -> Coche 1234ABC

# Repetir el __init__ es duplicar codigo: si manana el padre valida la matricula,
# el hijo se queda sin esa validacion y nadie se entera.
```
</details>


### Actividades guiadas

#### Actividad 1 — Tu primera clase
`Persona` con `nombre` y `edad`, y un método `saludar()` que devuelva `"Hola, soy Ada"`.
<details><summary>Solución</summary>

```python
class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def saludar(self) -> str:
        return f"Hola, soy {self.nombre}"

print(Persona("Ada", 36).saludar())
```
</details>

#### Actividad 2 — Método que modifica
Añade `cumplir_anios()` que sume 1 a la edad.
<details><summary>Solución</summary>

```python
    def cumplir_anios(self) -> None:
        self.edad = self.edad + 1
```
</details>

#### Actividad 3 — Encapsular
Protege `edad` para que no admita valores negativos.
<details><summary>Solución</summary>

```python
class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self._edad = 0
        self.edad = edad

    @property
    def edad(self) -> int:
        return self._edad

    @edad.setter
    def edad(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = valor
```
</details>

#### Actividad 4 — Herencia
`Empleado(Persona)` con un atributo `sueldo`, usando `super()`.
<details><summary>Solución</summary>

```python
class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, sueldo: float) -> None:
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def saludar(self) -> str:
        return f"Hola, soy {self.nombre} y cobro {self.sueldo} €"
```
</details>

### Ejercicios propuestos

**E1 ○ · Rectángulo.** Clase con `base` y `altura` y métodos `area()` y `perimetro()`.
<details><summary>Solución</summary>

```python
class Rectangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)
```
</details>

**E2 ○ · Cuenta bancaria.** `saldo`, `ingresar(cantidad)` y `saldo_actual()`.
<details><summary>Solución</summary>

```python
class Cuenta:
    def __init__(self, saldo: float = 0.0) -> None:
        self.saldo = saldo

    def ingresar(self, cantidad: float) -> None:
        self.saldo += cantidad

    def saldo_actual(self) -> float:
        return self.saldo
```
</details>

**E3 ◐ · Retirar con control.** Añade `retirar(cantidad)` que lance `ValueError` si no hay saldo.
<details><summary>Solución</summary>

```python
    def retirar(self, cantidad: float) -> None:
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad
```
</details>

**E4 ◐ · `__str__`.** Haz que imprimir un `Rectangulo` muestre `"Rectangulo 4x3"`.
<details><summary>Solución</summary>

```python
    def __str__(self) -> str:
        return f"Rectangulo {self.base}x{self.altura}"
```
</details>

**E5 ● · Jerarquía de figuras.** `Figura` con `area()` que devuelva `0.0`, y `Circulo` y `Cuadrado` que la sobrescriban.
<details><summary>Solución</summary>

```python
import math

class Figura:
    def area(self) -> float:
        return 0.0

class Circulo(Figura):
    def __init__(self, radio: float) -> None:
        self.radio = radio
    def area(self) -> float:
        return math.pi * self.radio ** 2

class Cuadrado(Figura):
    def __init__(self, lado: float) -> None:
        self.lado = lado
    def area(self) -> float:
        return self.lado ** 2
```
</details>

**E6 ○ · Clase Libro.** Escribe la clase `Libro` con `titulo`, `autor` y `anio`, y un `__str__` que devuelva `El Quijote (Cervantes, 1605)`.
<details><summary>Pista</summary>El <code>__str__</code> es una f-string con los tres atributos.</details>
<details><summary>Solución</summary>

```python
class Libro:
    """Un libro del catálogo."""

    def __init__(self, titulo: str, autor: str, anio: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__(self) -> str:
        return f"{self.titulo} ({self.autor}, {self.anio})"
```
</details>

**E7 ◐ · Cuenta bancaria.** `CuentaBancaria` con un atributo `saldo` **validado con `property`** que no admite negativos (lanza `ValueError`), y un método `ingresar(cantidad)` que lo aumenta.
<details><summary>Pista</summary>El <code>__init__</code> tiene que asignar con <code>self.saldo = ...</code> para que pase por el setter y se valide también al crear la cuenta.</details>
<details><summary>Solución</summary>

```python
class CuentaBancaria:
    """Cuenta con saldo que nunca puede ser negativo."""

    def __init__(self, titular: str, saldo: float) -> None:
        self.titular = titular
        self._saldo = 0.0
        self.saldo = saldo

    @property
    def saldo(self) -> float:
        """Saldo actual."""
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("el saldo no puede ser negativo")
        self._saldo = valor

    def ingresar(self, cantidad: float) -> None:
        """Aumenta el saldo."""
        self.saldo = self._saldo + cantidad
```
</details>

**E8 ● · Figuras con herencia.** Clase base `Figura` con un método `area()` que devuelve `0.0`, y dos derivadas, `Cuadrado` y `Circulo`, que lo sobrescriben. Las derivadas **no repiten** el `__init__`.
<details><summary>Pista</summary>Dale a <code>Figura</code> un <code>__init__</code> con el único dato que comparten (la medida) y que las hijas lo hereden tal cual.</details>
<details><summary>Solución</summary>

```python
import math


class Figura:
    """Figura genérica definida por una medida."""

    def __init__(self, medida: float) -> None:
        self.medida = medida

    def area(self) -> float:
        """Área de la figura."""
        return 0.0


class Cuadrado(Figura):
    """Cuadrado de lado `medida`."""

    def area(self) -> float:
        return self.medida ** 2


class Circulo(Figura):
    """Círculo de radio `medida`."""

    def area(self) -> float:
        return math.pi * self.medida ** 2
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

Toda la práctica de esta unidad se hace sobre un **proyecto base**: una jerarquía de clases con encapsulación y herencia. Está montado
con la estructura real de un proyecto Python y trae una **batería de tests** que puedes
ejecutar en cualquier momento para ver si va todo bien.

**[Proyecto Flota de vehículos →](../proyectos/ud4/README.md)**

```
proyecto-ud4/
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

## 10. Simulacro de examen

Cuando tengas el proyecto terminado, mídete: el **simulacro** es un examen de mentira con
**el mismo formato, tamaño y rúbrica** que el de verdad — y con los tests publicados.

**[Simulacro RA4 · Catálogo de dispositivos →](../simulacros/ra4/README.md)** · 14 tests · 45–50 min

Hazlo **contrarreloj y sin ayuda**, como si fuera el examen. Al terminar, aplica la rúbrica
y tendrás una estimación bastante fiel de tu nota.

!!! warning "El examen de verdad va sin tests"
    Allí solo tendrás los **docstrings** y unos ejemplos. Por eso, en el simulacro, intenta
    resolver cada función leyendo solo su docstring y mira el test únicamente cuando falle.

---

---

## 11. Retos opcionales

- **R1.** Añade `Camion(Vehiculo)` con carga, usando `super()` en `__init__` y en `describir()`.
- **R2.** Crea una lista de vehículos distintos y recórrela llamando a `describir()` en cada uno. Fíjate en que cada objeto responde a su manera: eso es **polimorfismo**.
- **R3.** Investiga `@dataclass` y reescribe `Rectangulo` con él.

- **R4.** Modela una `Biblioteca` que guarde una lista de `Libro` y sepa buscar por autor.
- **R5.** Añade a la jerarquía de figuras un método `describir()` en la base que use `area()`, y comprueba que cada derivada lo hereda dando su resultado correcto.
- **R6.** Escribe una clase `Temperatura` con una *property* que permita leer el valor en Celsius y en Fahrenheit, calculando la segunda a partir de la primera.
---

---

## 12. Autoevaluación rápida

<details><summary>1. Diferencia entre clase y objeto.</summary>La clase es el molde; el objeto es un ejemplar creado con ese molde.</details>
<details><summary>2. ¿Qué es <code>self</code>?</summary>El propio objeto. Python lo pasa solo como primer parámetro de cada método.</details>
<details><summary>3. ¿Cuándo se ejecuta <code>__init__</code>?</summary>Automáticamente, al crear el objeto.</details>
<details><summary>4. ¿Para qué sirve <code>super()</code>?</summary>Para llamar a un método de la clase base desde la derivada.</details>
<details><summary>5. ¿Qué hace <code>__str__</code>?</summary>Define el texto que se muestra al imprimir el objeto.</details>
<details><summary>6. ¿Qué aporta <code>property</code>?</summary>Validar al leer o asignar un atributo sin cambiar la forma de usarlo.</details>

---

---

## 13. Glosario

| Término | Definición |
|---|---|
| **Clase** | Molde que define atributos y métodos. |
| **Objeto / instancia** | Ejemplar concreto de una clase. |
| **Atributo** | Dato asociado a un objeto. |
| **Método** | Función definida dentro de una clase. |
| **`self`** | Referencia al propio objeto. |
| **`__init__`** | Constructor: inicializa el objeto. |
| **Encapsulación** | Controlar el acceso a los datos internos. |
| **`property`** | Mecanismo para validar el acceso a un atributo. |
| **Herencia** | Crear una clase a partir de otra. |
| **Sobrescribir** | Redefinir en la hija un método de la madre. |

---

---

## 14. Cómo se evalúa esta unidad (RA4)

El examen es **100 % práctico**: se entrega un proyecto con las funciones vacías y una
especificación, y hay que escribir el código.

**La nota sale solo de los casos de prueba.** No hay puntos por presentación ni por
esfuerzo: cada apartado del examen vale en proporción a los casos que tiene, de modo que
**todos los casos valen lo mismo**.

`nota del apartado = (casos superados ÷ casos del apartado) × puntos del apartado`

`nota del examen = suma de los apartados`

### Así es el examen

**Jerarquía de empleados** · entrega `src/empleados.py` · **50 min**

| # | Apartado | Casos | Puntos |
|:---:|---|:---:|:---:|
| **A** | Clase base y descripción | 4 | **3,64** |
| **B** | Herencia | 4 | **3,64** |
| **C** | Validación con `property` | 3 | **2,72** |
| | **TOTAL** | **11** | **10,00** |

Esta tabla viene en el enunciado, así que sabes desde el primer minuto **qué vale cada
parte** y por dónde empezar si vas justo de tiempo.

!!! warning "El examen se reparte sin tests"
    La carpeta `tests/` viene vacía. La especificación son los **docstrings** de cada
    función y los ejemplos del enunciado. Por eso conviene que en el simulacro te
    acostumbres a resolver leyendo el docstring y no el test.

### Así se corrige

Alguien que entrega el examen con **9 de los 11 casos** superados
—se le ha escapado el apartado **B**, donde falla 2 de
4 casos—:

| # | Apartado | Casos superados | Puntos |
|:---:|---|:---:|---|
| A | Clase base y descripción | 4 / 4 | 3,64 / 3,64 |
| B | Herencia | 2 / 4 | 1,82 / 3,64  ← |
| C | Validación con `property` | 3 / 3 | 2,72 / 2,72 |
| | | | **NOTA: 8,18** |

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
