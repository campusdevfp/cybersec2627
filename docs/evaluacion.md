# Evaluación

Todo lo que necesitas saber sobre cómo se te califica en este módulo. Sin letra pequeña: la
rúbrica es pública desde el primer día y la corrección es automática.

---

## 1. Dos evaluaciones distintas

Conviene no confundirlas, porque solo una pone nota.

| | Evaluación **formativa** | Evaluación **calificativa** |
|---|---|---|
| Qué es | Los ejercicios de clase, el proyecto de cada unidad y los simulacros. | Los exámenes prácticos y la FFE. |
| Para qué | Que compruebes **por ti mismo** si vas bien, y a tiempo de arreglarlo. | Poner la nota del módulo. |
| ¿Puntúa? | **No.** | **Sí.** |
| ¿Obligatoria? | Sí: se hace en clase y se comprueba. | Sí. |

### La formativa no puntúa, pero decide tu nota

Suena raro dicho así, pero es exacto: los ejercicios no suman puntos y, a la vez, son lo
único que hace que apruebes el examen.

**Lo que tienes que hacer y comprobar:**

- Los **ejercicios ** de cada sección, antes de la clase correspondiente.
- Las **actividades y ejercicios largos** que se trabajan en el aula.
- El **proyecto de la unidad**: hasta tener los tests en verde y `mypy` limpio.
- El **simulacro**, contrarreloj, la sesión anterior al examen.

Todos traen la manera de comprobarte: solución desplegable en los primeros, tests que
ejecutas tú en los dos últimos. No hay que entregar nada, pero el profesor pregunta por
ellos al empezar cada clase.

---

## 2. La unidad de evaluación es el RA

Cada una de las seis unidades se corresponde con un **Resultado de Aprendizaje**, y **cada
RA se califica por separado de 0 a 10**. Un RA está superado con **5**.

| Trimestre | RA que se examinan | Peso de cada uno | Instrumento |
|:---:|---|---|---|
| **1.º** | RA1 y RA2 | 15 % + 15 % | test de código |
| **2.º** | RA3 y RA4 | 25 % + 15 % | reto de programación |
| **3.º** | RA5 y RA6 | 10 % + 10 % | reto de programación |
| — | **FFE** (Fase de Formación en Empresa) | 10 % |

**Cada trimestre hay un examen de cada uno de sus dos RA.** En ninguno hay teoría ni
preguntas de desarrollo: o lees código y dices qué hace, o lo escribes.

La nota que aparece en el boletín de cada trimestre es la media ponderada de sus dos RA.

---

## 3. El examen no es igual en los tres trimestres

| Trimestre | RA | Instrumento |
|:---:|---|---|
| **1.º** | RA1, RA2 | **Test de código**: 12 preguntas de opción múltiple sobre fragmentos de código |
| **2.º** | RA3, RA4 | **Reto de programación**: escribir código, corregido con casos de prueba |
| **3.º** | RA5, RA6 | **Reto de programación** |

El primer trimestre es para **arrancar**: se evalúa que sepas **leer** código y predecir qué
hace, que es el paso previo a escribirlo. A partir del segundo ya se trata de escribirlo.

### Primer trimestre: test de código

12 preguntas de opción múltiple, **todas sobre código**: qué imprime un fragmento, qué
error da, cuánto vale una expresión o cuál de cuatro versiones de una función es la
correcta. Ninguna de definiciones.

| | |
|---|---|
| Acierto | **+0,83** |
| Error | **−0,28** |
| En blanco | 0 |

`nota = (aciertos − errores ÷ 3) × 0,83`, con mínimo 0. Se resta porque hay cuatro
opciones: **marcar al azar no compensa**. Si dudas entre dos, marca; si no tienes ni idea,
déjalo en blanco.

### Segundo y tercer trimestre: reto de programación

Siempre con la misma rúbrica, la conoces desde el primer día:

| Concepto | Cómo se calcula |
|---|---|
| Nota de un apartado | (casos superados ÷ casos del apartado) × puntos del apartado |
| Nota del examen | suma de todos los apartados, sobre **10** |

Los puntos de cada apartado son **proporcionales a sus casos**, así que todos los casos
valen lo mismo. El reparto viene en el enunciado.

Cada examen se divide en **apartados** (una función, o un bloque de funciones). El enunciado
trae la tabla con los casos y los puntos de cada uno, así que sabes desde el primer minuto
qué vale cada parte. La última sección de cada unidad tiene el ejemplo completo, con una
corrección resuelta.

**No hay puntos por presentación ni por esfuerzo.** Entregar el fichero con su nombre, que
`mypy src` pase sin errores y que cada función tenga su docstring son obligatorios, pero no
puntúan aparte: un fichero que no se puede importar da cero casos superados, que es mucho
peor que perder un punto.

!!! warning "El examen se reparte sin tests"
    En clase los tests te dicen si vas bien. **En el examen no los hay**: la especificación
    son los *docstrings* de cada función y los ejemplos del enunciado. Por eso conviene que
    en los simulacros te acostumbres a resolver leyendo el docstring, y no el test.

---

## 4. Convocatorias: qué pasa si suspendes un RA

Un RA no superado **queda pendiente**. No desaparece ni se compensa: hay que recuperarlo.

``` text
Evaluación continua  →  ¿Los 6 RA ≥ 5?
                          │
              sí ─────────┴───────── no
              │                       │
       MÓDULO SUPERADO        ORDINARIA (solo los RA pendientes)
                                      │
                          ¿Ya están los 6 RA ≥ 5?
                              │
                  sí ─────────┴───────── no
                  │                       │
           MÓDULO SUPERADO      EXTRAORDINARIA (solo los que sigan pendientes)
```

- **Ordinaria.** Te presentas **solo a los RA que tengas pendientes**, sean uno o los seis.
  Los que ya tenías aprobados se conservan con su nota.
- **Extraordinaria.** Igual: solo los que sigan pendientes tras la ordinaria.
- La nota nueva **sustituye** a la anterior.

Los exámenes de recuperación tienen **el mismo formato y la misma dificultad** que el de
continua: otro enunciado del mismo tipo, con la misma rúbrica.

---

## 5. El candado: los seis RA tienen que estar aprobados

Esta es la regla que más conviene entender:

!!! danger "Hacen falta los SEIS"
    El módulo está **SUPERADO** solo si **los seis RA están en 5 o más**.

    Si queda alguno por debajo de 5, el módulo es **NO SUPERADO** y la nota final se limita
    a **4**, por muy alta que sea la media.

No hay compensación entre RA. Un 10 en la UD3 no tapa un 4 en la UD5: son aprendizajes
distintos y se acreditan por separado.

**Un ejemplo.** Alguien con RA1 8, RA2 8, RA3 9, RA4 7, RA5 4, RA6 8 y FFE 8 tiene una media
de 8,05 — pero el RA5 está en 4. Resultado: **NO SUPERADO, nota 4**. Le basta con recuperar
el RA5 en la ordinaria para que el módulo quede superado con su nota real.

### La FFE pondera, pero no bloquea

La **FFE** aporta su 10 % a la media. **No tiene que estar aprobada** para superar el
módulo: el candado son los seis RA. Al revés tampoco funciona: una FFE de 10 no rescata un
RA suspenso.

---

## 6. Asistencia: el 15 %

Superar el **15 % de faltas** —**justificadas o injustificadas**, cuentan todas— supone la
**pérdida del derecho a la evaluación continua**.

Qué implica en la práctica:

- **Conservas los RA que ya tuvieras superados.** No se pierde lo aprobado.
- Los que te queden pendientes los recuperas en la **convocatoria ordinaria**.
- Y si tras esa siguen pendientes, en la **extraordinaria**, como todo el mundo.

En un módulo de 50 horas ese 15 % son unas **7 sesiones**. Es menos de lo que parece: se
llega ahí antes de darse cuenta.

!!! warning "Y hay algo peor que perder la continua"
    Este módulo se construye en escalera: cada unidad se apoya en la anterior. Faltar a las
    sesiones de la UD2 no te complica la UD2, te complica **todo lo que viene después**.
    Recuperar contenido perdido aquí cuesta bastante más que en otros módulos.

---

## 7. Resumen en seis líneas

1. Seis RA, uno por unidad, **cada uno se aprueba por separado con un 5**.
2. Dos exámenes por trimestre, uno por RA. **Ninguno de teoría.**
3. En el **1.er trimestre** son **tests de código**; en el 2.º y el 3.º, **retos de programación** corregidos con casos de prueba.
4. Lo que suspendas queda **pendiente**: ordinaria y después extraordinaria, solo con eso.
5. **Los seis RA ≥ 5** o el módulo no está superado (nota limitada a 4).
6. Los ejercicios de clase **no puntúan**, pero son lo que hace que apruebes.
