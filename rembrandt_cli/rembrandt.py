import asyncio

import websockets
import os
import json
import websocket



class Client:
    def __init__(self, server: str):
        self.logged_in = False
        self.server = server
        self.websocket = websocket.create_connection(self.server)

    def login(self, username: str, password: str):
        data = f'''
        {{
            "action":"login",
            "name":"{username}",
            "password":"{password}"
        }}
        '''
        self.websocket.send(data)
        token = self.websocket.recv()
        self.logged_in = True
        return token

    def status(self):
        data = '''
        {
            "action":"status"
        }
        '''
        self.websocket.send(data)
        return self.websocket.recv()

    def logout(self):
        self.websocket.send({"action":"logout"})
        return self.websocket.recv()

    def change_password(self):
        data = '''
        {
            "action":"password",
            "name":"<username [string]>",
            "password":"<old password [string]>",
            "new":"<new password [string]>",
        }
        '''

        pass

    def register_account(self):
        pass

    def info(self):
        pass

    def delete_account(self):
        pass
