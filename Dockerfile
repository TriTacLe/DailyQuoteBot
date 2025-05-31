FROM python:3.12-slim

WORKDIR /src

COPY requirements.txt .

COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

CMD ["python", "src/main.py"]
