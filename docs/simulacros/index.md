# Prepararse para el examen

Una prueba de práctica por cada RA, con el mismo formato y la misma dificultad que la de
verdad. La diferencia es que aquí **tienes las soluciones**.

Ojo, porque el examen **no es igual en los tres trimestres**:

| Trimestre | RA | Examen | Prueba de práctica |
|:---:|---|---|---|
| **1.º** | RA1, RA2 | **Test de código**: 12 preguntas de opción múltiple | test con las respuestas al final |
| **2.º** | RA3, RA4 | **Reto de programación**: escribir código | proyecto con los tests publicados |
| **3.º** | RA5, RA6 | **Reto de programación** | proyecto con los tests publicados |

El primer trimestre es para arrancar: se trata de **leer código y entender qué hace**. A
partir del segundo ya se trata de escribirlo.

---

## Primer trimestre: tests de código

| RA | Test de práctica | Qué entra | Preguntas |
|:---:|---|---|:---:|
| **1** | [Elementos del lenguaje](ra1/README.md) | tipos, conversión, operadores, constantes, formato | 12 |
| **2** | [Funciones y librerías](ra2/README.md) | `return` vs `print`, parámetros, ámbito, listas, `math` | 12 |

**Todas las preguntas son sobre código.** No hay definiciones: se te da un fragmento y
tienes que decir qué imprime, qué error da, cuánto vale una expresión o cuál de cuatro
versiones es la correcta.

### Cómo se puntúa

| | |
|---|---|
| Acierto | **+0,83** puntos |
| Error | **−0,28** puntos |
| En blanco | 0 |

`nota = (aciertos − errores ÷ 3) × 0,83`, con un mínimo de 0.

Se resta porque hay cuatro opciones: así **marcar al azar no compensa**. Si dudas entre
dos, marca; si no tienes ni idea, déjalo en blanco.

!!! tip "Hazlo sin ejecutar nada"
    45 minutos, sin ordenador y sin apuntes, como el de verdad. Contesta primero y
    **después** pasa cada fragmento por Python. Ahí es donde se aprende de verdad: no solo
    ves qué fallaste, sino por qué.

---

## Segundo y tercer trimestre: retos de programación

| RA | Simulacro | Qué se evalúa | Tests | Descargar |
|:---:|---|---|:---:|:---:|
| **3** | [Registro de pulsaciones](ra3/README.md) | condiciones, bucles y excepciones | 21 | [descargar](simulacro-ra3.zip) |
| **4** | [Catálogo de dispositivos](ra4/README.md) | `property`, herencia y sobrescritura | 14 | [descargar](simulacro-ra4.zip) |
| **5** | [Recetario en CSV y JSON](ra5/README.md) | ficheros, CSV, JSON y codificación | 13 | [descargar](simulacro-ra5.zip) |
| **6** | [Museo en SQLite](ra6/README.md) | CRUD y consultas parametrizadas | 11 | [descargar](simulacro-ra6.zip) |

Aquí sí se escribe código. Son proyectos con el mismo formato, tamaño y rúbrica que el
examen, pero **con los tests publicados**: los ejecutas y te dicen si vas bien.

### Cómo se puntúa

| Concepto | Cómo se calcula |
|---|---|
| Nota de un apartado | (casos superados ÷ casos del apartado) × puntos del apartado |
| Nota del examen | suma de todos los apartados, sobre **10** |

Cada simulacro trae su tabla de apartados, idéntica en formato a la del examen. Cuando
termines, aplícala y tendrás la nota que sacarías.

!!! warning "El examen de verdad va sin tests"
    En el simulacro los tests te dicen si vas bien; en el examen no los hay. La
    especificación son los **docstrings** de cada función y los ejemplos del enunciado. Por
    eso conviene que aquí te acostumbres a resolver leyendo el docstring, y que mires el
    test solo cuando algo falle.

---

## En qué se diferencian del proyecto de la unidad

| | Proyecto de unidad | Prueba de práctica | Examen |
|---|---|---|---|
| Cuándo | durante toda la unidad | la sesión previa al examen | el día del examen |
| Duración | varias sesiones | 45 min | 45–50 min |
| Soluciones | no: los tests | **sí** | no |
| Se califica | no | no | sí |

El proyecto es para **aprender**: largo y con calma. La prueba de práctica es para
**medirte**: mismo tamaño que el examen, contrarreloj, y al terminar sabes exactamente qué
nota habrías sacado.
