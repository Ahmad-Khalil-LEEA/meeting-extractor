FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for Whisper
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

WORKDIR /app/app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
