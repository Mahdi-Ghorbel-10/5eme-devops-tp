# Dockerfile
FROM python:3.14.0a3-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

CMD ["pytest", "tests"]
