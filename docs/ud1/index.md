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

El problema del cifrado simétrico es el reparto de la clave: si Ana y Luis están lejos, ¿cómo se pasan la clave sin que nadie la intercepte por el camino? El cifrado **asimétrico** lo resuelve con un truco: en vez de **una** clave, cada persona tiene **un par** de claves que funcionan juntas.

- La clave **pública**: se reparte a todo el mundo. **Solo sirve para cifrar.**
- La clave **privada**: se guarda en secreto, no se le da a nadie. **Es la única que descifra** lo que se cifró con su pública.

!!! analogia "La analogía del buzón"
    Imagina un buzón con una ranura. **Cualquiera** puede echar una carta por la ranura (cifrar con la clave pública), pero **solo** quien tiene la llave del buzón (la clave privada) puede abrirlo y leer las cartas. Repartir la "ranura" no es peligroso: con ella solo se puede meter, no sacar.

#### El mecanismo, paso a paso

Cada persona genera su par de claves **una sola vez** y publica su clave pública (en su web, en un servidor de claves, en su perfil…). La privada no sale nunca de su ordenador.

```mermaid
flowchart TB
    subgraph ANA["👩 Ana"]
      AP["🔑 privada de Ana<br/>(secreta)"]
      APub["📢 pública de Ana<br/>(repartida)"]
    end
    subgraph LUIS["👨 Luis"]
      LP["🔑 privada de Luis<br/>(secreta)"]
      LPub["📢 pública de Luis<br/>(repartida)"]
    end
    APub -.->|"Ana reparte su pública"| LUIS
    LPub -.->|"Luis reparte su pública"| ANA
```

Cuando **Ana quiere escribir a Luis**, usa la clave **pública de Luis** para cifrar. A partir de ahí, el mensaje solo se puede abrir con la **privada de Luis** — que solo Luis tiene:

```mermaid
flowchart LR
    M["✉️ Mensaje<br/>de Ana"] -->|"cifra con la<br/>PÚBLICA de Luis"| C["🔒 Cifrado"]
    C -->|"viaja por Internet"| C2["🔒 Cifrado"]
    C2 -->|"descifra con la<br/>PRIVADA de Luis"| M2["✉️ Mensaje<br/>que lee Luis"]
    style C fill:#dbeafe,color:#1e3a8a
    style C2 fill:#dbeafe,color:#1e3a8a
```

> La regla de oro: **se cifra con la clave pública del destinatario.** Fíjate en que la clave pública de *Ana* no interviene para nada cuando Ana **envía**: solo cuando alguien le escribe **a ella**.

#### En Python: Ana y Luis se escriben

Cada uno genera su par de claves. Para cifrar se usa un "relleno" llamado **OAEP** (lo explicamos justo después):

```python title="asimetrico_dos_usuarios.py"
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def nuevo_par():
    privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return privada, privada.public_key()

# Cada persona genera su par UNA vez. La privada no se comparte jamás.
privada_ana,  publica_ana  = nuevo_par()
privada_luis, publica_luis = nuevo_par()

OAEP = padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)

# Ana -> Luis: cifra con la PÚBLICA de LUIS
para_luis = publica_luis.encrypt(b"Hola Luis, el plan sigue en pie", OAEP)
print("Luis descifra:", privada_luis.decrypt(para_luis, OAEP).decode())

# Luis -> Ana: cifra con la PÚBLICA de ANA
para_ana = publica_ana.encrypt(b"Recibido Ana, alli estare", OAEP)
print("Ana descifra :", privada_ana.decrypt(para_ana, OAEP).decode())
```

```text title="Salida"
Luis descifra: Hola Luis, el plan sigue en pie
Ana descifra : Recibido Ana, alli estare
```

#### ¿Y si un espía intercepta el mensaje?

Aquí está la magia. Eva intercepta el mensaje cifrado que iba para Luis. Eva **tiene** la clave pública de Luis (es pública, la tiene todo el mundo)… pero eso no le sirve de nada: la pública **solo cifra, no descifra**. Y su propia clave privada tampoco abre un mensaje cifrado para Luis.

```mermaid
flowchart LR
    C["🔒 Mensaje cifrado<br/>para Luis"] --> Eva["🕵️ Eva lo intercepta"]
    Eva -->|"prueba con la<br/>pública de Luis"| X1["❌ la pública<br/>no descifra"]
    Eva -->|"prueba con su<br/>propia privada"| X2["❌ no es la<br/>privada de Luis"]
    style X1 fill:#fee2e2,color:#991b1b
    style X2 fill:#fee2e2,color:#991b1b
```

```python title="espia_fracasa.py"
# (continúa del ejemplo anterior: Eva ha interceptado 'para_luis')
privada_eva, publica_eva = nuevo_par()

# Eva tiene la clave PÚBLICA de Luis, pero una clave pública no tiene ni método para descifrar:
print("¿La pública puede descifrar?:", hasattr(publica_luis, "decrypt"))

# Eva intenta con la única clave privada que posee (la suya): falla
try:
    privada_eva.decrypt(para_luis, OAEP)
except ValueError:
    print("Eva NO puede leer el mensaje: no tiene la privada de Luis")
```

```text title="Salida"
¿La pública puede descifrar?: False
Eva NO puede leer el mensaje: no tiene la privada de Luis
```

> Por eso es seguro repartir la clave pública a cualquiera, incluso publicarla en Internet: con ella **solo** se puede cifrar hacia ti, nunca descifrar lo que va dirigido a ti.

#### ¿Qué es eso de OAEP? ¿Y PSS?

RSA "a secas" es inseguro: cifrar dos veces el mismo mensaje daría el mismo resultado, y eso filtra información. Para evitarlo se añade un **relleno** (*padding*) que mete aleatoriedad antes de aplicar RSA. Hay uno para cada tarea, y **no son intercambiables**:

| Relleno | ¿Para qué? | Dónde lo usas |
|---|---|---|
| **OAEP** | Para **cifrar** (ocultar un mensaje) | `encrypt` / `decrypt` (sección 5.2) |
| **PSS** | Para **firmar** (demostrar autoría) | `sign` / `verify` (sección 6) |

No hace falta que te sepas sus interioridades matemáticas. Lo que tienes que recordar para el examen: **OAEP cifra, PSS firma**, y ambos añaden aleatoriedad para que RSA sea seguro.

!!! warning "Lo lento no se cifra con RSA directamente"
    RSA es lento y solo cifra mensajes cortos (más pequeños que la clave). Por eso en la práctica se usa **cifrado híbrido**: se genera una clave simétrica rápida (Fernet/AES), con ella se cifra todo el mensaje, y **solo esa clave corta** se cifra con RSA. Es exactamente lo que hace tu navegador en cada conexión **HTTPS**.

!!! reto "Reto rápido 4"
    Quieres enviar un fichero secreto a una compañera. ¿Con qué clave lo cifras: tu pública, tu privada, la suya pública o la suya privada? ¿Y qué relleno usas, OAEP o PSS?

---

## 6. Criptografía III — firma electrónica y certificados

Cifrar sirve para **ocultar** un mensaje. Firmar sirve para lo contrario: **demostrar que un mensaje es tuyo y que nadie lo ha cambiado**, aunque el mensaje se lea a plena luz. Para ello se usa el par de claves **al revés** que al cifrar:

- Se **firma** con la clave **privada** (solo tú la tienes → solo tú puedes firmar en tu nombre).
- Se **verifica** con la clave **pública** (la tiene todo el mundo → cualquiera puede comprobar que fuiste tú).

Una firma digital da tres garantías a la vez: **autenticidad** (quién lo firmó), **integridad** (no se ha modificado) y **no repudio** (el firmante no puede negar que fue él).

```mermaid
flowchart LR
    D["📄 Documento"] -->|"Ana firma con su<br/>PRIVADA"| F["✍️ Firma"]
    D --> V{"Verificar con la<br/>PÚBLICA de Ana"}
    F --> V
    V -->|coinciden| OK["✅ auténtico<br/>e intacto"]
    V -->|no coinciden| NO["❌ falso o<br/>modificado"]
    style OK fill:#d1fae5,color:#065f46
    style NO fill:#fee2e2,color:#991b1b
```

Para firmar se usa el relleno **PSS** (recuerda de la sección 5.2: **PSS firma**, OAEP cifra). El ejemplo: Ana firma una autorización de pago; cualquiera comprueba que es suya.

```python title="firma_rsa.py"
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

privada_ana = rsa.generate_private_key(public_exponent=65537, key_size=2048)
publica_ana = privada_ana.public_key()
PSS = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)

mensaje = b"Yo, Ana, autorizo el pago de 100 euros"
firma = privada_ana.sign(mensaje, PSS, hashes.SHA256())    # firma con SU privada

def es_autentico(mensaje: bytes, firma: bytes) -> bool:
    try:
        publica_ana.verify(firma, mensaje, PSS, hashes.SHA256())   # verifica con la pública de Ana
        return True
    except InvalidSignature:
        return False

print("Mensaje original de Ana  :", es_autentico(mensaje, firma))
print("Mensaje con el importe cambiado:", es_autentico(b"Yo, Ana, autorizo el pago de 900 euros", firma))
```

```text title="Salida"
Mensaje original de Ana  : True
Mensaje con el importe cambiado: False
```

Cambiar **un solo carácter** (de `100` a `900`) rompe la verificación: integridad y autenticidad en una sola operación.

**¿Y si un impostor intenta hacerse pasar por Ana?** No puede: para firmar en nombre de Ana haría falta la clave **privada** de Ana, que solo ella tiene. Una firma hecha con cualquier otra clave no supera la verificación con la pública de Ana:

```python title="impostor.py"
# (continúa del ejemplo anterior)
privada_impostor = rsa.generate_private_key(public_exponent=65537, key_size=2048)
firma_falsa = privada_impostor.sign(mensaje, PSS, hashes.SHA256())   # firma con OTRA privada

print("Firma de un impostor:", es_autentico(mensaje, firma_falsa))
```

```text title="Salida"
Firma de un impostor: False
```

!!! tip "Cifrar y firmar son simétricos entre sí"
    Fíjate en el patrón: para **cifrar hacia alguien** usas su **pública** (y él descifra con su privada). Para **firmar** usas **tu privada** (y los demás verifican con tu pública). Lo privado es siempre tuyo y nunca sale de tu ordenador; lo público lo tiene todo el mundo.

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

El perito nunca trabaja sobre la evidencia original: podría estropearla y la prueba perdería validez en el juicio. El procedimiento es siempre el mismo:

1. **Antes de tocar nada**, se calcula el hash del original: es su **precinto digital**.
2. Se hace una **copia** y se trabaja siempre sobre ella.
3. Al terminar, se recalcula el hash de la copia: si coincide con el precinto, queda **demostrado** que nadie la alteró.

Y en paralelo se lleva la **cadena de custodia**: un registro de quién tuvo la prueba y cuándo.

Vamos a hacerlo de verdad sobre un fichero (aquí, un log que sería la evidencia):

```python title="cadena_custodia.py"
import hashlib, hmac, shutil
from pathlib import Path
from datetime import datetime

def sha256_fichero(ruta: str) -> str:
    return hashlib.sha256(Path(ruta).read_bytes()).hexdigest()

# La evidencia: un registro recogido del servidor del cliente
Path("evidencia.log").write_text("2026-05-01 10:03 acceso root desde 10.0.0.7\n")

# PASO 1 · Precinto: hash del original, ANTES de tocar nada
precinto = sha256_fichero("evidencia.log")
custodia = [(datetime(2026, 5, 1, 10, 30), "Agente López", "recoge la evidencia")]

# PASO 2 · Se trabaja SIEMPRE sobre una copia, nunca el original
shutil.copy("evidencia.log", "copia_trabajo.log")
custodia.append((datetime(2026, 5, 1, 11, 0), "Perito García", "crea copia de trabajo"))

# PASO 3 · Antes del juicio: ¿la copia sigue siendo idéntica al original?
hash_copia = sha256_fichero("copia_trabajo.log")
estado = "ÍNTEGRA" if hmac.compare_digest(precinto, hash_copia) else "ALTERADA"

print("Precinto del original:", precinto[:16], "...")
print("Hash de la copia     :", hash_copia[:16], "...")
print("La evidencia está     :", estado)
print("\nCadena de custodia:")
for fecha, quien, accion in custodia:
    print(f"  {fecha:%Y-%m-%d %H:%M} · {quien} · {accion}")
```

```text title="Salida"
Precinto del original: 4a65ab9cf9767bfd ...
Hash de la copia     : 4a65ab9cf9767bfd ...
La evidencia está     : ÍNTEGRA
Cadena de custodia:
  2026-05-01 10:30 · Agente López · recoge la evidencia
  2026-05-01 11:00 · Perito García · crea copia de trabajo
```

¿Y si alguien manipula la prueba por el camino? El hash cambia y se detecta al instante:

```python title="deteccion_manipulacion.py"
# (continúa del ejemplo anterior) alguien edita la copia para cambiar la IP del atacante
Path("copia_trabajo.log").write_text("2026-05-01 10:03 acceso root desde 1.2.3.4\n")

hash_tras_manipular = sha256_fichero("copia_trabajo.log")
print("¿Sigue íntegra?:", hmac.compare_digest(precinto, hash_tras_manipular))
```

```text title="Salida"
¿Sigue íntegra?: False
```

!!! analogia "Analogía"
    El hash de la evidencia es su **precinto digital**, como el de una caja de pruebas. Por eso se calcula **antes** de tocar nada: si al terminar sigue igual, has demostrado que no la manipulaste.

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

**15 · 🔴 Buzón asimétrico** — `cifrar_para(publica_destino, mensaje: bytes) -> bytes` y `descifrar(privada_propia, cifrado: bytes) -> bytes` con OAEP. Comprueba que un mensaje cifrado para Luis **solo** lo descifra Luis.
<details class="sol"><summary>Solución</summary>

```python
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
_OAEP = padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)

def cifrar_para(publica_destino, mensaje: bytes) -> bytes:
    return publica_destino.encrypt(mensaje, _OAEP)        # con la PÚBLICA del destinatario

def descifrar(privada_propia, cifrado: bytes) -> bytes:
    return privada_propia.decrypt(cifrado, _OAEP)         # con la PROPIA privada
```

Solo la privada que corresponde a la pública usada al cifrar puede descifrar; cualquier otra lanza `ValueError`.
</details>

**16 · 🔴 ¿Cuánto le queda al certificado?** — `dias_restantes(fecha_expiracion: datetime) -> int`, usando `datetime.now(timezone.utc)`.
<details class="sol"><summary>Solución</summary>

```python
from datetime import datetime, timezone

def dias_restantes(fecha_expiracion: datetime) -> int:
    return (fecha_expiracion - datetime.now(timezone.utc)).days
```
</details>

**17 · 🔴 Manifiesto en dos formatos** — `a_texto(man: dict[str,str]) -> str` en formato `sha256sum` (`hash  nombre` por línea) y `de_texto(s: str) -> dict[str,str]` que lo lee de vuelta.
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
| **OAEP / PSS** | Rellenos de RSA: OAEP para **cifrar**, PSS para **firmar**. |
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

> 18 preguntas de opción múltiple. Cada una trae su propio código o un caso concreto — no necesitas recordar de qué sección era, solo leerlo y razonar.

**1.** ¿Qué imprime este código?

```python
import hashlib
def h(t): return hashlib.sha256(t.encode()).hexdigest()

print(h("clave123") == h("clave123"))
print(h("clave123") == h("Clave123"))
```

A) `True` y `True`
B) `True` y `False`
C) `False` y `False`
D) `False` y `True`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> El hash es determinista (mismo texto exacto → mismo resultado), pero es sensible a mayúsculas: <code>"clave123"</code> y <code>"Clave123"</code> son cadenas distintas, así que sus hashes también lo son.</details>

**2.** ¿Qué imprime este código?

```python
import hashlib
def h(t): return hashlib.sha256(t.encode()).hexdigest()

a, b = h("1234"), h("1235")
iguales = sum(1 for x, y in zip(a, b) if x == y)
print(iguales < 20)
```

A) `True`
B) `False`
C) Lanza una excepción, `zip` no funciona con cadenas
D) Depende de la máquina donde se ejecute

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: A.</b> Es el efecto avalancha: cambiar un solo carácter de la entrada altera la mayoría del hash, así que muy pocos de los 64 caracteres siguen coincidiendo entre los dos hashes.</details>

**3.** Tienes estas dos funciones para comparar dos cadenas secretas:

```python
import hmac

def comparar_lento(a: str, b: str) -> bool:
    return a == b

def comparar_seguro(a: str, b: str) -> bool:
    return hmac.compare_digest(a, b)
```

¿Cuál de las dos es vulnerable a un ataque de temporización, y por qué?

A) `comparar_seguro`, porque `hmac` es más lento
B) `comparar_lento`, porque `==` se detiene en el primer carácter distinto y el tiempo de respuesta varía según cuántos caracteres coincidan
C) Ninguna, ambas tardan exactamente lo mismo siempre
D) `comparar_lento`, porque Python no permite comparar cadenas con `==`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> <code>==</code> compara carácter a carácter y se detiene en el primer fallo; ese tiempo variable puede filtrar información a un atacante. <code>compare_digest</code> siempre tarda lo mismo, sin importar dónde esté la diferencia.</details>

**4.** ¿Qué imprime este código?

```python
import hashlib

def hash_bloques(datos: bytes, n: int = 4) -> str:
    h = hashlib.sha256()
    for i in range(0, len(datos), n):
        h.update(datos[i:i + n])
    return h.hexdigest()

print(hash_bloques(b"holamundo", 4) == hashlib.sha256(b"holamundo").hexdigest())
```

A) `True`
B) `False`
C) Lanza `TypeError`
D) Depende del valor de `n`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: A.</b> Hashear un dato entero de una vez o alimentarlo por trozos con <code>update()</code> produce exactamente el mismo resultado — es lo que permite hashear ficheros enormes sin cargarlos enteros en memoria.</details>

**5.** ¿Qué imprime este código?

```python
from cryptography.fernet import Fernet, InvalidToken

clave = Fernet.generate_key()
f = Fernet(clave)
token = f.encrypt(b"mensaje")
alterado = token[:-1] + b"X"      # se cambia el último byte

try:
    f.decrypt(alterado)
    resultado = "descifrado sin problema"
except InvalidToken:
    resultado = "rechazado"

print(resultado)
```

A) `descifrado sin problema`, porque Fernet ignora bytes sueltos manipulados
B) `rechazado`, porque Fernet detecta que el texto cifrado fue alterado
C) El programa se cuelga esperando una respuesta
D) Lanza `KeyError`, no `InvalidToken`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> Fernet es cifrado autenticado: verifica la integridad del texto cifrado antes de descifrar, y si detecta manipulación lanza <code>InvalidToken</code> en vez de devolver datos corruptos.</details>

**6.** Ana tiene un par de claves (`privada_ana`, `publica_ana`). Quieres enviarle un mensaje que **solo ella** pueda leer:

```python
oaep = padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
mensaje_cifrado = ____.encrypt(b"secreto", oaep)
```

¿Qué clave va en el hueco?

A) `privada_ana`
B) `publica_ana`
C) Tu propia clave privada
D) Cualquiera de las dos, da igual

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> Se cifra con la clave <b>pública</b> del destinatario; solo su clave privada (que nadie más tiene) puede descifrarlo después.</details>

**7.** ¿Qué imprime este código?

```python
firma = privada.sign(documento, pss, hashes.SHA256())

def verifica(doc: bytes) -> bool:
    try:
        publica.verify(firma, doc, pss, hashes.SHA256())
        return True
    except InvalidSignature:
        return False

print(verifica(documento))
print(verifica(documento + b"!"))
```

A) `True` y `True`
B) `True` y `False`
C) `False` y `True`
D) `False` y `False`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> La firma se calculó sobre <code>documento</code> exacto; verificar ese mismo documento da <code>True</code>, pero cambiar un solo carácter (<code>documento + b"!"</code>) hace que la verificación falle.</details>

**8.** Generas un certificado así:

```python
certificado = (
    x509.CertificateBuilder()
    .subject_name(nombre)
    .issuer_name(nombre)          # mismo valor que subject_name
    .public_key(clave.public_key())
    .sign(clave, hashes.SHA256())
)
print(certificado.subject == certificado.issuer)
```

¿Qué imprime, y qué tipo de certificado es?

A) `False`; es un certificado firmado por una CA
B) `True`; es un certificado autofirmado
C) Lanza una excepción, `subject` e `issuer` no se pueden comparar
D) `True`; es un certificado revocado

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> Como <code>issuer_name</code> recibe el mismo <code>nombre</code> que <code>subject_name</code>, el certificado se firma a sí mismo — por definición, un certificado autofirmado.</details>

**9.** ¿Qué imprime este código, sabiendo que `privada` es una clave RSA de 2048 bits?

```python
contenido = b"informe confidencial de la empresa"
firma = privada.sign(contenido, pss, hashes.SHA256())
print(len(firma))
```

A) `19`, la longitud del texto en bytes
B) `32`, el tamaño de un hash SHA-256 en bytes
C) `256`, el tamaño fijo que da una clave RSA de 2048 bits (2048 ÷ 8)
D) Depende de la longitud de `contenido`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: C.</b> El tamaño de una firma RSA lo determina el tamaño de la <b>clave</b>, no el del documento firmado — por eso firmar un byte o firmar un fichero de 10 GB da siempre 256 bytes con esta clave.</details>

**10.** Tienes esta función de auditoría:

```python
def auditar(previo: dict, actual: dict) -> dict:
    r = {}
    for n, h in previo.items():
        if n not in actual:
            r[n] = "AUSENTE"
        elif h == actual[n]:
            r[n] = "OK"
        else:
            r[n] = "MODIFICADO"
    for n in actual:
        if n not in previo:
            r[n] = "NUEVO"
    return r

print(auditar({"a": "x", "b": "y"}, {"a": "x", "c": "z"}))
```

¿Qué imprime?

A) `{'a': 'OK', 'b': 'AUSENTE', 'c': 'NUEVO'}`
B) `{'a': 'OK', 'b': 'MODIFICADO'}`
C) `{'a': 'OK', 'b': 'OK', 'c': 'OK'}`
D) `{'a': 'OK'}`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: A.</b> <code>"a"</code> tiene el mismo hash en ambos → <code>OK</code>. <code>"b"</code> estaba en <code>previo</code> pero ya no está en <code>actual</code> → <code>AUSENTE</code>. <code>"c"</code> no estaba en <code>previo</code> → <code>NUEVO</code>.</details>

**11.** Tienes esta cadena de hashes (cada uno depende del anterior):

```python
def cadena(bloques: list[str]) -> list[str]:
    hashes_, anterior = [], "0" * 64
    for b in bloques:
        h = hashlib.sha256((anterior + b).encode()).hexdigest()
        hashes_.append(h)
        anterior = h
    return hashes_

c1 = cadena(["a", "b", "c"])
c2 = cadena(["a", "X", "c"])     # se altera el bloque del medio
print(c1[0] == c2[0], c1[1] == c2[1], c1[2] == c2[2])
```

¿Qué imprime?

A) `True True True`
B) `False False False`
C) `True False False`
D) `True True False`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: C.</b> El primer bloque no depende del alterado, así que su hash no cambia. Pero a partir de ahí, cada hash incorpora el anterior — alterar el bloque 2 cambia su hash y, en cascada, también el del bloque 3.</details>

**12.** ¿Qué imprime este código?

```python
from dataclasses import dataclass

@dataclass
class Copia:
    soporte: str
    ubicacion: str

def cumple_321(copias: list[Copia]) -> tuple[bool, list[str]]:
    fallos = []
    if len(copias) < 3:
        fallos.append("num")
    if len({c.soporte for c in copias}) < 2:
        fallos.append("soporte")
    if not any(c.ubicacion == "externo" for c in copias):
        fallos.append("externo")
    return (not fallos, fallos)

copias = [Copia("disco_local", "sitio"), Copia("disco_local", "sitio"), Copia("nas", "externo")]
print(cumple_321(copias))
```

A) `(True, [])`
B) `(False, ['num'])`
C) `(False, ['soporte'])`
D) `(False, ['num', 'soporte'])`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: A.</b> Hay 3 copias (cumple), dos soportes distintos (<code>disco_local</code> y <code>nas</code>, cumple) y una está en <code>"externo"</code> (cumple) — las tres condiciones se satisfacen.</details>

**13.** ¿Qué imprime este código?

```python
from enum import Enum

class Pilar(Enum):
    CONFIDENCIALIDAD = "C"
    INTEGRIDAD = "I"
    DISPONIBILIDAD = "D"

def describe(p: Pilar) -> str:
    return f"Rompe: {p.name}"

incidente = Pilar.DISPONIBILIDAD
print(describe(incidente))
```

A) `Rompe: D`
B) `Rompe: DISPONIBILIDAD`
C) `Rompe: Pilar.DISPONIBILIDAD`
D) Lanza `AttributeError`, `Enum` no tiene atributo `name`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> <code>.name</code> devuelve el nombre del miembro del <code>Enum</code> (<code>"DISPONIBILIDAD"</code>), no su valor (<code>.value</code> daría <code>"D"</code>).</details>

**14.** ¿Qué imprime este código?

```python
def riesgo(probabilidad: float, impacto: float) -> float:
    return round(probabilidad * impacto, 2)

print(riesgo(probabilidad=0.9, impacto=6))
```

A) `5.4`
B) `6.9`
C) `0.9`
D) `54.0`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: A.</b> <code>0.9 × 6 = 5.4</code>, redondeado a 2 decimales sigue siendo <code>5.4</code>.</details>

**15.** *(Sobre el reto de la unidad)* Un fichero de configuración cambia de valor, y aparece un fichero nuevo. Con las funciones del verificador de integridad:

```python
manifiesto = {"app.conf": "hash_de_puerto=8080", "app.bin": "hash_binario"}
actual =     {"app.conf": "hash_de_puerto=9090", "app.bin": "hash_binario", "nuevo.txt": "hash_x"}

print(auditar(manifiesto, actual))
```

(`auditar` es la misma función de la pregunta 10.) ¿Qué imprime?

A) `{'app.conf': 'OK', 'app.bin': 'OK', 'nuevo.txt': 'NUEVO'}`
B) `{'app.conf': 'MODIFICADO', 'app.bin': 'OK', 'nuevo.txt': 'NUEVO'}`
C) `{'app.conf': 'AUSENTE', 'app.bin': 'OK'}`
D) `{'app.conf': 'MODIFICADO', 'app.bin': 'MODIFICADO', 'nuevo.txt': 'NUEVO'}`

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> <code>app.conf</code> cambió de valor (hash distinto) → <code>MODIFICADO</code>. <code>app.bin</code> sigue igual → <code>OK</code>. <code>nuevo.txt</code> no estaba en el manifiesto original → <code>NUEVO</code>. Es exactamente el mecanismo que usa tu <code>verificador.py</code> para detectar manipulaciones.</details>

**16.** *(Sobre el reto de la unidad)* ¿Qué ocurre al ejecutar este código?

```python
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("accion", choices=["generar", "auditar"])
ap.add_argument("--algoritmo", default="sha256", choices=["sha256", "sha3_256", "blake2b"])

args = ap.parse_args(["generar", "--algoritmo", "md5"])
print(args.algoritmo)
```

A) Imprime `"md5"` sin problema
B) `argparse` rechaza la ejecución, porque `"md5"` no está entre los `choices` permitidos
C) Imprime `"sha256"`, ignorando el valor inválido
D) Lanza `TypeError` en tiempo de ejecución

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> Al declarar <code>choices=[...]</code>, <code>argparse</code> valida el valor <b>antes</b> de que tu código lo use, y termina el programa con un mensaje de error si no está en la lista — así el <code>verificador.py</code> nunca llega a intentar hashear con un algoritmo roto como MD5.</details>

**17.** En RSA con la librería `cryptography`, usas dos tipos de "relleno": **OAEP** y **PSS**. ¿Para qué sirve cada uno?

A) OAEP para firmar y PSS para cifrar
B) OAEP para cifrar y PSS para firmar
C) Los dos sirven para lo mismo, son intercambiables
D) OAEP es para RSA y PSS para AES

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> <b>OAEP</b> se usa en <code>encrypt</code>/<code>decrypt</code> (ocultar un mensaje); <b>PSS</b> en <code>sign</code>/<code>verify</code> (demostrar autoría). No son intercambiables: cada operación necesita el suyo.</details>

**18.** Eva intercepta un mensaje que Ana ha cifrado con la clave **pública de Luis**. Eva también tiene esa clave pública (es pública). ¿Puede leer el mensaje?

A) Sí, porque tiene la clave pública con la que se cifró
B) No: la clave pública solo sirve para cifrar; descifrar requiere la **privada de Luis**, que solo Luis tiene
C) Sí, si usa su propia clave privada
D) Solo si el mensaje mide menos de 256 bytes

<details class="sol"><summary>Ver respuesta</summary><b>Correcta: B.</b> Es la base del cifrado asimétrico: lo que se cifra con una pública **solo** lo abre la privada emparejada. Por eso repartir la clave pública no compromete la seguridad.</details>
