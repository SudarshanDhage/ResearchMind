# ResearchMind backend — FastAPI + TextCNN
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
# CPU torch only (smaller / faster on Render free tier)
RUN pip install --no-cache-dir -r requirements.txt \
    --extra-index-url https://download.pytorch.org/whl/cpu

COPY backend/ ./backend/
COPY .env.example ./.env.example

WORKDIR /app/backend

ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
