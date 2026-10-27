import xml.etree.ElementTree as ET

# "NVD local": versiones vulnerables conocidas (extracto, para el laboratorio)
NVD_LOCAL = {
    ("nginx", "1.18.0"): "CVE-2021-23017 (resolver, gravedad alta)",
    ("Apache httpd", "2.4.49"): "CVE-2021-41773 (path traversal, crítico)",
    ("OpenSSH", "7.4"): "CVE-2018-15473 (enumeración de usuarios)",
    ("vsftpd", "2.3.4"): "CVE-2011-2523 (puerta trasera, crítico)",
}

# nmap guardó el resultado del escaneo en este fichero XML
arbol = ET.parse("resultado.xml")

print("=== Informe de auditoría ===\n")
vulnerables = 0
for puerto in arbol.iter("port"):
    estado = puerto.find("state").get("state")
    if estado != "open":
        continue
    servicio = puerto.find("service")
    producto = servicio.get("product", "") if servicio is not None else ""
    version = servicio.get("version", "") if servicio is not None else ""
    cve = NVD_LOCAL.get((producto, version), "")
    marca = f"VULNERABLE: {cve}" if cve else "sin vulnerabilidades conocidas"
    if cve:
        vulnerables += 1
    print(f"  Puerto {puerto.get('portid'):5}  {producto} {version:10}  {marca}")

print(f"\nResumen: {vulnerables} servicio(s) con vulnerabilidades conocidas.")
