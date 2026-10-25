import re
from collections import Counter

UMBRAL = 3

def leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read().splitlines()

# 1) auth.log: contar fallos de login por IP
fallos = Counter()
for linea in leer("auth.log"):
    m = re.search(r"Failed password for \S+ from (\d+\.\d+\.\d+\.\d+)", linea)
    if m:
        fallos[m.group(1)] += 1

# 2) web.log: contar errores 404 por IP (rastreo de rutas que no existen)
rutas_404 = Counter()
for linea in leer("web.log"):
    m = re.search(r"(\d+\.\d+\.\d+\.\d+).* 404$", linea)
    if m:
        rutas_404[m.group(1)] += 1

print("Fallos de login por IP:", dict(fallos))
print("Errores 404 por IP:    ", dict(rutas_404))

# 3) mini-IDS: una IP es sospechosa si supera el umbral en login O en rutas
print("\n--- ALERTAS ---")
hay = False
for ip in sorted(set(fallos) | set(rutas_404)):
    motivos = []
    if fallos[ip] >= UMBRAL:
        motivos.append(f"fuerza bruta ({fallos[ip]} fallos de login)")
    if rutas_404[ip] >= UMBRAL:
        motivos.append(f"rastreo de rutas ({rutas_404[ip]} rutas inexistentes)")
    if motivos:
        hay = True
        print(f"  [ALERTA] {ip}: " + " + ".join(motivos))
if not hay:
    print("  (ninguna)")
