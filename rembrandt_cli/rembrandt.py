import json
import websocket
import rembrandt_cli.exceptions


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
        raw_response = self.websocket.recv()
        response = json.loads(raw_response)
        if 'error' in raw_response:
            error = response['error']
            if error == 'missing parameters':
                raise rembrandt_cli.exceptions.MissingParametersError
            elif error == 'permissions denied':
                raise rembrandt_cli.exceptions.PermissionDeniedError
        else:
            self.logged_in = True
            return response

    def status(self):
        data = '''
        {
            "action":"status"
        }
        '''
        self.websocket.send(data)
        raw_response = self.websocket.recv()
        response = json.loads(raw_response)
        return response

    def logout(self):
        data = '''
        {
            "action":"logout"
        }
        '''
        self.websocket.send(data)
        raw_response = self.websocket.recv()
        response = json.loads(raw_response)
        return response

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
        raw_response = self.websocket.recv()
        response = json.loads(raw_response)
        if 'error' in response:
            error = response['error']
            if error == 'missing parameters':
                raise rembrandt_cli.exceptions.MissingParametersError
            elif error == 'permission denied':
                raise rembrandt_cli.exceptions.PermissionDeniedError

        else:
            return response

    def register_account(self, username, password):
        data = f'''
        {{
            "action":"register",
            "name":"{username}",
            "password":"{password}"
        }}
        '''
        self.websocket.send(data)
        raw_response = self.websocket.recv()
        response = json.loads(raw_response)
        if 'error' in response:
            error = response["error"]
            if error == 'missing parameters':
                raise rembrandt_cli.exceptions.MissingParametersError
            elif error == "invalid password":
                raise rembrandt_cli.exceptions.PasswordRequirementsError
            elif error == 'username already exists':
                raise rembrandt_cli.exceptions.UsernameAlreadyExistsError

        else:
            return response

    def info(self):
        if not self.logged_in == True:
            raise rembrandt_cli.exceptions.NotLoggedInError
        else:
            data = '''
            {
                "action":"info"
            }
            '''
            self.websocket.send(data)
            raw_response = self.websocket.recv()
            response = json.loads(raw_response)
            return response

    def delete_account(self):
        if not self.logged_in == True:
            raise rembrandt_cli.exceptions.NotLoggedInError
        else:
            data = '''
            {
                "action":"delete"
            }
            '''
            self.websocket.send(data)
            raw_response = self.websocket.recv()
            response = json.loads(raw_response)
            return response
