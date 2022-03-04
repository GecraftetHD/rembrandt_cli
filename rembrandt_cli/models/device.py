from rembrandt_cli.subfunc import uuid
import websocket

class Device:
    def __init__(self):
        pass

    def device_all(self):

        data = f'''
        {{
            "tag":"f177fe68-b06b-499e-a8da-dc5751902eff",
            "ms":"device",
            "endpoint":"['device', 'all']",
            "data":{{}}
        }}
        '''
        self.websocket.send(data)
        raw_response = self.websocket.recv()
        return raw_response