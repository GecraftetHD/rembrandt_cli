import asyncio

import websockets
import os
import json
import websocket
import exceptions



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

    def change_password(self, username, old_password, new_password):
        data = f'''
        {{
            "action":"password",
            "name":"{username}",
            "password":"{old_password}",
            "new":"{new_password}",
        }}
        '''
        self.websocket.send(data)
        response = self.websocket.recv()
        if 'error' in response:
            raise exceptions.Error
            return "Error"
        else:
            return "success"

    def register_account(self, username, password):
        data = f'''
        {{
            "action":"register",
            "name":"{username}",
            "password":"{password}"
        }}
        '''
        self.websocket.send(data)
        response = self.websocket.recv()
        if 'error' in response:
            raise exceptions.Error
            return 'Error'
        else:
            return 'success'

    def info(self):
        if not self.logged_in == True:
            raise exceptions.Error
        else:
            data = '''
            {
                "action":"info"
            }
            '''
            self.websocket.send(data)
            response = self.websocket.recv()
            return response

    def delete_account(self):
        if not self.logged_in == True:
            raise exceptions.Error
        else:
            data = '''
            {
                "action":"delete"
            }
            '''
            self.websocket.send(data)
            response = self.websocket.recv()
            return response
