FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y curl && \
    pip install flask && \
    apt-get clean

EXPOSE 30000

CMD ["python", "app.py"]


