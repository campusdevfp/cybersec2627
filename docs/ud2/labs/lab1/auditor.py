import socket
import json

OBJETIVO = "servidor"          # nombre del contenedor objetivo en la red Docker
PUERTOS = [22, 23, 80, 443, 3306, 8080]

# "NVD local": versiones vulnerables conocidas (extracto, para el laboratorio)
NVD_LOCAL = {
    "nginx/1.18.0": "CVE-2021-23017 (resolver, gravedad alta)",
    "Apache/2.4.49": "CVE-2021-41773 (path traversal, crítico)",
    "OpenSSH_7.4": "CVE-2018-15473 (enumeración de usuarios)",
    "vsftpd/2.3.4": "CVE-2011-2523 (puerta trasera, crítico)",
}

def escanear(host, puerto):
    """Devuelve (abierto, banner) para un puerto."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    try:
        if s.connect_ex((host, puerto)) != 0:
            return False, ""
        # Banner grabbing: pedimos algo y leemos lo que el servicio anuncia
        try:
            s.send(b"GET / HTTP/1.0\r\n\r\n")
            respuesta = s.recv(2048).decode(errors="ignore")
        except Exception:
            respuesta = ""
        banner = ""
        for linea in respuesta.splitlines():
            if linea.lower().startswith("server:"):
                banner = linea.split(":", 1)[1].strip()
        return True, banner
    finally:
        s.close()

def auditar():
    hallazgos = []
    print(f"Auditando {OBJETIVO}...\n")
    for puerto in PUERTOS:
        abierto, banner = escanear(OBJETIVO, puerto)
        if abierto:
            cve = NVD_LOCAL.get(banner, "")
            estado = f"VULNERABLE: {cve}" if cve else "sin vulnerabilidades conocidas"
            print(f"  [ABIERTO] puerto {puerto:5}  {banner or '(sin banner)':20}  {estado}")
            hallazgos.append({"puerto": puerto, "banner": banner, "vulnerabilidad": cve})
    # Informe automático en JSON
    with open("informe_auditoria.json", "w", encoding="utf-8") as f:
        json.dump(hallazgos, f, indent=2, ensure_ascii=False)
    vulnerables = [h for h in hallazgos if h["vulnerabilidad"]]
    print(f"\nResumen: {len(hallazgos)} servicios abiertos, {len(vulnerables)} vulnerables.")
    print("Informe guardado en informe_auditoria.json")

if __name__ == "__main__":
    auditar()
