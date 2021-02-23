from typing import Optional

from websocket import WebSocket


class Client:
    def __init__(self, server: str, username: str, password: str) -> None:
        self.server: str = server
        self.__username: str = username
        self.__password: str = password
        self.websocket: Optional[WebSocket] = None
