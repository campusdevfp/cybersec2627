# Retos de programación

> Una colección de **problemas típicos de ciberseguridad de hoy**, pensados para **programarlos y pasarlo bien**. Python es la herramienta principal, pero cada reto sugiere la librería que usa la industria (`requests`, `BeautifulSoup`, `PyJWT`, `cryptography`…). No hay que hacerlos todos ni en orden: elige por tema o por el RA que estés dando.

!!! danger "Regla de oro: todo contra tu laboratorio o tus propios datos"
    Estos retos se resuelven **contra tus contenedores del laboratorio**, contra **datos que generas tú** o contra **tus propios servicios**. Nunca contra sistemas, webs o personas de terceros. La misma técnica es una práctica en tu lab y un delito fuera de él (arts. 197 y 264 del Código Penal). Ver [Uso ético y legal](../recursos/uso-etico.md).

## Cómo trabajarlos

Cada reto tiene: **contexto** (por qué importa ahora), **objetivo** (qué construir), **herramientas** sugeridas, **criterios de aceptación** y una **pista** desplegable. Programa con tipos y comprueba con `mypy`. Las librerías extra están en `requirements-retos.txt`:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-retos.txt   # requests, beautifulsoup4, PyJWT, cryptography, dnspython, Pillow
```

---

## Bloque 1 · Criptografía y contraseñas (RA1, RA4)

### R1 · ¿Está tu contraseña en una filtración? (k-anonymity)

!!! analogia "Por qué mola"
    Es exactamente lo que hace el aviso "esta contraseña apareció en una filtración" de tu navegador. Y lo bonito: se consulta **sin enviar tu contraseña**, ni siquiera su hash completo.

**Contexto.** El servicio *Have I Been Pwned* permite comprobar si un hash SHA-1 de una contraseña está en filtraciones usando **k-anonymity**: solo le envías los **5 primeros caracteres** del hash y te devuelve todos los sufijos que empiezan así; tú buscas el tuyo en local.

**Objetivo.** `veces_filtrada(contrasena: str) -> int` que devuelva cuántas veces aparece esa contraseña en filtraciones (0 si ninguna).

**Herramientas.** `hashlib`, `requests`. Endpoint: `https://api.pwnedpasswords.com/range/PRIMEROS5`.

**Criterios de aceptación.** Nunca envías la contraseña ni el hash completo · comparas en local ignorando mayúsculas/minúsculas del hex · manejas el caso "0 apariciones".

<details class="sol"><summary>Pista</summary>
Calcula `sha1(contraseña).hexdigest().upper()`. Envía `range/` + los 5 primeros. La respuesta es `SUFIJO:conteo` por línea; busca el sufijo (los 35 caracteres restantes) y devuelve el conteo.
</details>

### R2 · Autenticación en dos pasos: implementa TOTP (RFC 6238)

!!! analogia "Por qué mola"
    Vas a reimplementar el código de 6 dígitos que cambia cada 30 s de Google Authenticator / Authy. Con 20 líneas entiendes para siempre cómo funciona el 2FA.

**Objetivo.** `totp(secreto_base32: str, t: int | None = None) -> str` que genere el código de 6 dígitos, y `valida(secreto, codigo)` que acepte también el intervalo anterior (tolerancia de reloj).

**Herramientas.** `base64`, `hmac`, `hashlib`, `struct`, `time`.

**Criterios de aceptación.** Coincide con una app real para el mismo secreto · ventana de 30 s · validación con ±1 intervalo · tipado limpio.

<details class="sol"><summary>Pista</summary>
Contador = `tiempo // 30`, empaquetado como 8 bytes big-endian. HMAC-SHA1 del contador con el secreto (decodificado de base32). Truncamiento dinámico (RFC 4226) y `% 1_000_000`, rellenando a 6 cifras.
</details>

### R3 · Rompe tus propios hashes (y aprende por qué salar)

!!! warning "Solo hashes que generas tú"
    Este reto trabaja sobre una lista de hashes que **creas tú mismo** a partir de un diccionario. No es para atacar credenciales ajenas: es para *sentir* por qué MD5/SHA sin sal son un desastre para contraseñas.

**Objetivo.** Dado un fichero de hashes (que generas de un diccionario), un crackeador por diccionario con **reglas** simples (añadir 0–99, poner en mayúscula la inicial, sustituir `a→@`, `e→3`). Luego repite con `bcrypt`/`argon2` y **cronometra** la diferencia.

**Herramientas.** `hashlib`, `itertools`, `time`; para la comparación, `bcrypt` o `argon2-cffi`.

**Criterios de aceptación.** Recupera las contraseñas del diccionario que sí están · informa de aciertos/tiempo · escribe 3 líneas de conclusión sobre sal y funciones lentas.

<details class="sol"><summary>Pista</summary>
Precalcula un dict `hash → palabra` aplicando las reglas al diccionario y busca cada hash objetivo. Con bcrypt no puedes precalcular (la sal va incrustada): tienes que probar `bcrypt.checkpw` uno a uno, y ahí verás por qué es lento a propósito.
</details>

---

## Bloque 2 · Web y APIs (RA2, RA3)

### R4 · Auditor de cabeceras de seguridad

**Contexto.** Antes de publicar una web se revisan sus cabeceras: `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`. Faltan en la mayoría de sitios.

**Objetivo.** `auditar(url) -> dict` que puntúe (A–F) las cabeceras de **tu** contenedor web del laboratorio y explique qué falta y por qué.

**Herramientas.** `requests`.

**Criterios de aceptación.** Detecta presencia/ausencia de las 5 cabeceras clave · da una nota y una recomendación por cada una · funciona contra `http://localhost:8080` de tu `docker-compose`.

<details class="sol"><summary>Pista</summary>
`requests.get(url).headers` es un dict insensible a mayúsculas. Puntúa restando por cada cabecera ausente. Para HSTS comprueba además `max-age`.
</details>

### R5 · OSINT ligero con BeautifulSoup: fingerprint de una web (de tu lab)

!!! analogia "Por qué mola"
    Es la fase de *reconocimiento* de cualquier pentest, pero hecha con buen gusto: parsear HTML y sacar información útil. Lo haces contra una web que tú mismo levantas en Docker.

**Objetivo.** `fingerprint(url) -> dict` que, con **BeautifulSoup**, extraiga de una página de tu laboratorio: título, tecnología (`<meta name="generator">`, cabecera `Server`), correos (`mailto:` y por regex), formularios con sus campos, y enlaces externos.

**Herramientas.** `requests`, `bs4` (BeautifulSoup). Alternativas válidas: `selectolax`, `lxml`.

**Criterios de aceptación.** No revienta si falta un elemento · deduplica correos y enlaces · distingue enlaces internos de externos con `urllib.parse`.

<details class="sol"><summary>Pista</summary>
`soup.find_all("form")` → por cada uno, `find_all(["input","select","textarea"])` y lee `name`/`type`. Para correos, combina `a[href^=mailto]` con un `re.findall` de patrón de email sobre `soup.get_text()`.
</details>

### R6 · ¿Es esta URL de phishing? (heurística)

**Contexto.** Los filtros antiphishing puntúan URLs por señales: dominio con IP en vez de nombre, `@` en la URL, punycode (`xn--`), demasiados subdominios, TLD sospechoso, o **typosquatting** (parecido a una marca conocida).

**Objetivo.** `riesgo_url(url, marcas: list[str]) -> tuple[int, list[str]]` que devuelva una puntuación 0–100 y las razones.

**Herramientas.** `urllib.parse`, `difflib` (para la distancia a marcas), `re`.

**Criterios de aceptación.** Al menos 5 señales · `paypa1.com` o `micros0ft-login.xyz` puntúan alto · una URL legítima de la lista de marcas puntúa bajo.

<details class="sol"><summary>Pista</summary>
`difflib.SequenceMatcher(None, dominio, marca).ratio()` alto (p. ej. > 0,8) pero **no igual** = probable typosquatting. Suma puntos por cada señal y devuelve las razones para poder explicarlas.
</details>

### R7 · Token JWT: por qué hay que validar el algoritmo

!!! warning "Tokens de laboratorio"
    Genera tú los tokens (con un secreto débil a propósito) para el ejercicio. El objetivo es **entender el fallo para defenderte de él**, no atacar tokens ajenos.

**Objetivo.** (a) Decodifica un JWT sin verificar y muéstralo. (b) Detecta el ataque `alg: none`. (c) Sobre un token HS256 con secreto débil, pruébalo contra una lista corta de secretos y avisa si cae. (d) Escribe la versión **correcta** de verificación (algoritmo fijado + secreto fuerte).

**Herramientas.** `PyJWT` (o `base64` + `hmac` a mano), `hashlib`.

**Criterios de aceptación.** Distingues cabecera/carga/firma · rechazas `alg:none` · tu verificador seguro fija `algorithms=["HS256"]` y valida `exp`.

<details class="sol"><summary>Pista</summary>
Un JWT son tres bloques base64url separados por puntos. Con PyJWT: `jwt.decode(tok, options={"verify_signature": False})` para inspeccionar; para verificar de verdad, `jwt.decode(tok, secreto, algorithms=["HS256"])`. La lección: nunca aceptar el `alg` que propone el token.
</details>

---

## Bloque 3 · Red, servicios y monitorización (RA3, RA5)

### R8 · ¿Caduca tu certificado TLS?

**Contexto.** Media caída de servicios "misteriosa" es un certificado caducado. Un script que avise con antelación vale oro.

**Objetivo.** `caducidad(host, puerto=443) -> dict` que devuelva emisor, SAN, días hasta la expiración y una alerta si quedan menos de 30. Pruébalo contra tu contenedor HTTPS del laboratorio.

**Herramientas.** `ssl`, `socket`, `datetime`.

**Criterios de aceptación.** Extrae `notAfter` y lo convierte a fecha · lista los nombres del SAN · alerta por umbral configurable.

<details class="sol"><summary>Pista</summary>
`ctx = ssl.create_default_context()`, envuelve un socket con `server_hostname=host` y usa `getpeercert()`. `notAfter` se parsea con `ssl.cert_time_to_seconds` o `datetime.strptime(..., "%b %d %H:%M:%S %Y %Z")`.
</details>

### R9 · Descubridor de subdominios (en tu zona de laboratorio)

!!! warning "Solo tu dominio de laboratorio"
    Resuelve nombres **de una zona que controlas** (un contenedor DNS del lab o entradas en tu `/etc/hosts`). Enumerar subdominios de terceros a gran escala puede considerarse abusivo.

**Objetivo.** Lee un diccionario de nombres y comprueba cuáles resuelven en tu dominio de laboratorio; para los que existan, muestra su IP.

**Herramientas.** `socket.getaddrinfo` o `dnspython`. Bonus: hazlo concurrente con `concurrent.futures`.

**Criterios de aceptación.** Diccionario configurable · maneja los que no resuelven sin romperse · salida ordenada.

<details class="sol"><summary>Pista</summary>
`socket.getaddrinfo(f"{sub}.{dominio}", None)` lanza `socket.gaierror` si no resuelve: captúralo. Para concurrencia, un `ThreadPoolExecutor` con 20 hilos multiplica la velocidad porque es I/O.
</details>

### R10 · Mini-honeypot que registra quién llama

!!! analogia "Por qué mola"
    Un honeypot es un servicio "cebo": no da servicio real, solo **apunta quién intenta conectarse**. Es defensa activa y entretenidísimo de ver funcionando en el lab.

**Objetivo.** Un servidor TCP (en un contenedor) que escuche en un puerto típico (p. ej. 2323 simulando telnet), registre `fecha, IP, datos recibidos` de cada conexión y nunca dé acceso real.

**Herramientas.** `socketserver` (o `asyncio`). Se despliega con Docker en la red del laboratorio.

**Criterios de aceptación.** Registra cada intento con marca de tiempo · no bloquea con varias conexiones · log en fichero.

<details class="sol"><summary>Pista</summary>
`socketserver.ThreadingTCPServer` + un `StreamRequestHandler` que en `handle()` escribe una línea de log y cierra. Pruébalo desde otro contenedor con `nc honeypot 2323`.
</details>

---

## Bloque 4 · Defensa, forense y cumplimiento (RA1, RA2, RA6)

### R11 · Escáner de secretos en el código (tipo gitleaks)

**Contexto.** Subir por error una clave AWS o un token a un repositorio es de los incidentes más comunes hoy. Un escáner que los detecte **antes** del commit evita el disgusto.

**Objetivo.** Recorre un directorio y detecta secretos con expresiones regulares: claves AWS (`AKIA…`), tokens tipo `ghp_…`, claves privadas (`-----BEGIN … PRIVATE KEY-----`), URLs con contraseña. Salida con fichero, línea y tipo.

**Herramientas.** `re`, `pathlib`. Bonus: pensar cómo sería un *hook* de pre-commit.

**Criterios de aceptación.** Al menos 4 patrones · ignora binarios y `.git` · no da falsos positivos con un `README` normal.

<details class="sol"><summary>Pista</summary>
Recorre con `Path.rglob("*")`, salta si `is_dir()` o la ruta contiene `.git`. Lee como texto con `errors="ignore"`. Un dict `{nombre: patrón compilado}` y `finditer` para tener número de línea.
</details>

### R12 · Detector de patrones de ataque en logs (Log4Shell, traversal, SQLi)

**Contexto.** Cuando salta una vulnerabilidad como Log4Shell, lo primero es **buscar en los logs** si ya te la intentaron. Patrones como `${jndi:`, `../../`, `' OR '1'='1` o `<script>` son señales claras.

**Objetivo.** `analizar(ruta_log) -> list[dict]` que marque líneas sospechosas clasificando el tipo (JNDI/traversal/SQLi/XSS) y la IP de origen.

**Herramientas.** `re`, `collections.Counter`. Genera tú un log de ejemplo (o usa el de los laboratorios de RA2).

**Criterios de aceptación.** ≥ 4 familias de patrones · cuenta ataques por IP · resumen final de las 3 IP más ruidosas.

<details class="sol"><summary>Pista</summary>
Un dict de `familia → regex`. Por cada línea, prueba todas; si alguna casa, extrae la IP con otro regex y acumula en un `Counter`. `most_common(3)` da el resumen.
</details>

---

## Reto integrador (para nota)

### RX · Panel de "salud de seguridad" de tu laboratorio

Combina tres retos anteriores en un solo informe: audita las **cabeceras** (R4) de tu web, comprueba la **caducidad TLS** (R8) y **escanea secretos** (R11) del código del proyecto, y saca un único informe (texto o HTML) con semáforo por sección. Todo orquestado con un `docker-compose` que levante los servicios objetivo del laboratorio.

!!! reto "Criterios de aceptación"
    Un solo comando genera el informe · cada sección tiene nota y recomendaciones · el código está tipado (`mypy` limpio) y documentado · el `docker-compose` levanta y derriba el entorno.
