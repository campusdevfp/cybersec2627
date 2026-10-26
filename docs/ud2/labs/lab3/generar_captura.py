from scapy.all import Ether, IP, TCP, wrpcap

# El auditor (10.0.0.66) escanea 6 puertos del servidor; 10.0.0.5 es tráfico normal.
paquetes = []
for puerto in [22, 23, 80, 443, 3306, 8080]:
    paquetes.append(Ether()/IP(src="10.0.0.66", dst="10.0.0.10")/TCP(dport=puerto, flags="S"))
paquetes.append(Ether()/IP(src="10.0.0.5", dst="10.0.0.10")/TCP(dport=80, flags="S"))

wrpcap("captura.pcap", paquetes)
print(f"captura.pcap creada con {len(paquetes)} paquetes")
