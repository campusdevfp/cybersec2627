import psutil
import platform

print("=== Auditoría del sistema ===")
print("SO:", platform.system(), platform.release())
print("CPU:", psutil.cpu_percent(interval=0.3), "%")

mem = psutil.virtual_memory()
print(f"Memoria: {mem.percent}% usada ({mem.used // (1024**2)} MB de {mem.total // (1024**2)} MB)")

print("\n-- Procesos que más memoria usan --")
procesos = []
for p in psutil.process_iter(["pid", "name", "memory_percent"]):
    try:
        procesos.append((p.info["memory_percent"] or 0.0, p.info["pid"], p.info["name"]))
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue
for mem_pct, pid, nombre in sorted(procesos, reverse=True)[:3]:
    print(f"  PID {pid:6}  {nombre:20}  {mem_pct:.1f}%")

print(f"\nTotal de procesos visibles: {len(procesos)}")
print("(Dentro de un contenedor, estos son los procesos DE ESE contenedor.)")
