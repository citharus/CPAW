import json
import ssl
from typing import Optional, List

from websocket import WebSocket, create_connection


class Client:
    def __init__(self, server: str, username: str, password: str) -> None:
        self.server: str = server
        self.__username: str = username
        self.__password: str = password
        self.websocket: Optional[WebSocket] = None
        self.waiting_for_response: bool = False
        self.notifications: List[dict] = []

    def start(self) -> None:
        try:
            self.websocket: WebSocket = create_connection(self.server)
        except ssl.SSLCertVerificationError:
            self.websocket: WebSocket = create_connection(self.server, sslopt={"cert_reqs": ssl.CERT_NONE})

    def close(self) -> None:
        self.websocket.close()
        self.websocket: Optional[WebSocket] = None

    def request(self, data: dict, no_response: bool = False) -> dict:
        if not self.websocket:
            raise ConnectionError

        self.websocket.send(json.dumps(data))
        if no_response:
            return {}
        self.waiting_for_response = True

        while True:
            response: dict = json.loads(self.websocket.recv())
            if "notify-id" in response:
                self.notifications.append(response)
            else:
                break

        self.waiting_for_response = False
        return response
