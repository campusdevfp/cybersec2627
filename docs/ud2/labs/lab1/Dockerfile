FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY auditor_sistema.py .
# Se ejecuta como root: puedes instalar paquetes con apt dentro del contenedor.
# El contenedor se mantiene vivo para poder entrar y lanzar el script tú mismo.
CMD ["sleep", "infinity"]
