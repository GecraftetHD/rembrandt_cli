import os

from rembrandt import Client
from dotenv import load_dotenv
load_dotenv()

import asyncio

client = Client('wss://ws.cryptic-game.net:443/')
print(client.status())
client.login(os.getenv('USERNAME'), os.getenv('PASSWORD'))