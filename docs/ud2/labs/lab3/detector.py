import re
from collections import Counter

UMBRAL = 3

# 1) auth.log: contar fallos de login por IP
fallos = Counter()
with open("auth.log", encoding="utf-8") as f:
    for linea in f:
        m = re.search(r"Failed password .* from (\d+\.\d+\.\d+\.\d+)", linea)
        if m:
            fallos[m.group(1)] += 1

# 2) web.log: contar errores 404 por IP (rutas que no existen)
rutas_404 = Counter()
with open("web.log", encoding="utf-8") as f:
    for linea in f:
        m = re.search(r"(\d+\.\d+\.\d+\.\d+).* 404$", linea.strip())
        if m:
            rutas_404[m.group(1)] += 1

print("Fallos de login por IP:", dict(fallos))
print("Errores 404 por IP:    ", dict(rutas_404))

# 3) Alertas: IP que supera el umbral en login o en rutas
print("\n--- ALERTAS ---")
for ip in sorted(set(fallos) | set(rutas_404)):
    motivos = []
    if fallos[ip] >= UMBRAL:
        motivos.append(f"fuerza bruta ({fallos[ip]} fallos de login)")
    if rutas_404[ip] >= UMBRAL:
        motivos.append(f"rastreo de rutas ({rutas_404[ip]} rutas inexistentes)")
    if motivos:
        print(f"  [ALERTA] {ip}: " + " + ".join(motivos))
