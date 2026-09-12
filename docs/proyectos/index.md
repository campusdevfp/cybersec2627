# Proyectos

Cada unidad se cierra con un **proyecto en Python** que reúne toda su práctica. Es la forma en que se evalúa el módulo: tú escribes el código, y una batería de **tests** te dice si funciona, igual que en el examen.

## Los seis proyectos

| Unidad | Proyecto | Módulo | Qué practicas |
|:---:|---|---|---|
| [UD1](ud1/README.md) | Verificador de integridad | `integridad.py` | `hashlib`, integridad, forense |
| [UD2](ud2/README.md) | Detector de fuerza bruta | `deteccion.py` | `re`, `Counter`, análisis de logs |
| [UD3](ud3/README.md) | Motor de cortafuegos | `cortafuegos.py` | POO, ACL, primera coincidencia |
| [UD4](ud4/README.md) | Riesgo y contraseñas | `riesgo.py` | riesgo, ALE, política, MFA |
| [UD5](ud5/README.md) | Escáner de puertos | `escaner.py` | `socket`, red (solo localhost) |
| [UD6](ud6/README.md) | Cumplimiento y anonimización | `cumplimiento.py` | RGPD, `hashlib`, `re` |

## Cómo se trabaja cualquier proyecto

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest                          # al principio falla: aún no has escrito nada
mypy src                        # cuando todo esté verde, debe decir Success
```

1. Lee cada función y su docstring.
2. Sustituye los `TODO` por tu código y borra el `raise NotImplementedError`.
3. Lanza `pytest -x`, arregla el primer fallo, repite.
4. Termina cuando todo está en verde y `mypy` dice *Success*.

!!! warning "Los tests son la especificación"
    No se tocan. Describen exactamente el comportamiento esperado, y el examen usa una batería equivalente.

!!! danger "Uso ético"
    El proyecto de la UD5 (escáner de puertos) apunta a `127.0.0.1`. Úsalo solo contra tus máquinas o el laboratorio. Ver [Uso ético y legal](../recursos/uso-etico.md).
