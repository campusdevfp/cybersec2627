# Entorno y laboratorio

Antes de la primera unidad, prepara dos cosas: tu **entorno de Python** (para los proyectos) y el **laboratorio aislado** (para las prácticas de seguridad).

## 1. Entorno de Python

### 1.1 Instalar Python y el editor

Instala **Python 3** desde [python.org](https://www.python.org) y **Visual Studio Code** con la extensión de Python. Comprueba la versión:

```bash
python --version      # p. ej. Python 3.12.x
```

### 1.2 Entorno virtual (uno por proyecto)

Un **entorno virtual** aísla los paquetes de cada proyecto para que no se mezclen.

```bash
python -m venv .venv
# Activar:
source .venv/bin/activate          # macOS / Linux
.venv\Scripts\Activate.ps1         # Windows (PowerShell)
# Cuando está activo, el prompt muestra (.venv). Para salir: deactivate
```

> Añade `.venv/` a tu `.gitignore`: el entorno no se sube, se recrea con `requirements.txt`.

### 1.3 Instalar dependencias y trabajar

```bash
pip install -r requirements.txt    # normalmente pytest y mypy
pytest                             # ejecuta los tests del proyecto
pytest -x                          # se detiene en el primer fallo
mypy src                           # comprueba los tipos
```

El ciclo de trabajo de cada proyecto: lees una función con su docstring, la escribes, lanzas `pytest`, y repites hasta que todo está en verde y `mypy` dice *Success*.


### 1.4 Docker y Docker Compose

Muchos laboratorios del módulo se montan con **contenedores**: son reproducibles, desechables y no tocan tu sistema. Instala **Docker Desktop** (Windows/Mac) o **Docker Engine + plugin compose** (Linux) y comprueba:

```bash
docker --version
docker compose version
```

Patrón que usaremos todo el curso: un `docker-compose.yml` levanta uno o varios servicios (un servidor que genera logs, un objetivo con puertos abiertos, un servicio con datos de prueba) y tu **script de Python** trabaja contra ellos. Al terminar, `docker compose down` lo borra todo.

!!! warning "Atención"
    Los laboratorios ofensivos usan redes con `internal: true` (sin salida a Internet) para que nada escape del laboratorio.


!!! warning "Nunca uses `sudo`: usa Docker"
    Si un reto necesita permisos de administrador o levantar servicios (un servidor, un objetivo de escaneo, una base de datos), **no toques tu sistema con `sudo`**: móntalo en un **contenedor** con `docker` / `docker compose`. Es reproducible, aislado y se borra con `docker compose down`. Así nadie se carga su equipo por error.

## 2. El laboratorio de ciberseguridad

Las prácticas de ataque y defensa se hacen en un **laboratorio aislado** de máquinas virtuales, **nunca** sobre sistemas reales ajenos.

### 2.1 Software base

- **VirtualBox** o **VMware** para virtualizar.
- Una red **solo-anfitrión (host-only)**: las VM se ven entre sí pero **no** salen a Internet ni a tu red real.

### 2.2 Máquinas del laboratorio

| VM | Papel | IP sugerida |
|---|---|---|
| **Kali Linux** | Estación de análisis (Rojo) | 10.0.20.10 |
| **Debian** | Servidor a proteger (Azul) | 10.0.20.20 |
| **Windows Server** | Servidor Windows | 10.0.20.30 |
| **Metasploitable** | Objetivo deliberadamente vulnerable | 10.0.20.40 |
| **pfSense** | Cortafuegos / router | 10.0.20.1 |

Red del laboratorio: **10.0.20.0/24** (host-only). DMZ opcional: **10.0.30.0/24**.

!!! warning "Instantáneas antes de cada práctica"
    Haz una **instantánea (snapshot)** de cada VM antes de una práctica ofensiva. Al terminar, restauras y dejas la máquina limpia. Es lo que te permite "romper" sin miedo.

### 2.3 Objetivos de práctica legales

Además del laboratorio, para practicar por tu cuenta usa plataformas **preparadas para ser atacadas legalmente**: TryHackMe, Hack The Box, PortSwigger Web Security Academy, VulnHub, y las aplicaciones DVWA y OWASP Juice Shop dentro de tu lab.

!!! danger "La regla de oro"
    Todo lo de este módulo se practica en el laboratorio o en plataformas que lo autorizan expresamente. Nunca sobre sistemas de terceros. Ver [Uso ético y legal](uso-etico.md).
