FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY auth.log web.log detector.py generar_captura.py ids_red.py .
RUN useradd --create-home analista && chown analista /app
USER analista
CMD ["sh", "-c", "python detector.py && echo '' && python generar_captura.py && python ids_red.py"]
