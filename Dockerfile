FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libmagic1 \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"


CMD ["python", "main.py"]
