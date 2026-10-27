FROM python:3.12-slim
WORKDIR /app
# Instalamos nmap, la herramienta estándar de escaneo y auditoría
RUN apt-get update && apt-get install -y --no-install-recommends nmap \
    && rm -rf /var/lib/apt/lists/*
COPY informe.py .
# Root dentro del contenedor y se mantiene vivo para que ejecutes los comandos.
CMD ["sleep", "infinity"]
