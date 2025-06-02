# DailyQuoteBot

A Telegram bot and scheduler that sends you daily quotes per x times and sends you a quote if you send any messages to the bot

## Features

- Fetches and sends a random quote daily at a scheduled time.
- Supports multiple quote sources: Bible API, Kanye REST API, motivational quotes.
- Users can request a quote on-demand via the Telegram command `/w` or any messages to the bot.
- Deployable via Docker or runnable locally.

## Prerequisites

- Python 3.10+ installed locally.
- `pip` for installing Python dependencies.
- A Telegram account to create a bot.
- Docker for containerized deployment.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/TriTacLe/DailyQuoteBot.git
cd DailyQuoteBot
```

### 2. Create and Configure the Telegram Bot

1. Open Telegram and start a chat with BotFather.
2. Send /newbot and follow the prompts to set a name and username for your bot.
3. BotFather will provide you with a bot token. Copy this token.

### 3. Get Your Telegram Chat ID

In order to send messages to you, the bot needs your Chat ID:

1. Open a chat with your newly created bot and send any message (e.g., Hello).
2. Ensure the .env file has your TELEGRAM_BOT_TOKEN set (see next step).
3. Run the helper script:

```bash
python get_telegram_chat_id.py
```

This script will print your Chat ID. Copy value.

### 4. Configure Environment Variables

1. Copy the example file:

```bash
cp .env.example .env
```

2. Open .env in IDE and fill in the required fields:

```dotenv
# Time the bot sends a daily quote (24-hour format HH:MM)
TIME=07:00

# Quote Sources Endpoints (defaults work out of the box)
BASE_URL_BIBLE=https://bible-api.com/
BASE_URL_KANYE=https://api.kanye.rest
BASE_URL_MOTIVATIONAL=https://stoic.tekloon.net/stoic-quote

# Enable/Disable Quote Sources (true/false)
ENABLE_BIBLE=true
ENABLE_KANYE=false
ENABLE_MOTIVATIONAL=true

# Telegram Credentials
TELEGRAM_BOT_TOKEN=<your_bot_token>
TELEGRAM_BOT_USERNAME=@YourBotUsername
TELEGRAM_CHAT_ID=<your_chat_id>
```

3. Save `.env`

### 5. Install Dependencies

```bash
pip install --no-cache-dir -r requirements.txt
```

### 6. Docker

#### Running the Application Locally

From the project root, run:

```bash
python src/main.py
```

This will:

1. Start the scheduler, which sends a quote daily at the time specified by TIME.
2. Launch the Telegram bot, which listens for messages. You can request a quote manually by sending `/w` in the bot chat.

### Docker Setup manually

You can containerize the application for easier deployment.

1. Build the Docker Image

```bash
docker build -t dailyquotebot:latest .
```

2. Run the container manually

```bash
docker run -d --name dailyquotebot-container dailyquotebot:latest
```

3. Stop and remove image and container

```bash
docker rmi dailyquotebot:latest
docker rm -f dailyquotebot-container
```

### Docker compose

1. Start service

```bash
docker compose down
docker compose up --build
docker compose up -d
```

2. Stop service

```bash
docker compose down
```

3. #### Logs and troubleshooting

```bash
docker images
docker ps -a
docker compose logs -f dailyquotebot
```

4. Other commands

```bash
docker compose stop
docker compose start
pip freeze -> requirements.txt
```
