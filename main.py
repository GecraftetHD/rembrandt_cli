import os
from rembrandt_cli.rembrandt import Client
from dotenv import load_dotenv
load_dotenv()

client = Client('wss://ws.cryptic-game.net:443/')
print(client.status())
print(client.login('allah579123', 'Testblyat123!'))
print(client.info())
print(client.logout())