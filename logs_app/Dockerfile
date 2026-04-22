FROM python:3.11-slim

WORKDIR /app

# Instalar SSH
RUN apt update && apt install -y openssh-client && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
