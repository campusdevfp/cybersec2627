# CMO-313 · Fundamentos de programación

Materiales del módulo: **6 unidades**, una por cada Resultado de Aprendizaje. Puedes consultarlos online u offline.

## Unidades

| | Unidad | Qué aprendes | Horas |
|:---:|---|---|:---:|
| **1** | [Estructura del programa](ud1/index.md) | Variables, tipos, operadores, conversión, Python tipado | 8 h |
| **2** | [Funciones y librerías](ud2/index.md) | Dividir el problema en funciones y reutilizar código | 8 h |
| **3** | [Control y excepciones](ud3/index.md) | Decidir, repetir y no romperse con datos raros | 12 h |
| **4** | [Orientación a objetos](ud4/index.md) | Clases, objetos, encapsulación y herencia | 8 h |
| **5** | [Entrada/salida y ficheros](ud5/index.md) | Que los datos sobrevivan al cerrar el programa | 6 h |
| **6** | [Bases de datos](ud6/index.md) | SQLite y las cuatro operaciones CRUD | 8 h |

Las unidades van en orden: cada una se apoya en la anterior.

## Empieza por aquí

- **[El módulo](el-modulo.md)** — qué se aprende en cada unidad, los pesos y cómo se trabaja.
- **[Evaluación](evaluacion.md)** — exámenes, recuperaciones, el candado de los seis RA y la asistencia.

## Recursos

- **[Puesta en marcha](recursos/puesta-en-marcha.md)** — instalar Python, VS Code, el entorno virtual y `mypy`. Se hace en la sesión 2.
- **[Entorno de trabajo](recursos/entorno.md)** — chuleta de entornos virtuales, `pip` y `mypy`.
- **[Proyectos](proyectos/index.md)** — los **6 proyectos base** con sus tests, uno por unidad.
- **[Simulacros de examen](simulacros/index.md)** — un examen de mentira por RA, con los tests publicados, para medirte antes de la prueba real.
- **[Todo el material en una página](completo.md)** — para leer del tirón o exportar a PDF.

## Cómo se trabaja cada unidad

Todas las unidades tienen **la misma estructura**, y siempre en este orden:

| | Qué es |
|---|---|
| **Conceptos** | La teoría, con ejemplos resueltos y comentados que puedes copiar y ejecutar. |
| **Ejercicios** | Todos juntos al final, agrupados por tema y con la solución desplegable. |
| **Práctica final** | En la UD1 y la UD2, un **simulacro tipo test**. En las demás, el **proyecto** de la unidad y un **simulacro** en formato de examen. |

Así puedes leer un concepto, hacer sus ejercicios y saber si lo has entendido **sin esperar
a nadie**.

El módulo va en **aula invertida**: la teoría y los ejercicios los haces tú, y **la clase se
dedica a programar** —dudas, actividades guiadas y proyecto, con el profesor por las mesas—.
Está explicado con detalle en **[El módulo](el-modulo.md)**.

!!! warning "La solución no es el objetivo"
    Leer una solución da sensación de haber aprendido, pero no enseña. Si la abres sin haberlo intentado, el ejercicio no ha servido de nada. Atáscate primero: ahí está el aprendizaje.

## Cómo se evalúa

Un examen por RA, dos por trimestre, y ninguno de teoría. En el **primer trimestre** es un **test de código**: 12 preguntas sobre fragmentos, para comprobar que sabes leerlos. En el **segundo y el tercero** son **retos de programación**: escribes código y se ejecuta contra una batería de casos.

**Los seis RA tienen que estar en 5 o más** para superar el módulo. Lo que suspendas queda pendiente para la ordinaria y, después, la extraordinaria.

Todo el detalle —incluidas las recuperaciones, la FFE y el 15 % de faltas— en **[Evaluación](evaluacion.md)**. La rúbrica exacta de cada unidad está en su última sección.

## Uso offline

Descarga la carpeta `site/` (o genérala con `mkdocs build`) y abre `site/index.html`. Todo funciona sin conexión, incluidos los diagramas y la búsqueda.

!!! tip "Herramientas que usarás"
    Python 3 · Visual Studio Code · `pytest` (pruebas) · `mypy` (tipos) · SQLite (UD6)
