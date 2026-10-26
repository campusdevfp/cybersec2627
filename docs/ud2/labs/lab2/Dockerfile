FROM python:3.12-slim
WORKDIR /app
COPY auditor.py .
RUN useradd --create-home auditor
USER auditor
CMD ["python", "auditor.py"]
