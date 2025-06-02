FROM python:3.12-slim

WORKDIR /src

COPY requirements.txt .

COPY .env .
RUN pip install --no-cache-dir -r requirements.txt

#RUN apt add --no-cache tzdata && cp /usr/share/zoneinfo/Europe/Oslo /etc/localtime && echo "Europe/Oslo" > /etc/timezone && apk del tzdata

#COPY src/ ./src/
COPY . .

CMD ["python", "-m", "src.main"]
