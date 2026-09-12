# Python para ciberseguridad

Python es el lenguaje más usado en ciberseguridad: legible, con una enorme biblioteca estándar y muchos paquetes especializados. En este módulo lo usamos como **herramienta principal**, con **anotaciones de tipo** y comprobación con `mypy`.

## La librería estándar que usarás

| Módulo | Para qué | Unidad |
|---|---|---|
| `hashlib` | Hashes (integridad, seudonimización) | UD1, UD6 |
| `secrets` | Aleatoriedad criptográfica (sal, tokens) | UD1, UD4 |
| `re` | Expresiones regulares (analizar logs, detectar datos) | UD2, UD6 |
| `collections` | `Counter` para agregar y contar | UD2 |
| `socket` | Red de bajo nivel (escáner de puertos) | UD5 |
| `ipaddress` | Manejo de direcciones y redes | UD3 |
| `csv`, `json` | Leer y escribir datos estructurados | varias |
| `datetime` | Marcas de tiempo, ventanas temporales | UD2 |

## Paquetes útiles (fuera de la estándar)

Para ampliar (retos y laboratorio): `cryptography` (cifrado y firma de verdad), `scapy` (paquetes de red), `requests` (HTTP), `paramiko` (SSH), `python-nmap` (envolver Nmap). No hacen falta para los proyectos evaluables, que usan solo la estándar.

## Estilo de código del módulo

**Siempre tipado.** Las anotaciones documentan y `mypy` caza errores sin ejecutar:

```python
def contar_fallos(estados: list[str]) -> int:
    """Cuenta cuántos estados son 'FALLO'."""
    return sum(1 for e in estados if e == "FALLO")
```

**Funciones pequeñas y puras** cuando se pueda: una función que recibe datos y devuelve un resultado, sin efectos raros, es fácil de probar con `pytest`. Por eso los proyectos separan la lógica (pura, testeable) de la parte que toca la red o el disco.

**Aleatoriedad segura.** Para nada criptográfico usa `secrets`, no `random`:

```python
import secrets
sal = secrets.token_hex(16)     # 16 bytes aleatorios en hexadecimal
```

## Cómo se prueba tu código

Cada proyecto trae una batería de **tests** con `pytest`. Los tests son la **especificación**: describen exactamente qué debe hacer tu código. Tu trabajo es escribir el código hasta que todos pasen.

```bash
pytest          # todos los tests
pytest -x       # para en el primer fallo (recomendado para ir de uno en uno)
pytest -k hash  # solo los tests cuyo nombre contiene 'hash'
mypy src        # comprobación de tipos
```

!!! tip "De uno en uno"
    `pytest -x` se detiene en el primer fallo. Arreglas esa función y sigues. Es mucho más llevadero que enfrentarte a todos los errores a la vez.

!!! warning "No toques los tests"
    Si un test falla, arregla tu código, no el test. En el examen se usa una batería equivalente que tú no puedes modificar.
