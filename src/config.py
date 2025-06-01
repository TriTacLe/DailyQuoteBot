import os
from dotenv import load_dotenv

load_dotenv()

ENABLE_BLBE = os.getenv("ENABLE_BIBLE", "false").lower() == "true"
ENABLE_KANYE = os.getenv("ENABLE_KANYE", "false").lower() == "true"
ENABLE_MOTIVATIONAL = os.getenv("ENABLE_MOTIVATIONAL", "false").lower() == "true"