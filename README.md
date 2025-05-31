```bash
pip freeze -> requirements.txt
```

# Docker

Build the image, name the container

```bash
docker build -t dailyboatcarry .
docker run docker run -d --name dailyboatcarry dailyboatcarry
```

Dockerfile

```bash
docker stop dailyboatcarry
docker start dailyboatcarry
docker rm dailyboatcarry
```

docker-compose.yml

```bash
docker compose up -d
docker compose down
docker compose logs -f dailyboatcarry
docker compose stop
docker compose start
```
