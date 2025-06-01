```bash
pip freeze -> requirements.txt
```

# Docker

Manually

```bash
docker build -t dailyboatcarry:latest .
docker rm -f dailyboatcarry-container
docker rmi dailyboatcarry:latest
docker run -d --name dailyboatcarry-container dailyboatcarry:latest
```

Docker compose

```bash
docker compose down
docker compose up -d
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

Check

```bash
docker images
docker ps -a
```
