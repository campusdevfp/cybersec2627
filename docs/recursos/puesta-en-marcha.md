# Puesta en marcha

Todo lo que hay que instalar y configurar, en un sitio. **Esto se hace en la sesión 2, en
clase y entre todos**, así que no hace falta que lo traigas hecho. Guárdalo para cuando
necesites repetirlo o para consultar un comando.

!!! tip "No intentes entenderlo todo hoy"
    Esta página es una **chuleta**, no una unidad. La primera vez la sigues paso a paso sin
    preguntarte por qué; con el tiempo entenderás para qué sirve cada cosa. Lo importante
    ahora es que al final tengas un programa corriendo.

---

## 1. Lo que se instala

| Qué | Para qué | De dónde |
|---|---|---|
| **Python 3** | El lenguaje. Es lo que ejecuta tus programas. | [python.org](https://www.python.org) |
| **Visual Studio Code** | El editor donde escribes el código. | [code.visualstudio.com](https://code.visualstudio.com) |
| Extensión **Python** para VS Code | Colores, autocompletado y el botón de ejecutar. | Desde VS Code, pestaña de extensiones |

Comprueba que Python ha quedado bien instalado:

```bash
python --version
```

Tiene que responder algo como `Python 3.12.3`. Si dice que no encuentra el comando, prueba
con `python3 --version`.

!!! warning "En Windows, marca la casilla"
    El instalador de Python trae abajo una casilla que dice **«Add python.exe to PATH»**.
    Márcala. Si no, el comando `python` no funcionará en la terminal y tendrás que
    reinstalar.

---

## 2. Un proyecto por unidad

Cada unidad se trabaja en su propia carpeta. Dentro de esa carpeta van tu código y las
herramientas que necesita, sin mezclarse con nada más.

```bash
mkdir ud1
cd ud1
```

---

## 3. El entorno virtual

Un **entorno virtual** es una copia aislada de Python para un proyecto concreto.

> **Analogía.** Cada proyecto lleva su propia **mochila** con sus herramientas. Sin entornos
> virtuales, todo va en una única mochila gigante compartida: un día actualizas una
> herramienta para un proyecto y rompes otro sin querer.

<figure markdown>
  ![Entornos virtuales](../assets/diagramas/ud1-entornos.svg#only-light)
  ![Entornos virtuales](../assets/diagramas/ud1-entornos-dark.svg#only-dark)
  <figcaption>Cada proyecto lleva su propio entorno: los paquetes no se mezclan.</figcaption>
</figure>

**Crearlo** (una vez por proyecto):

```bash
python -m venv .venv
```

Eso crea una carpeta `.venv`. **Activarlo** (cada vez que abras la terminal):

```bash
source .venv/bin/activate
```

En **Windows con PowerShell**:

```powershell
.venv\Scripts\Activate.ps1
```

Sabrás que está activado porque el *prompt* de la terminal empieza con `(.venv)`. Para
salir, `deactivate`.

!!! danger "Si el prompt no dice (.venv), estás fuera"
    Y todo lo que instales irá al Python del sistema en vez de al proyecto. Es la causa
    número uno de «a mí no me funciona»: mirar el prompt antes de instalar algo resuelve la
    mitad de los problemas del curso.

---

## 4. Instalar las herramientas

Con el entorno **activado**:

```bash
pip install pytest mypy
```

| Herramienta | Qué hace |
|---|---|
| **pytest** | Ejecuta los tests de los proyectos y te dice si tu código está bien. |
| **mypy** | Comprueba que los tipos cuadran, sin ejecutar el programa. |

Ver lo que hay instalado:

```bash
pip list
```

---

## 5. Guardar las dependencias

```bash
pip freeze > requirements.txt
```

Eso crea un fichero con la lista exacta de paquetes y versiones. Sirve para que otra
persona —o tú en otro ordenador— monte el mismo entorno con una sola orden:

```bash
pip install -r requirements.txt
```

Los proyectos del curso ya vienen con su `requirements.txt`: solo tienes que ejecutar esa
línea.

---

## 6. Las anotaciones de tipo y mypy

En este módulo el código se escribe **anotando los tipos**:

```python
precio: float = 19.95
unidades: int = 3


def importe(precio: float, unidades: int) -> float:
    """Importe de una línea."""
    return precio * unidades
```

Las anotaciones **no cambian nada al ejecutar**: Python las ignora. Sirven para dos cosas.

1. **Documentan.** Quien lee la función sabe qué espera y qué devuelve.
2. **Permiten comprobarlas** con una herramienta: `mypy`.

```bash
mypy mi_programa.py
```

Si todo cuadra responde `Success: no issues found`. Si no, señala la línea:

```text
mi_programa.py:4: error: Unsupported operand types for + ("str" and "int")
```

!!! tip "mypy encuentra fallos antes de ejecutar"
    Un programa puede estar mal y no dar error hasta que el usuario introduce cierto dato.
    `mypy` detecta parte de esos problemas **leyendo el código**, sin ejecutarlo. Por eso en
    los exámenes se exige que pase limpio.

---

## 7. Comandos que usarás todo el curso

```bash
python mi_programa.py          # ejecutar un programa
pytest                         # todos los tests del proyecto
pytest -x                      # parar en el primer fallo
pytest -k media                # solo los tests con "media" en el nombre
mypy src                       # comprobar los tipos
pip install -r requirements.txt
```

---

## 8. Si algo no funciona

| Lo que ves | Qué suele ser | Qué hacer |
|---|---|---|
| `python: command not found` | Python no está en el PATH | Reinstalar marcando «Add python.exe to PATH» |
| `pytest: command not found` | El entorno no está activado | Mirar si el prompt dice `(.venv)` y activarlo |
| `ModuleNotFoundError: No module named 'pytest'` | Instalado fuera del entorno | Activar y `pip install pytest` |
| En PowerShell: «no se puede ejecutar scripts» | Política de ejecución de Windows | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| `pytest` no encuentra ningún test | Estás en la carpeta equivocada | `cd` a la carpeta del proyecto, donde está `pytest.ini` |

!!! tip "Pregunta pronto"
    Un entorno mal montado no se arregla solo y arrastra problemas durante semanas. Si algo
    no cuadra en la sesión 2, dilo en el momento: es el día que está reservado para eso.
