FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install \
    --default-timeout=1000 \
    --extra-index-url https://download.pytorch.org/whl/cpu \
    torch==2.3.1 \
    torchvision==0.18.1

RUN pip install \
    --default-timeout=1000\
    --retries=10\
    --no-cache-dir\
    -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]