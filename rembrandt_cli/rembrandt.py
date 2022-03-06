import json
import websocket
import rembrandt_cli.exceptions
import sys

def frontend():
    while True:
        command = input("$ ")
        if command == "exit":
            break
        elif command == "help":
            print("rembrandt_cli | a python based cryptic game client\n"
                  " -help | list all commands\n"
                  " -exit | stops the client\n")
        else:
            print(command)

def main():
    args = sys.argv[1:]
    if len(args) > 0:
        server = args[0]
    else:
        server = 'wss://ws.cryptic-game.net'

    print("")
    print("Welcome to rembrandt_cli")
    print("")
    print("GitHub: https://github.com/GecraftetHD/rembrandt_cli")
    frontend()
