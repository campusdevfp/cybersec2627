# Unidad 1 · Fundamentos de seguridad, criptografía y forense

> **Módulo:** CMO-314 · Ciberseguridad · **RA1** · **Duración:** 20 h · **Peso:** 15 % · **Herramienta:** Python 3 (tipado) + `cryptography`

Esta es la unidad de **cimientos**. Aquí sale por primera vez el patrón que vas a repetir seis veces este curso: **entender el problema → resolverlo con código real → medir que funciona**. Vas a tocar los tres pilares de la seguridad, y las dos disciplinas que sostienen casi todo lo demás: **criptografía** (hash, cifrado, firma, certificados) y **análisis forense**. Al terminar habrás construido, línea a línea, un **verificador de integridad** de nivel profesional — el mismo principio que usan `sha256sum`, `debsums`, AIDE o Tripwire.

!!! reto "El reto de la unidad"
    **Detecta si unos ficheros han sido manipulados.** Vas a construir un verificador de integridad con manifiesto, auditoría y CLI. Todo lo de abajo es tu **entrenamiento** para llegar a resolverlo tú solo y demostrarlo en el examen.

```mermaid
flowchart TB
    A["Principios C·I·D"] --> B["Seguridad física,<br/>ambiental y lógica"]
    A --> R["Amenaza · Vulnerabilidad<br/>Riesgo"]
    A --> C["Criptografía"]
    C --> C1["Hash e integridad"]
    C --> C2["Cifrado simétrico<br/>y asimétrico"]
    C --> C3["Firma y<br/>certificados (PKI)"]
    C1 --> D["Análisis forense<br/>cadena de custodia"]
    C3 --> D
    C1 --> P["RETO<br/>Verificador de integridad"]
    D --> P
    style P fill:#d1fae5,color:#065f46,stroke:#10b981,stroke-width:3px
    style A fill:#dbeafe,color:#1e3a8a,stroke:#3b82f6,stroke-width:2px
```

**Qué sabrás hacer al terminar:** explicar C·I·D y ampliarlo con autenticidad/trazabilidad · calcular y comparar hashes con criterio · cifrar y descifrar de verdad (simétrico y asimétrico) con `cryptography` · firmar un documento y generar un certificado X.509 · aplicar las fases del análisis forense y la cadena de custodia · escribir Python tipado con CLI profesional, comprobado con `mypy` y `pytest`.

**Cómo se trabaja (aula invertida):** lees la sección y ejecutas los ejemplos antes de clase, con el *reto rápido* intentado → en clase resuelves las actividades y avanzas el reto en parejas, con ayuda al lado.

!!! danger "Antes de nada: uso ético y legal"
    Vas a manejar herramientas y técnicas de seguridad. Se usan **solo** sobre tus propios sistemas o el laboratorio autorizado. Manipular sistemas ajenos sin permiso es delito (arts. 197 y 264 del Código Penal). Lee [Uso ético y legal](../recursos/uso-etico.md).

---

## 1. ¿Qué es la seguridad de la información?

Es el conjunto de medidas para proteger datos y servicios frente a accesos, alteraciones o interrupciones no autorizados. No es un producto que se compra: es una propiedad que se **diseña por capas** y se mantiene en el tiempo.

### 1.1 Los tres pilares: C·I·D

| Pilar | Qué garantiza | Se rompe cuando… | La cripto que ayuda |
|---|---|---|---|
| **Confidencialidad** | Solo accede quien está autorizado | Se filtra una base de datos | Cifrado (§5) |
| **Integridad** | La información no se altera sin permiso | Alguien modifica una factura | Hash / firma (§4, §6) |
| **Disponibilidad** | El servicio está accesible cuando se necesita | Un ataque tumba la web | Copias, redundancia |

Se amplían con **autenticidad** (el origen es quien dice ser) y **trazabilidad** (queda registro de quién hizo qué):

```mermaid
flowchart LR
    subgraph "Pilares clásicos"
    Cf["Confidencialidad"]
    In["Integridad"]
    Di["Disponibilidad"]
    end
    subgraph "Ampliación"
    Au["Autenticidad"]
    Tr["Trazabilidad"]
    end
    In -.->|"la firma añade"| Au
    Au -.->|"registrar quién firmó"| Tr
```

Lo modelamos ya con código — nada de listas en abstracto:

```python title="clasificar_incidentes.py"
from dataclasses import dataclass
from enum import Enum

class Pilar(Enum):
    CONFIDENCIALIDAD = "C"
    INTEGRIDAD = "I"
    DISPONIBILIDAD = "D"

@dataclass
class Incidente:
    descripcion: str
    pilar: Pilar

INCIDENTES = [
    Incidente("Ransomware cifra los ficheros del servidor", Pilar.DISPONIBILIDAD),
    Incidente("Un empleado copia la lista de clientes a un USB", Pilar.CONFIDENCIALIDAD),
    Incidente("Cambian el número de cuenta en un albarán", Pilar.INTEGRIDAD),
    Incidente("Un ataque DDoS satura el servidor web", Pilar.DISPONIBILIDAD),
]

for i in INCIDENTES:
    print(f"[{i.pilar.name:16}] {i.descripcion}")
```

```text title="Salida"
[DISPONIBILIDAD ] Ransomware cifra los ficheros del servidor
[CONFIDENCIALIDAD] Un empleado copia la lista de clientes a un USB
[INTEGRIDAD      ] Cambian el número de cuenta en un albarán
[DISPONIBILIDAD  ] Un ataque DDoS satura el servidor web
```

> Usamos `Enum` en vez de cadenas sueltas: así `mypy` **impide** escribir `Pilar.CONFIDENCIALIDA` mal por error. Es una técnica profesional habitual.

!!! reto "Reto rápido 1"
    Un ransomware que además **exfiltra** los datos antes de cifrarlos (doble extorsión, muy habitual en 2025-2026) rompe dos pilares a la vez. ¿Cuáles? Añádelo a `INCIDENTES` con los dos.

### 1.2 Amenaza, vulnerabilidad y riesgo

- **Amenaza:** lo que puede pasar (un incendio, un atacante). Está fuera de tu control.
- **Vulnerabilidad:** la debilidad que lo permite (un servidor sin actualizar). Sí depende de ti.
- **Riesgo:** la combinación de ambos con su impacto. Es lo que se gestiona (a fondo en la UD4).

```mermaid
flowchart LR
    Am["Amenaza<br/>(atacante, incendio…)"] -->|explota| Vu["Vulnerabilidad<br/>(servidor sin parchear)"]
    Vu -->|produce| Ri["Riesgo<br/>= probabilidad × impacto"]
    Ri -->|si se materializa| Inc["Incidente"]
```

```python title="riesgo_simple.py"
def riesgo(probabilidad: float, impacto: float) -> float:
    """probabilidad en [0,1]; impacto en una escala (p. ej. euros o 1-10)."""
    return round(probabilidad * impacto, 2)

# Un servidor sin parchear (vulnerabilidad) frente a un exploit conocido (amenaza)
print(riesgo(probabilidad=0.7, impacto=10))   # alto: la amenaza es muy probable
print(riesgo(probabilidad=0.05, impacto=10))  # bajo: la amenaza es rara
```

```text title="Salida"
7.0
0.5
```

---

## 2. Seguridad física, ambiental y lógica

No toda la seguridad es software: quien entra físicamente a la sala de servidores no necesita romper ningún cifrado.

| Tipo | Protege frente a | Ejemplos |
|---|---|---|
| **Física** | Acceso físico no autorizado | Control de acceso al CPD, cerraduras, cámaras |
| **Ambiental** | El entorno | SAI (batería), climatización, detección de incendios |
| **Lógica** | Usos indebidos del sistema | Contraseñas, permisos, cifrado, cortafuegos, copias |

```python title="clasificar_medida.py"
FISICA = {"camara", "cerradura", "armario", "torniquete", "biometria_entrada"}
AMBIENTAL = {"sai", "climatizacion", "incendios", "humedad", "generador"}

def clasifica(medida: str) -> str:
    if medida in FISICA:
        return "física"
    if medida in AMBIENTAL:
        return "ambiental"
    return "lógica"          # todo lo demás: contraseñas, cifrado, cortafuegos...

for m in ["camara", "sai", "cortafuegos", "cifrado", "mfa"]:
    print(f"{m:12} -> {clasifica(m)}")
```

```text title="Salida"
camara       -> física
sai          -> ambiental
cortafuegos  -> lógica
cifrado      -> lógica
mfa          -> lógica
```

### 2.1 Copias de seguridad: la última línea

La regla **3-2-1**: al menos **3** copias, en **2** soportes distintos, con **1** fuera del sitio. Y **la copia que nunca se ha restaurado no cuenta como copia**: hay que probar la restauración.

```python title="regla_321.py"
from dataclasses import dataclass

@dataclass
class Copia:
    soporte: str        # "disco_local", "nas", "cloud", "cinta"...
    ubicacion: str       # "sitio" o "externo"

def cumple_321(copias: list[Copia]) -> tuple[bool, list[str]]:
    fallos = []
    if len(copias) < 3:
        fallos.append(f"solo hay {len(copias)} copias, hacen falta 3")
    soportes = {c.soporte for c in copias}
    if len(soportes) < 2:
        fallos.append("todas las copias usan el mismo soporte")
    if not any(c.ubicacion == "externo" for c in copias):
        fallos.append("ninguna copia está fuera del sitio")
    return (not fallos, fallos)

copias = [Copia("disco_local", "sitio"), Copia("nas", "sitio")]
print(cumple_321(copias))
```

```text title="Salida"
(False, ['solo hay 2 copias, hacen falta 3', 'ninguna copia está fuera del sitio'])
```

!!! reto "Reto rápido 2"
    Un empleado se lleva un USB con la copia los viernes (soporte: `"usb"`, ubicación: `"externo"`). Añádelo a la lista de arriba junto con una copia en `"cloud"`. ¿Ahora `cumple_321` da `True`?

---

## 3. Python como herramienta de seguridad

Python es tu herramienta durante todo el módulo. Monta el entorno una vez:

```bash title="Preparar el entorno"
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\Activate.ps1
pip install pytest mypy cryptography
```

Escribimos **Python tipado**: las anotaciones documentan y permiten que `mypy` cace errores sin ejecutar nada.

```python title="Tu primera huella digital"
import hashlib

def hash_de_texto(texto: str) -> str:      # (1)!
    """Devuelve el hash SHA-256 de un texto, en hexadecimal."""
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()   # (2)!

print(hash_de_texto("hola"))                # (3)!
print(hash_de_texto("hola"))                # (4)!
```

1.  Las **anotaciones de tipo** (`str -> str`) documentan y permiten que `mypy` detecte errores sin ejecutar.
2.  `.encode("utf-8")` convierte el texto en **bytes**, que es lo que acepta `hashlib`. Olvidarlo es el error clásico.
3.  Imprime `b221d9db…`: 64 caracteres hexadecimales (256 bits).
4.  El mismo texto da **siempre** el mismo hash — lo comprobamos llamando dos veces.

```text title="Salida"
b221d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79
b221d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79
```

!!! warning "Atención"
    Muchas funciones devuelven **texto**; para hashear hay que pasar a **bytes** con `.encode()`. Si ves `TypeError: Strings must be encoded before hashing`, es justo esto.

---

## 4. Criptografía I — funciones hash e integridad

Una **función hash** transforma cualquier dato en una huella de longitud fija.

| Propiedad | Qué significa |
|---|---|
| **Determinista** | El mismo dato da siempre el mismo hash |
| **Efecto avalancha** | Cambiar un bit cambia por completo la salida |
| **Unidireccional** | No se puede volver del hash al dato |
| **Resistente a colisiones** | Es inviable encontrar dos datos con el mismo hash |

```mermaid
flowchart LR
    D1["'seguridad'"] --> F["SHA-256"]
    D2["'Seguridad'"] --> F
    F --> H1["1ea9f394… (64 hex)"]
    F --> H2["b64167f5… (64 hex)"]
    H1 -.->|"57 de 64 caracteres distintos"| H2
```

### 4.1 Efecto avalancha, medido con código

```python title="avalancha.py"
import hashlib

def h(t: str) -> str:
    return hashlib.sha256(t.encode()).hexdigest()

def avalancha(a: str, b: str) -> int:
    ha, hb = h(a), h(b)
    return sum(1 for x, y in zip(ha, hb) if x != y)

a, b = "seguridad", "Seguridad"     # solo cambia una letra a mayúscula
print(h(a))
print(h(b))
print(f"Cambian {avalancha(a, b)} de 64 caracteres del hash")
```

```text title="Salida"
1ea9f394f510e2beb43cb0b317258b09bce9f4fccef69407360483690ac9b746
b64167f58e1cf0c322747fbe1a7361084a004ffb5c145fd64e5413ef11215965
Cambian 57 de 64 caracteres del hash
```

> Un cambio mínimo en la entrada altera casi todo el hash: por eso sirve para detectar la más pequeña manipulación.

### 4.2 Elegir el algoritmo (no todos valen)

```python title="comparar_algoritmos.py"
import hashlib

dato = b"documento importante"
for alg in ("md5", "sha1", "sha256", "sha3_256", "blake2b"):
    d = hashlib.new(alg, dato).hexdigest()
    print(f"{alg:9} {len(d)*4:4} bits   {d[:24]}...")
```

```text title="Salida"
md5        128 bits   73943af0696212b0ebfb60cf...
sha1       160 bits   3d8dd0ba48b54b431502c4f6...
sha256     256 bits   dd1cd769ac316412f9a0669e...
sha3_256   256 bits   ce5c2e89bddab0174ba19299...
blake2b    512 bits   e29f58fbe35b5357d889089c...
```

| Algoritmo | Estado | Uso recomendado |
|---|---|---|
| MD5 / SHA-1 | **Rotos** | Nunca para integridad seria |
| **SHA-256** | Vigente, estándar de facto | Integridad, firma, certificados TLS |
| **SHA-3 / BLAKE2** | Vigente, más modernos | Alternativas cuando se busca velocidad o margen extra |

### 4.3 Hash de un fichero grande (por bloques) y comparación segura

```python title="hash_fichero.py"
import hashlib, hmac
from pathlib import Path

def hash_fichero(ruta: Path, algoritmo: str = "sha256") -> str:
    """Hashea leyendo por bloques: funciona igual de bien con 1 KB que con 10 GB."""
    h = hashlib.new(algoritmo)
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(8192), b""):   # 8 KiB por lectura
            h.update(bloque)
    return h.hexdigest()

def integro(esperado: str, actual: str) -> bool:
    """Comparación en tiempo constante: no filtra información por temporización."""
    return hmac.compare_digest(esperado, actual)
```

!!! analogia "Analogía"
    El hash es el **número de precinto** de una caja de pruebas: no dice qué hay dentro, pero si el precinto coincide, nadie la ha abierto.

!!! warning "Hash ≠ cifrado"
    El hash **no se deshace**: no sirve para guardar algo que luego haya que recuperar, sino para **comprobar** que no ha cambiado. Para contraseñas se usa hash **con sal** y funciones lentas (bcrypt, Argon2) — lo verás en la UD4.

!!! reto "Reto rápido 3"
    Ejecuta `avalancha("1234", "1235")`. ¿Cambia también casi todo el hash aunque solo varíe un dígito? ¿Y `avalancha("1234", "1234 ")` (con un espacio al final)?

---

## 5. Criptografía II — cifrado simétrico y asimétrico

Cifrar es transformar un mensaje para que solo lo lea quien tenga la clave.

| | **Simétrico** | **Asimétrico** |
|---|---|---|
| Claves | Una sola, compartida | Par: pública + privada |
| Algoritmos típicos | AES, ChaCha20 (Fernet los usa por debajo) | RSA, curvas elípticas (ECC) |
| Ventaja | Muy rápido | No hay que compartir un secreto |
| Problema | ¿Cómo comparto la clave con seguridad? | Lento para grandes volúmenes |

### 5.1 Simétrico de verdad: Fernet (AES) con `cryptography`

```python title="simetrico_fernet.py"
from cryptography.fernet import Fernet, InvalidToken

clave = Fernet.generate_key()          # ⚠️ guárdala en secreto: cifra y descifra por igual
f = Fernet(clave)

token = f.encrypt(b"numero de cuenta: ES12 3456 7890")
print("Cifrado :", token[:50], b"...")
print("Descifrado:", f.decrypt(token))

# ¿Qué pasa si alguien manipula el mensaje cifrado?
try:
    manipulado = token[:-5] + b"XXXXX"
    f.decrypt(manipulado)
except InvalidToken:
    print("Detectado: el token manipulado NO se puede descifrar")
```

```text title="Salida"
Cifrado : b'gAAAAABo3k9f...' ...
Descifrado: b'numero de cuenta: ES12 3456 7890'
Detectado: el token manipulado NO se puede descifrar
```

> Fernet no solo cifra: también **autentica** el mensaje. Si alguien lo toca, `decrypt` lanza `InvalidToken` en vez de devolver basura silenciosamente. Es cifrado autenticado (AEAD), el estándar profesional.

### 5.2 Asimétrico: RSA (candado público, llave privada)

```python title="asimetrico_rsa.py"
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Genera el par de claves (esto lo hace Ana, una sola vez)
privada_ana = rsa.generate_private_key(public_exponent=65537, key_size=2048)
publica_ana = privada_ana.public_key()

oaep = padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)

# Cualquiera (tú) cifra con la clave PÚBLICA de Ana
cifrado = publica_ana.encrypt(b"clave de sesion: 7f3a9c", oaep)
print("Cifrado (bytes):", cifrado[:20], "...")

# Solo Ana, con su clave PRIVADA, puede descifrarlo
print("Descifrado:", privada_ana.decrypt(cifrado, oaep))
```

```text title="Salida"
Cifrado (bytes): b'\x8f\x3a\x1c...' ...
Descifrado: b'clave de sesion: 7f3a9c'
```

```mermaid
flowchart LR
    M["Mensaje"] -->|"se cifra con<br/>la pública de Ana"| C["🔒 Cifrado"]
    C -->|"se descifra con<br/>la privada de Ana"| M2["Mensaje"]
    style C fill:#7c3aed,color:#fff
```

!!! analogia "Analogía"
    La clave **pública** es un candado abierto que repartes a todo el mundo; la **privada**, la única llave que lo abre y que guardas tú. En la práctica se combinan (**cifrado híbrido**): el mensaje se cifra con una clave simétrica rápida, y esa clave se cifra con RSA. Así funciona HTTPS.

!!! reto "Reto rápido 4"
    Quieres enviar un fichero secreto a una compañera. ¿Con qué clave lo cifras: tu pública, tu privada, la suya pública o la suya privada? ¿Y si además quieres demostrar que lo enviaste tú?

---

## 6. Criptografía III — firma electrónica y certificados

La **firma** invierte el uso del par de claves para garantizar **autenticidad, integridad y no repudio**: se firma con la **privada** y cualquiera verifica con la **pública**.

```mermaid
sequenceDiagram
    participant A as Autor (clave privada)
    participant D as Documento
    participant V as Verificador (clave pública)
    A->>D: calcula hash(documento)
    A->>A: cifra el hash con su clave privada
    A->>V: envía documento + firma
    V->>D: calcula hash(documento) de nuevo
    V->>V: descifra la firma con la clave pública
    V->>V: compara los dos hashes
    Note over V: ¿coinciden? → auténtico e íntegro
```

```python title="firma_rsa.py"
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
publica = privada.public_key()
pss = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)

documento = b"Transferir 100 EUR a la cuenta ES12-555"
firma = privada.sign(documento, pss, hashes.SHA256())

def verifica(doc: bytes, firma: bytes) -> bool:
    try:
        publica.verify(firma, doc, pss, hashes.SHA256())
        return True
    except InvalidSignature:
        return False

print("Documento original :", verifica(documento, firma))
print("Documento alterado :", verifica(b"Transferir 999 EUR a la ES12-555", firma))
```

```text title="Salida"
Documento original : True
Documento alterado : False
```

> Cambiar **un solo carácter** del documento rompe la verificación: integridad y autenticidad a la vez, en una sola operación.

### 6.1 Firmar un fichero real, no solo una cadena en memoria

En la práctica no firmas literales de Python: firmas **ficheros** (un informe, un instalador, un contrato en PDF). La firma se guarda aparte, como un fichero `.sig`, y se distribuye junto al original.

```python title="firma_de_fichero.py"
from pathlib import Path

# Un informe real en disco (reutiliza privada/pss/verifica del ejemplo anterior)
Path("informe.txt").write_text("Informe trimestral: cifras confidenciales del cliente.")

# Se firma el CONTENIDO en bytes del fichero, no una cadena en memoria
contenido = Path("informe.txt").read_bytes()
firma_fichero = privada.sign(contenido, pss, hashes.SHA256())
Path("informe.txt.sig").write_bytes(firma_fichero)
print(f"Firma guardada en informe.txt.sig ({len(firma_fichero)} bytes)")

# La verificación se hace RELEYENDO ambos ficheros del disco — así ocurre en la vida real
contenido_releido = Path("informe.txt").read_bytes()
firma_releida = Path("informe.txt.sig").read_bytes()
print("Verificación tras releer del disco:", verifica(contenido_releido, firma_releida))
```

```text title="Salida"
Firma guardada en informe.txt.sig (256 bytes)
Verificación tras releer del disco: True
```

> 256 bytes es justo el tamaño de una firma RSA de 2048 bits (2048 ÷ 8), **siempre**, sin importar si el fichero firmado pesa 10 bytes o 10 GB — la firma es del hash del documento, no del documento entero.

### 6.2 Certificados digitales: generar uno de verdad

Un **certificado X.509** vincula una clave pública con una identidad. En producción lo firma una **CA** (Autoridad de Certificación); para practicar, generamos uno **autofirmado**:

```python title="certificado_x509.py"
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import datetime

clave = rsa.generate_private_key(public_exponent=65537, key_size=2048)
nombre = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "cmo314.local")])
ahora = datetime.datetime.now(datetime.timezone.utc)

certificado = (
    x509.CertificateBuilder()
    .subject_name(nombre)
    .issuer_name(nombre)                         # autofirmado: emisor = sujeto
    .public_key(clave.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(ahora)
    .not_valid_after(ahora + datetime.timedelta(days=365))
    .sign(clave, hashes.SHA256())
)

print("Sujeto      :", certificado.subject.rfc4514_string())
print("Emisor      :", certificado.issuer.rfc4514_string())
print("Válido hasta:", certificado.not_valid_after_utc.date())
print("Autofirmado :", certificado.subject == certificado.issuer)

pem = certificado.public_bytes(serialization.Encoding.PEM)
print(pem.decode().splitlines()[0])
```

```text title="Salida"
Sujeto      : CN=cmo314.local
Emisor      : CN=cmo314.local
Válido hasta: 2027-09-14
Autofirmado : True
-----BEGIN CERTIFICATE-----
```

Un certificado no vive en una variable: se **guarda como fichero `.pem`** y así es como lo lee un servidor web o un navegador.

```python title="certificado_a_fichero.py"
from pathlib import Path

# Los certificados se distribuyen como ficheros .pem, no en memoria
Path("cert.pem").write_bytes(pem)
print("Certificado guardado en cert.pem")

# Comprobación real: lo recargamos desde el disco, como haría un servidor web
recargado = x509.load_pem_x509_certificate(Path("cert.pem").read_bytes())
print("Mismo sujeto tras recargar del disco:", recargado.subject == certificado.subject)
print("Tamaño del fichero:", Path("cert.pem").stat().st_size, "bytes")
```

```text title="Salida"
Certificado guardado en cert.pem
Mismo sujeto tras recargar del disco: True
Tamaño del fichero: 1005 bytes
```

| Concepto | Qué es |
|---|---|
| **CA (Autoridad de Certificación)** | Entidad de confianza que firma certificados ajenos |
| **Certificado autofirmado** | El emisor y el sujeto son el mismo — vale para pruebas, **no** para producción pública |
| **PKI** | Toda la infraestructura: CAs, certificados, revocación, cadenas de confianza |

!!! reto "Reto rápido 5"
    Si tu navegador visita una web con un certificado **autofirmado**, avisa de "conexión no segura". ¿Por qué, si el cifrado funciona igual de bien?

---

## 7. Análisis forense digital

Investiga un incidente para responder **qué pasó, cómo, cuándo y con qué alcance**, preservando las evidencias para que tengan validez legal.

```mermaid
flowchart LR
    A["1 · Identificación<br/>¿qué ha pasado?"] --> B["2 · Adquisición<br/>copia bit a bit"]
    B --> C["3 · Análisis<br/>sobre la copia"]
    C --> D["4 · Documentación<br/>qué se hizo y cuándo"]
    D --> E["5 · Presentación<br/>informe pericial"]
```

### 7.1 Cadena de custodia, con código

Cada evidencia debe demostrar que **no se ha alterado** desde su recogida: se trabaja sobre una **copia**, se calcula el **hash** del original y de la copia (deben coincidir), y se registra quién la tuvo y cuándo.

```python title="cadena_custodia.py"
import hmac
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class RegistroCustodia:
    responsable: str
    fecha: datetime = field(default_factory=datetime.now)
    accion: str = "acceso"

def verifica_integridad(hash_original: str, hash_copia: str) -> str:
    return "ÍNTEGRA" if hmac.compare_digest(hash_original, hash_copia) else "⚠️ ALTERADA"

registro = [
    RegistroCustodia("Agente López", accion="adquisición"),
    RegistroCustodia("Perito García", accion="análisis"),
]
for r in registro:
    print(f"{r.fecha:%Y-%m-%d %H:%M} · {r.responsable} · {r.accion}")

print(verifica_integridad("abc123", "abc123"))   # ÍNTEGRA
print(verifica_integridad("abc123", "abc999"))   # ⚠️ ALTERADA
```

!!! analogia "Analogía"
    El hash de la evidencia es su **precinto digital**. Por eso se calcula **antes** de tocar nada: si al terminar sigue igual, has demostrado que no la manipulaste.

!!! reto "Reto rápido 6"
    ¿Por qué el forense calcula el hash **antes** de empezar a analizar y no después? ¿Qué pasaría con una prueba en un juicio si no lo hiciera?

---

## 8. Errores frecuentes (ten esto a mano)

| Error | Causa | Solución |
|---|---|---|
| `Strings must be encoded before hashing` | Pasar `str` a `hashlib` | `.encode("utf-8")` primero |
| Hashes que "no coinciden" | Espacios, mayúsculas o saltos de línea | Normaliza antes de comparar |
| Comparar hashes/secretos con `==` | Filtra información por tiempos | `hmac.compare_digest(a, b)` |
| Fichero grande lentísimo | Leerlo entero en memoria | Leer por bloques con `update()` |
| Usar MD5 para integridad | Algoritmo roto (colisiones conocidas) | SHA-256 o BLAKE2 |
| `InvalidSignature` inesperado | Verificar con datos distintos a los firmados | Comprueba que pasas el **mismo** `documento` |

---

## 9. Actividades: de lo más sencillo a preguntas tipo examen

> Una única escalera, sin saltos: empieza por el 🟢 1 y no mires la solución hasta intentarlo. Al final tienes preguntas del mismo estilo que el examen. Librerías reales: `hashlib`, `hmac`, `secrets`, `pathlib`, `re`, `cryptography`.

**1 · 🟢 Verificar una descarga** — acabas de descargar un fichero y la web publica su SHA-256. `descarga_integra(contenido: str, hash_publicado: str) -> bool`: ¿coincide de verdad?
<details class="sol"><summary>Solución</summary>

```python
import hashlib, hmac
def descarga_integra(contenido: str, hash_publicado: str) -> bool:
    hash_real = hashlib.sha256(contenido.encode("utf-8")).hexdigest()
    return hmac.compare_digest(hash_real, hash_publicado.strip().lower())
```
</details>

**2 · 🟢 ¿Ha cambiado el fichero?** — guardaste el hash de un `config.ini` la semana pasada. `ha_cambiado(hash_guardado: str, contenido_actual: str) -> bool`: ¿es distinto ahora? (este es, en miniatura, exactamente lo que hace `auditar()` en el reto de esta unidad).
<details class="sol"><summary>Solución</summary>

```python
import hashlib, hmac
def ha_cambiado(hash_guardado: str, contenido_actual: str) -> bool:
    hash_actual = hashlib.sha256(contenido_actual.encode("utf-8")).hexdigest()
    return not hmac.compare_digest(hash_actual, hash_guardado.strip().lower())
```
</details>

**3 · 🟢 Clasificar incidente** — `pilar(x)` para `"filtracion"/"alteracion"/"caida"` → `"C"`/`"I"`/`"D"`.
<details class="sol"><summary>Solución</summary>

```python
def pilar(x: str) -> str:
    return {"filtracion": "C", "alteracion": "I", "caida": "D"}.get(x, "?")
```
</details>

**4 · 🟢 ¿Formato de hash válido?** — `es_sha256(cadena: str) -> bool` con una expresión regular (64 hex).
<details class="sol"><summary>Solución</summary>

```python
import re
def es_sha256(cadena: str) -> bool:
    return bool(re.fullmatch(r"[0-9a-f]{64}", cadena.strip().lower()))
```
</details>

**5 · 🟡 Hash de bytes por bloques** — `hash_bloques(datos: bytes, n: int = 1024) -> str`.
<details class="sol"><summary>Solución</summary>

```python
import hashlib
def hash_bloques(datos: bytes, n: int = 1024) -> str:
    h = hashlib.sha256()
    for i in range(0, len(datos), n):
        h.update(datos[i:i + n])
    return h.hexdigest()
```
</details>

**6 · 🟡 Contar cambios (avalancha)** — `avalancha(a: str, b: str) -> int`: caracteres hex distintos entre sus SHA-256.
<details class="sol"><summary>Solución</summary>

```python
import hashlib
def avalancha(a: str, b: str) -> int:
    ha = hashlib.sha256(a.encode()).hexdigest()
    hb = hashlib.sha256(b.encode()).hexdigest()
    return sum(1 for x, y in zip(ha, hb) if x != y)
```
</details>

**7 · 🟡 Sal aleatoria** — `con_sal(pwd: str) -> tuple[str, str]` con `secrets` (no `random`).
<details class="sol"><summary>Solución</summary>

```python
import hashlib, secrets
def con_sal(pwd: str) -> tuple[str, str]:
    sal = secrets.token_hex(16)
    return sal, hashlib.sha256((sal + pwd).encode()).hexdigest()
```
</details>

**8 · 🟡 Detectar el algoritmo por longitud** — `adivina(hash_hex: str) -> str`: `"md5"` (32), `"sha1"` (40), `"sha256"` (64) o `"desconocido"`.
<details class="sol"><summary>Solución</summary>

```python
def adivina(hash_hex: str) -> str:
    return {32: "md5", 40: "sha1", 64: "sha256"}.get(len(hash_hex.strip()), "desconocido")
```
</details>

**9 · 🟠 Manifiesto: ficheros alterados** — `alterados(esperados, actuales) -> list[str]`.
<details class="sol"><summary>Solución</summary>

```python
def alterados(esperados: dict[str, str], actuales: dict[str, str]) -> list[str]:
    return [f for f, h in esperados.items() if actuales.get(f) != h]
```
</details>

**10 · 🟠 Auditoría completa** — `audita(man, ahora) -> dict[str,str]` con estados `OK`/`MODIFICADO`/`NUEVO`/`AUSENTE`.
<details class="sol"><summary>Solución</summary>

```python
def audita(man: dict[str, str], ahora: dict[str, str]) -> dict[str, str]:
    r: dict[str, str] = {}
    for f, h in man.items():
        r[f] = "AUSENTE" if f not in ahora else ("OK" if ahora[f] == h else "MODIFICADO")
    for f in ahora:
        if f not in man:
            r[f] = "NUEVO"
    return r
```
</details>

**11 · 🟠 Detectar ficheros duplicados** — `duplicados(archivos: dict[str,str]) -> dict[str, list[str]]`: agrupa nombres que comparten el mismo hash.
<details class="sol"><summary>Solución</summary>

```python
from collections import defaultdict
def duplicados(archivos: dict[str, str]) -> dict[str, list[str]]:
    por_hash: dict[str, list[str]] = defaultdict(list)
    for nombre, h in archivos.items():
        por_hash[h].append(nombre)
    return {h: n for h, n in por_hash.items() if len(n) > 1}
```
</details>

**12 · 🔴 Autenticar un mensaje (HMAC)** — `firma(clave, msg) -> str` y `valida(clave, msg, f) -> bool`. Así se firman webhooks y APIs reales.
<details class="sol"><summary>Solución</summary>

```python
import hmac, hashlib
def firma(clave: str, msg: str) -> str:
    return hmac.new(clave.encode(), msg.encode(), hashlib.sha256).hexdigest()
def valida(clave: str, msg: str, f: str) -> bool:
    return hmac.compare_digest(firma(clave, msg), f)
```
</details>

**13 · 🔴 Cadena de hashes (mini-blockchain)** — `cadena(bloques: list[str]) -> list[str]`: cada hash depende del anterior; `cadena_valida(bloques, hashes) -> bool` detecta si algo se alteró.
<details class="sol"><summary>Solución</summary>

```python
import hashlib
def cadena(bloques: list[str]) -> list[str]:
    hashes, anterior = [], "0" * 64
    for b in bloques:
        h = hashlib.sha256((anterior + b).encode()).hexdigest()
        hashes.append(h)
        anterior = h
    return hashes

def cadena_valida(bloques: list[str], hashes: list[str]) -> bool:
    return cadena(bloques) == hashes
```
</details>

**14 · 🔴 Firma RSA con `cryptography`** — dados `privada`/`publica`, `firma_rsa(privada, doc: bytes) -> bytes` y `verifica_rsa(publica, doc, firma) -> bool`.
<details class="sol"><summary>Solución</summary>

```python
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
_PSS = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)

def firma_rsa(privada, doc: bytes) -> bytes:
    return privada.sign(doc, _PSS, hashes.SHA256())

def verifica_rsa(publica, doc: bytes, firma: bytes) -> bool:
    try:
        publica.verify(firma, doc, _PSS, hashes.SHA256()); return True
    except InvalidSignature:
        return False
```
</details>

**15 · 🔴 ¿Cuánto le queda al certificado?** — `dias_restantes(fecha_expiracion: datetime) -> int`, usando `datetime.now(timezone.utc)`.
<details class="sol"><summary>Solución</summary>

```python
from datetime import datetime, timezone

def dias_restantes(fecha_expiracion: datetime) -> int:
    return (fecha_expiracion - datetime.now(timezone.utc)).days
```
</details>

**16 · 🔴 Manifiesto en dos formatos** — `a_texto(man: dict[str,str]) -> str` en formato `sha256sum` (`hash  nombre` por línea) y `de_texto(s: str) -> dict[str,str]` que lo lee de vuelta.
<details class="sol"><summary>Solución</summary>

```python
def a_texto(man: dict[str, str]) -> str:
    return "\n".join(f"{h}  {n}" for n, h in man.items())

def de_texto(s: str) -> dict[str, str]:
    m: dict[str, str] = {}
    for ln in s.splitlines():
        if ln.strip():
            h, _, n = ln.partition("  ")
            m[n.strip()] = h.strip().lower()
    return m
```
</details>

---

## 10. Reto resuelto, paso a paso — Verificador de integridad profesional

Te acaban de contratar como técnico junior en una consultora de ciberseguridad. Tu primer encargo: **una herramienta de línea de comandos** que genere un manifiesto de una carpeta y audite si algo cambió — el mismo principio que `sha256sum --check`, `debsums` o un HIDS como **AIDE**/**Tripwire**. La construimos contigo, de principio a fin.

```mermaid
flowchart LR
    G["generar"] -->|escribe| M["MANIFEST.json<br/>ruta → hash"]
    M -->|más tarde| Au["auditar"]
    Au -->|compara con| Fs["ficheros actuales"]
    Fs --> R["OK / MODIFICADO<br/>NUEVO / AUSENTE"]
```

**Paso 1 — Hash de un fichero.** La pieza más pequeña: hashear leyendo por bloques, para que funcione igual con 1 KB que con 10 GB.

```python title="verificador.py"
import hashlib
from pathlib import Path

def hash_fichero(ruta: Path, algoritmo: str = "sha256") -> str:
    h = hashlib.new(algoritmo)
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(8192), b""):
            h.update(bloque)
    return h.hexdigest()
```

**Paso 2 — Manifiesto de una carpeta entera.** Recorremos con `pathlib.rglob` y hasheamos cada fichero, saltando el propio manifiesto para no auto-referenciarnos:

```python title="verificador.py (continúa)"
def generar_manifiesto(carpeta: Path, algoritmo: str = "sha256") -> dict[str, str]:
    manifiesto: dict[str, str] = {}
    for ruta in sorted(carpeta.rglob("*")):
        if ruta.is_file() and ruta.name != "MANIFEST.json":
            manifiesto[str(ruta.relative_to(carpeta))] = hash_fichero(ruta, algoritmo)
    return manifiesto
```

**Paso 3 — Persistir en JSON.** Un manifiesto real se guarda estructurado, no como texto suelto: así es fácil de extender (algoritmo, fecha…).

```python title="verificador.py (continúa)"
import json
from datetime import datetime, timezone

def guardar(manifiesto: dict[str, str], destino: Path, algoritmo: str) -> None:
    datos = {"generado": datetime.now(timezone.utc).isoformat(timespec="seconds"),
             "algoritmo": algoritmo, "ficheros": manifiesto}
    destino.write_text(json.dumps(datos, indent=2, ensure_ascii=False), encoding="utf-8")

def cargar(origen: Path) -> dict[str, str]:
    return dict(json.loads(origen.read_text(encoding="utf-8"))["ficheros"])
```

**Paso 4 — Auditar.** El corazón de la herramienta: comparar lo guardado con lo actual, en tiempo constante.

```python title="verificador.py (continúa)"
import hmac

def auditar(previo: dict[str, str], actual: dict[str, str]) -> dict[str, str]:
    resultado: dict[str, str] = {}
    for nombre, h in previo.items():
        if nombre not in actual:
            resultado[nombre] = "AUSENTE"
        elif hmac.compare_digest(h, actual[nombre]):
            resultado[nombre] = "OK"
        else:
            resultado[nombre] = "MODIFICADO"
    for nombre in actual:
        if nombre not in previo:
            resultado[nombre] = "NUEVO"
    return resultado
```

**Paso 5 — CLI profesional con `argparse`.** Nada de leer `sys.argv` a mano: `argparse` da ayuda automática (`-h`), validación de opciones y aspecto de herramienta real.

```python title="verificador.py (continúa)"
import argparse

def main() -> None:
    ap = argparse.ArgumentParser(
        prog="verificador",
        description="Genera y audita un manifiesto de integridad de una carpeta.")
    ap.add_argument("accion", choices=["generar", "auditar"])
    ap.add_argument("carpeta", type=Path, help="carpeta a proteger")
    ap.add_argument("--algoritmo", default="sha256",
                    choices=["sha256", "sha3_256", "blake2b"])
    args = ap.parse_args()

    manifiesto_path = args.carpeta / "MANIFEST.json"
    if args.accion == "generar":
        guardar(generar_manifiesto(args.carpeta, args.algoritmo), manifiesto_path, args.algoritmo)
        print(f"Manifiesto creado en {manifiesto_path}")
    else:
        previo = cargar(manifiesto_path)
        actual = generar_manifiesto(args.carpeta, args.algoritmo)
        for nombre, estado in sorted(auditar(previo, actual).items()):
            print(f"[{estado:10}] {nombre}")

if __name__ == "__main__":
    main()
```

**Paso 6 — Pruébalo como cadena de custodia (Docker, sin `sudo`).**

```yaml title="docker-compose.yml"
services:
  demo:
    image: python:3.12-alpine
    volumes: ["./datos:/datos", "./verificador.py:/verificador.py"]
    working_dir: /datos
    command: >
      sh -c "echo 'binario de la app'     > app.bin;
             echo 'config=produccion'     > app.conf;
             python /verificador.py generar .;
             echo '--- alguien altera config.conf ---';
             echo 'config=HACKEADA'        > app.conf;
             echo 'malware.sh'             > intruso.sh;
             python /verificador.py auditar ."
```

```bash title="Ejecutar"
mkdir -p datos && docker compose run --rm demo
```

```text title="Salida esperada"
Manifiesto creado en datos/MANIFEST.json
--- alguien altera config.conf ---
[MODIFICADO] app.conf
[NUEVO     ] intruso.sh
[OK        ] app.bin
```

<details class="sol"><summary>📄 verificador.py completo (los 5 pasos juntos, para comparar)</summary>

```python
import argparse, hashlib, hmac, json
from pathlib import Path
from datetime import datetime, timezone

def hash_fichero(ruta: Path, algoritmo: str = "sha256") -> str:
    h = hashlib.new(algoritmo)
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(8192), b""):
            h.update(bloque)
    return h.hexdigest()

def generar_manifiesto(carpeta: Path, algoritmo: str = "sha256") -> dict[str, str]:
    m: dict[str, str] = {}
    for ruta in sorted(carpeta.rglob("*")):
        if ruta.is_file() and ruta.name != "MANIFEST.json":
            m[str(ruta.relative_to(carpeta))] = hash_fichero(ruta, algoritmo)
    return m

def guardar(manifiesto: dict[str, str], destino: Path, algoritmo: str) -> None:
    datos = {"generado": datetime.now(timezone.utc).isoformat(timespec="seconds"),
             "algoritmo": algoritmo, "ficheros": manifiesto}
    destino.write_text(json.dumps(datos, indent=2, ensure_ascii=False), encoding="utf-8")

def cargar(origen: Path) -> dict[str, str]:
    return dict(json.loads(origen.read_text(encoding="utf-8"))["ficheros"])

def auditar(previo: dict[str, str], actual: dict[str, str]) -> dict[str, str]:
    r: dict[str, str] = {}
    for n, h in previo.items():
        r[n] = "AUSENTE" if n not in actual else ("OK" if hmac.compare_digest(h, actual[n]) else "MODIFICADO")
    for n in actual:
        if n not in previo:
            r[n] = "NUEVO"
    return r

def main() -> None:
    ap = argparse.ArgumentParser(prog="verificador", description="Manifiesto de integridad")
    ap.add_argument("accion", choices=["generar", "auditar"])
    ap.add_argument("carpeta", type=Path)
    ap.add_argument("--algoritmo", default="sha256", choices=["sha256", "sha3_256", "blake2b"])
    args = ap.parse_args()
    ruta_man = args.carpeta / "MANIFEST.json"
    if args.accion == "generar":
        guardar(generar_manifiesto(args.carpeta, args.algoritmo), ruta_man, args.algoritmo)
        print(f"Manifiesto creado en {ruta_man}")
    else:
        previo = cargar(ruta_man)
        actual = generar_manifiesto(args.carpeta, args.algoritmo)
        for n, e in sorted(auditar(previo, actual).items()):
            print(f"[{e:10}] {n}")

if __name__ == "__main__":
    main()
```
</details>

---

## 11. Reto para ti (propuesto, sin solución)

### 🛡️ Centinela de integridad — un HIDS mínimo en Docker

Un **HIDS** (*Host Intrusion Detection System*) vigila que los ficheros de un sistema no cambien sin permiso. Constrúyelo **partiendo de tu `verificador.py`**.

```mermaid
flowchart TB
    subgraph "Contenedor: objetivo"
    F["Ficheros vigilados"]
    end
    subgraph "Contenedor: centinela (tu código)"
    Ge["1. genera manifiesto"] --> Bu["2. bucle cada 5s"]
    Bu --> Au["3. audita"]
    Au -->|cambio detectado| Lo["4. log con timestamp"]
    Au -->|sin cambios| Bu
    end
    F -.->|volumen compartido| Ge
    F -.->|volumen compartido| Au
```

**Objetivo.** Un contenedor "objetivo" tiene una carpeta con ficheros. Tu **centinela** (otro contenedor con tu Python) genera el manifiesto **una vez** y luego, **en bucle cada 5 segundos**, reaudita y **registra en un log** cualquier cambio con marca de tiempo, distinguiendo `MODIFICADO`, `NUEVO` y `AUSENTE`.

**Requisitos**

- `docker-compose.yml` con dos servicios que comparten un volumen: uno que va tocando ficheros (simula cambios con un `sh` que escribe de vez en cuando) y el **centinela** (tu programa).
- El centinela **no** reescribe el manifiesto tras detectar un cambio (si lo hiciera, no volvería a alertar de lo mismo).
- CLI con `argparse`: `python centinela.py <carpeta> --intervalo 5`.
- Log con formato `2026-05-01T10:00:05+00:00  [MODIFICADO] app.conf`.
- Código **tipado** (`mypy` limpio), reutilizando funciones de tu `verificador.py`.
- Nada de `sudo`: todo dentro de `docker compose up`.

**Criterios de aceptación**

1. Al arrancar, crea el manifiesto y no alerta de nada.
2. Cuando un fichero cambia, aparece **una sola** línea de alerta con su marca de tiempo (no se repite en cada vuelta del bucle).
3. Si se crea o se borra un fichero, lo marca como `NUEVO` o `AUSENTE`.
4. Se puede parar y volver a arrancar sin perder el manifiesto (persístelo en el volumen).

**Pistas** (no solución): reutiliza `generar_manifiesto`, `auditar`, `guardar` y `cargar` tal cual · para no repetir alertas, guarda en memoria el **último estado conocido** de cada fichero y compara antes de loguear · bucle `while True: ...; time.sleep(args.intervalo)` · para el log, `logging.basicConfig(filename=..., level=logging.INFO)`.

**Si te sobra tiempo:** añade un modo `--formato texto` que además escriba un `MANIFEST.sha256` estilo `sha256sum` · firma el `MANIFEST.json` con RSA (§6) para que nadie pueda falsificarlo sin que se note · investiga `Pillow` (`Image.open(ruta)._getexif()`) para extraer metadatos EXIF de una fotografía como evidencia forense.

> Entrega el `docker-compose.yml` y tu código. Esto es justo el tipo de reto que resolverás en el **test práctico**.

---

## Autoevaluación rápida (conceptos)

<details><summary>1. ¿Qué garantiza la <b>integridad</b>?</summary>Que la información no se altera sin autorización.</details>
<details><summary>2. ¿Se puede recuperar un dato a partir de su hash?</summary>No: la función hash es unidireccional.</details>
<details><summary>3. ¿Con qué clave cifras un mensaje para que solo lo lea Ana?</summary>Con la clave <b>pública</b> de Ana.</details>
<details><summary>4. ¿Por qué MD5 no sirve para integridad seria?</summary>Está roto: se pueden encontrar colisiones.</details>
<details><summary>5. ¿Por qué se trabaja sobre una copia en forense?</summary>Para no alterar el original y preservar la cadena de custodia.</details>

## Glosario

| Término | Definición |
|---|---|
| **C·I·D** | Confidencialidad, integridad y disponibilidad. |
| **Hash** | Huella de longitud fija de un dato; unidireccional y determinista. |
| **Efecto avalancha** | Un cambio mínimo altera casi todo el hash. |
| **HMAC** | Hash con clave secreta: autentica un mensaje, no solo lo hashea. |
| **Cifrado simétrico / asimétrico** | Una clave compartida / par pública-privada. |
| **Cifrado autenticado (AEAD)** | Cifrado que además detecta si el texto cifrado fue manipulado. |
| **Firma electrónica** | Hash cifrado con la clave privada; prueba autoría e integridad. |
| **Certificado / CA / PKI** | Vínculo clave-identidad / quien lo firma / la infraestructura completa. |
| **Cadena de custodia** | Garantía de que una evidencia no se ha alterado. |
| **HIDS** | Sistema que detecta cambios no autorizados en los ficheros de un host. |

## Cómo se evalúa esta unidad (RA1)

El instrumento principal es un **test práctico**: resuelves en Python un reto parecido al de esta unidad y se corrige **solo con su batería de tests** (queda abierto, como complemento, algún ejercicio práctico).

!!! reto "La nota, sin sorpresas"
    **Nota = (tests superados ÷ total) × 10.** Se aprueba con 5. Es la misma mecánica del reto de esta unidad, así que llegas entrenado.

El informe además te marca, **sin puntuar**, tres buenas prácticas: usar la técnica del RA (aquí, `hashlib`), pasar `mypy` y documentar el código.

---

## Simulacro de examen tipo test

> 17 preguntas de opción múltiple sobre **todo el código práctico** de la unidad — teoría, actividades y reto. Elige tu respuesta antes de abrir la solución.

**1.** Un ransomware moderno cifra los ficheros **y además** exfiltra los datos antes (doble extorsión). Según `clasificar_incidentes.py`, ¿qué pilar(es) rompe?

A) Solo Disponibilidad
B) Solo Confidencialidad
C) Disponibilidad y Confidencialidad
D) Integridad

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: C.</b> Cifrar rompe la disponibilidad (no se puede acceder a los datos); exfiltrarlos antes rompe además la confidencialidad (alguien no autorizado los tiene).</details>

**2.** ¿Qué devuelve `riesgo(probabilidad=0.2, impacto=8)` con la función de `riesgo_simple.py`?

A) `1.6`
B) `10.0`
C) `0.2`
D) `8.0`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: A.</b> <code>round(0.2 * 8, 2) = 1.6</code>.</details>

**3.** Según `clasifica()` de `clasificar_medida.py`, ¿qué devuelve `clasifica("generador")`?

A) `"física"`
B) `"ambiental"`
C) `"lógica"`
D) `"desconocido"`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> <code>"generador"</code> está en el conjunto <code>AMBIENTAL</code>.</details>

**4.** Tres copias, **todas** en `soporte="disco_local"`, dos en `"sitio"` y una en `"externo"`. ¿Qué devuelve `cumple_321`?

A) `(True, [])`
B) `(False, ['solo hay 3 copias, hacen falta 3'])`
C) `(False, ['todas las copias usan el mismo soporte'])`
D) `(False, ['ninguna copia está fuera del sitio'])`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: C.</b> Hay 3 copias (cumple) y sí hay una externa (cumple), pero las tres usan el <b>mismo</b> soporte — falla la regla de los "2 soportes distintos".</details>

**5.** ¿Qué relación hay entre las dos líneas que imprime `print(hash_de_texto("hola"))` ejecutado dos veces seguidas?

A) Son idénticas siempre
B) Son distintas cada vez que se ejecuta el programa
C) Solo coinciden si el ordenador no ha cambiado de hora
D) La segunda tiene el doble de caracteres

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: A.</b> El hash es <b>determinista</b>: el mismo texto siempre produce el mismo resultado.</details>

**6.** `avalancha("1234", "1235")` compara los SHA-256 de dos cadenas que difieren en un solo dígito. ¿Qué observas en el resultado?

A) Cambia solo 1 carácter del hash (el dígito que cambió)
B) Cambia 0 caracteres, son números parecidos
C) Cambia la mayoría de los 64 caracteres — efecto avalancha
D) El hash da error porque los textos son casi iguales

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: C.</b> Es el efecto avalancha: un cambio mínimo en la entrada altera casi toda la salida (en la práctica, más de 50 de los 64 caracteres).</details>

**7.** Según `comparar_algoritmos.py`, ¿cuántos bits produce `hashlib.new("sha256", ...).hexdigest()`?

A) 128
B) 160
C) 256
D) 512

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: C.</b> SHA-256 produce 256 bits (64 caracteres hexadecimales).</details>

**8.** ¿Por qué `hash_fichero()` lee el fichero en bloques de 8192 bytes en vez de cargarlo entero con `f.read()`?

A) Es un límite fijo de `hashlib` que no se puede evitar
B) Para que funcione igual de bien con ficheros enormes sin agotar la memoria
C) Para que el hash resultante sea más seguro
D) Es un requisito legal del RGPD

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> Leer por bloques mantiene el consumo de memoria constante, sin importar si el fichero pesa 1 KB o 10 GB.</details>

**9.** En `simetrico_fernet.py`, si manipulas los últimos bytes del token cifrado y luego llamas a `f.decrypt(...)`, ¿qué ocurre?

A) Devuelve el texto descifrado igualmente, aunque corrupto
B) Lanza `InvalidToken`
C) El programa se queda colgado sin excepción
D) Devuelve `None` silenciosamente

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> Fernet es cifrado autenticado: detecta la manipulación y rechaza explícitamente el token en vez de devolver datos corruptos.</details>

**10.** Quieres enviar un mensaje que **solo** Ana pueda leer, usando RSA asimétrico. ¿Con qué clave lo cifras?

A) Tu clave privada
B) Tu clave pública
C) La clave pública de Ana
D) La clave privada de Ana

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: C.</b> Se cifra con la clave <b>pública</b> del destinatario; solo su clave privada (que nadie más tiene) puede descifrarlo.</details>

**11.** Firmas un documento con `firma_rsa.py`. ¿Con qué clave firmas, y con cuál se verifica la firma?

A) Firmas con tu pública; se verifica con tu privada
B) Firmas con tu privada; se verifica con tu pública
C) Ambas operaciones usan tu clave privada
D) Ambas operaciones usan tu clave pública

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> Se firma con la clave privada del autor; cualquiera puede verificar con su clave pública, que es de dominio público.</details>

**12.** En `firma_de_fichero.py`, ¿cuántos bytes ocupa la firma guardada en `informe.txt.sig`?

A) Depende del tamaño de `informe.txt`
B) Siempre 256 bytes, porque la clave RSA es de 2048 bits (2048 ÷ 8)
C) 64 bytes, como un hash SHA-256
D) 1 byte por cada carácter del documento firmado

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> La firma RSA tiene un tamaño fijo determinado por el tamaño de la clave, no por el tamaño del documento — por eso pesa 256 bytes firmes un informe de 10 bytes o de 10 GB.</details>

**13.** ¿Por qué `certificado_a_fichero.py` guarda el certificado como `cert.pem` en vez de dejarlo solo en la variable `pem`?

A) Porque las variables de Python se borran cada pocos segundos
B) Porque un certificado se distribuye y se lee como fichero — así lo usa un servidor web real
C) Porque el formato `.pem` comprime los datos
D) No hay ninguna razón técnica, es solo estética

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> Un certificado tiene que poder leerse desde disco por un servidor, un navegador u otra herramienta — por eso se distribuye como fichero <code>.pem</code>, no como una variable en memoria.</details>

**14.** Un certificado X.509 tiene `certificado.subject == certificado.issuer`. ¿Qué tipo de certificado es?

A) Emitido por una CA reconocida
B) Autofirmado
C) Caducado
D) Revocado

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> Que el emisor y el sujeto coincidan significa que el propio certificado se firmó a sí mismo — nadie de confianza externo lo avaló.</details>

**15.** Ordena las fases del análisis forense digital tal como se ven en la unidad:

A) Análisis → Identificación → Adquisición → Documentación → Presentación
B) Identificación → Adquisición → Análisis → Documentación → Presentación
C) Adquisición → Identificación → Presentación → Análisis → Documentación
D) Presentación → Documentación → Análisis → Adquisición → Identificación

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> Primero se identifica el incidente, luego se adquiere una copia de la evidencia, se analiza esa copia, se documenta todo, y por último se presenta el informe.</details>

**16.** Con el manifiesto guardado `{"app.bin": "aaa", "app.conf": "bbb"}` y el estado actual `{"app.conf": "ccc", "extra.txt": "ddd"}`, ¿qué estado recibe `"app.bin"` al llamar a `auditar(previo, actual)`?

A) `"OK"`
B) `"MODIFICADO"`
C) `"AUSENTE"`
D) `"NUEVO"`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: C.</b> <code>"app.bin"</code> está en el manifiesto guardado (<code>previo</code>) pero ya no existe en el estado actual (<code>actual</code>) — por eso se marca <code>AUSENTE</code>.</details>

**17.** ¿Por qué el código de esta unidad usa `hmac.compare_digest(a, b)` en vez de `a == b` para comparar hashes o firmas?

A) Es más rápido de ejecutar
B) `compare_digest` tarda siempre el mismo tiempo, evitando filtrar información por temporización
C) `==` no funciona con cadenas de más de 32 caracteres
D) No hay diferencia real, es solo una cuestión de estilo

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> <code>==</code> se detiene en el primer carácter distinto, y ese tiempo de respuesta variable puede filtrar información a un atacante (ataque de temporización). <code>compare_digest</code> siempre tarda lo mismo.</details>
