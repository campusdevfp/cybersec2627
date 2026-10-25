from scapy.all import rdpcap, IP, TCP

UMBRAL_PUERTOS = 5

paquetes = rdpcap("captura.pcap")

# Una IP que envía SYN a muchos puertos distintos está escaneando.
puertos_por_ip = {}
for p in paquetes:
    if p.haslayer(TCP) and p[TCP].flags == "S":
        puertos_por_ip.setdefault(p[IP].src, set()).add(p[TCP].dport)

print("--- Mini-IDS de red (escaneo de puertos) ---")
for ip, puertos in puertos_por_ip.items():
    if len(puertos) >= UMBRAL_PUERTOS:
        print(f"  [ALERTA] {ip}: escaneo de puertos ({len(puertos)} puertos distintos)")
    else:
        print(f"  {ip}: {len(puertos)} puerto(s) contactado(s), normal")
