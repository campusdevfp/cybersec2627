# El módulo

**CMO-313 · Fundamentos de programación** — módulo optativo de **50 horas**, primer curso de
DAW y DAM. El lenguaje es **Python 3**, siempre con anotaciones de tipo.

Es el módulo donde se aprende a programar desde cero. No se da por sabido nada: se empieza
por qué es una variable y se termina escribiendo una aplicación que guarda sus datos en una
base de datos.

---

## En qué consiste

El módulo está dividido en **seis unidades de trabajo (UT)**. Cada UT se corresponde
exactamente con un **Resultado de Aprendizaje (RA)** del currículo, así que cada unidad se
estudia, se practica y se evalúa por separado.

| UT | Resultado de aprendizaje | Qué sabrás hacer | Horas | Peso |
|:---:|---|---|:---:|:---:|
| **1** | **RA1** · Reconoce la estructura de un programa | Declarar variables tipadas, usar operadores, convertir tipos y dar formato a la salida. Montar un entorno de trabajo con `venv` y `pip`. | 8 h | **15 %** |
| **2** | **RA2** · Escribe y prueba programas sencillos | Partir un problema en funciones, usar parámetros y `return`, manejar listas y aprovechar la librería estándar. | 8 h | **15 %** |
| **3** | **RA3** · Escribe y depura código con estructuras de control | Decidir con `if`, repetir con `while` y `for`, usar diccionarios, controlar errores con excepciones y depurar. | 12 h | **25 %** |
| **4** | **RA4** · Conoce los fundamentos de la POO | Escribir clases con atributos validados, métodos y herencia. | 8 h | **15 %** |
| **5** | **RA5** · Realiza operaciones de E/S con ficheros | Guardar y recuperar información en ficheros de texto, CSV y JSON. | 6 h | **10 %** |
| **6** | **RA6** · Gestiona bases de datos relacionales | Crear tablas en SQLite, hacer el CRUD completo y escribir consultas seguras. | 8 h | **10 %** |
| **—** | **FFE** · Fase de Formación en Empresa | — | — | **10 %** |
| | | | **50 h** | **100 %** |

**Las unidades van en orden y cada una se apoya en la anterior.** No se puede saltar la UD2
y entender la UD3: las funciones aparecen en todo lo que viene después.

!!! info "De dónde sale el 10 % de la FFE"
    La **FFE** (Fase de Formación en Empresa) pondera un 10 % del módulo, que se reparte
    a medias entre el RA5 y el RA6: **5 % con cada uno**. Es un bloque aparte, con su
    propia nota.

### La UD3 es la más importante

Doce horas y el 25 % de la nota. Es la unidad donde de verdad se aprende a programar: hasta
ahí los programas van de arriba abajo en línea recta, y a partir de ahí toman decisiones y
repiten. Si una unidad merece que le eches horas de más, es esa.

---

## Cómo se trabaja: aula invertida

El módulo funciona en **aula invertida**. Dicho en corto: **la teoría la lees tú fuera de
clase, y la clase se dedica a programar.**

No es para que trabajes más, es para que trabajes mejor. Leer una explicación es lo que
puedes hacer solo; escribir código y atascarte es justo lo que conviene hacer con el
profesor delante.

### Qué se espera de ti antes de cada sesión

1. **Leer la sección** que toque. Son cortas.
2. **Ejecutar los ejemplos** en tu ordenador. Leer código sin ejecutarlo no cuenta.
3. **Hacer los ejercicios ** que cierran la sección. Son dos o tres, cortos, y tienen la
   solución desplegable.

Si llegas con eso hecho, la clase te va a servir. Si llegas sin leer, vas a pasarte la hora
viendo cómo los demás avanzan.

### Qué pasa en clase

| Tramo | Qué se hace |
|---|---|
| Primeros 10 min | Dudas de la lectura. Salís a la pizarra a resolver algún ejercicio. |
| 10 min | El profesor explica **solo lo que ha costado**. Nunca más. |
| 30 min | **Taller**: actividades guiadas, ejercicios largos o el proyecto de la unidad. Tú tecleando, el profesor por las mesas. |
| Últimos 5 min | El fallo típico del día y qué leer para la próxima. |

**Más de la mitad de cada clase eres tú escribiendo código.** Esa es la idea.

---

## Los cinco tipos de práctica

Están ordenados de menos a más exigente, y cada uno tiene su función:

| | Qué es | ¿Ves la solución? | ¿Puntúa? |
|---|---|:---:|:---:|
| **Retos rápidos** | Mini-desafíos de 1–2 minutos dentro de la teoría. | A veces | No |
| **Ejercicios de sección** | 3–4 al final de cada sección, con lo recién leído. | **Sí**, desplegable | No |
| **Actividades y ejercicios largos** | Los de clase, más completos y graduados ○◐●. | **Sí**, con pista | No |
| **Proyecto de la unidad** | Un proyecto Python de verdad, con `src/` y `tests/`. | **No**: los tests | No |
| **Simulacro** | Un examen de mentira, con los tests publicados. | **No**: los tests | No |
| **Examen** | Test de código (1.er trim.) o reto de programación sin tests (2.º y 3.º). | No | **Sí** |

La progresión es deliberada: primero ves el patrón con la solución delante, luego te
compruebas solo contra unos tests, y por último lo haces sin red. **Solo lo último puntúa**,
pero sin lo anterior no se llega.

!!! warning "La solución no es el objetivo"
    Abrir la solución sin haberlo intentado da sensación de haber aprendido, y no enseña
    nada. El aprendizaje está justo en el rato en que estás atascado. Aguanta ahí un poco
    más de lo que te apetece.

---

## Qué necesitas

**Python 3** · **Visual Studio Code** · `pytest` (ejecutar los tests) · `mypy` (comprobar
los tipos) · **SQLite** (viene con Python, para la UD6).

Todo se instala en la **sesión 2**, y se instala en clase, entre todos. Es la sesión más
importante del curso en lo práctico: un entorno mal montado da guerra durante meses.

La chuleta de comandos está en **[Entorno de trabajo](recursos/entorno.md)**.

---

## Y la evaluación

Un examen por RA, dos por trimestre, y **ninguno es de teoría**:

| Trimestre | RA | Examen |
|:---:|---|---|
| **1.º** | RA1, RA2 | **Test de código**: 12 preguntas sobre fragmentos de código |
| **2.º** | RA3, RA4 | **Reto de programación** |
| **3.º** | RA5, RA6 | **Reto de programación** |

El primero mide que sepas **leer** código; los otros dos, que sepas **escribirlo**. Está
explicado con detalle, con las recuperaciones y la asistencia, en
**[Evaluación](evaluacion.md)**.
