FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY auth.log web.log detector.py generar_captura.py ids_red.py .
# Root dentro del contenedor (puedes instalar con apt). Se mantiene vivo.
CMD ["sleep", "infinity"]
