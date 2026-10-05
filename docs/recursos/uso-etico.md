# Uso ético y legal

!!! danger "Léelo antes de tocar cualquier herramienta"
    Este módulo enseña técnicas de seguridad **para defender**. Usarlas contra sistemas que no son tuyos, sin autorización, es un **delito** en España. Esta página no es un formalismo: define la línea que un profesional no cruza nunca.

## Lo que dice la ley

El **Código Penal** castiga, entre otros:

| Artículo | Conducta |
|---|---|
| **197 bis** | Acceder sin autorización a un sistema informático |
| **197 ter** | Facilitar herramientas para hacerlo |
| **264 y ss.** | Dañar u obstaculizar datos o sistemas |

Las penas incluyen prisión. **La intención de "ayudar" o "avisar del fallo" no exime**: sin autorización previa, el acceso ya es delito.

## La autorización lo es todo

Lo único que separa una **prueba de intrusión** legítima de un delito es un documento de **alcance y autorización**, firmado por quien tiene potestad, que define:

- Qué sistemas están **incluidos** y cuáles **excluidos**.
- Qué **técnicas** se permiten y cuáles no.
- La **ventana temporal**.
- Qué se puede ver y qué **no** se puede exfiltrar.
- Contactos y procedimiento de **parada de emergencia**.

Tocar algo fuera del alcance, aunque sea de la misma organización, deja de estar autorizado.

## Reglas de este módulo

1. **Solo el laboratorio.** Todas las prácticas ofensivas se hacen en el laboratorio aislado o sobre `localhost`. Nunca sobre sistemas de terceros ni sobre la red del centro.
2. **Instantáneas.** Haz snapshot antes y restaura después.
3. **Herramientas del proyecto.** El escáner de puertos de la UD5 apunta a `127.0.0.1` por defecto. No lo cambies para apuntar fuera.
4. **Plataformas autorizadas.** Para practicar por tu cuenta, usa TryHackMe, Hack The Box, PortSwigger Academy, VulnHub… que existen para ser atacadas legalmente.
5. **Datos personales.** En las prácticas se usan datos ficticios. No uses datos reales de nadie.

## Divulgación responsable

Si algún día, fuera de este módulo, encuentras por casualidad una vulnerabilidad en un sistema ajeno: **no la explotes**. Comunícala por los cauces de *responsible disclosure* del propietario o a través de INCIBE-CERT. Mirar no autoriza a entrar.

## Ética profesional

La ciberseguridad se basa en la **confianza**: empresas y personas te dan acceso a lo más sensible que tienen. Un profesional protege esa confianza. Las mismas habilidades que aprendes aquí pueden construir o destruir; la diferencia está en el permiso y en la intención, y esa diferencia define tu carrera.
