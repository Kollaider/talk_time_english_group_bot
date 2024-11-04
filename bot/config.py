# config.py
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MEME_API_KEY = os.getenv("MEME_API_KEY")
CHAT_ID = os.getenv("CHAT_ID")
