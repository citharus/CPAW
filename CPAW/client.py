import json
import re
import ssl
from typing import Optional, List
from uuid import uuid4

from websocket import WebSocket, create_connection

from .exceptions import (
    InvalidServerResponseException,
    UnknownMicroserviceException,
    MicroserviceException,
    LoggedInException,
    LoggedOutException,
    InvalidLoginException)


class Client:
    def __init__(self, server: str, username: str, password: str) -> None:
        self.server: str = server
        self.__username: str = username
        self.__password: str = password
        self.logged_in: bool = False
        self.websocket: Optional[WebSocket] = None
        self.waiting_for_response: bool = False
        self.notifications: List[dict] = []

    def init(self) -> None:
        try:
            self.websocket: WebSocket = create_connection(self.server)
        except ssl.SSLCertVerificationError:
            self.websocket: WebSocket = create_connection(self.server, sslopt={"cert_reqs": ssl.CERT_NONE})

    def close(self) -> None:
        self.websocket.close()
        self.websocket: Optional[WebSocket] = None
        self.logged_in = False

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

    def microservice(self, microservice: str, endpoint: List[str], **data) -> dict:
        if not self.logged_in:
            raise LoggedOutException

        response: dict = self.request({"ms": microservice, "endpoint": endpoint, data: data, "tag": str(uuid4())})

        if "error" in response:
            error: str = response["error"]
            if error == "unknown microservice":
                raise UnknownMicroserviceException(microservice)
            raise InvalidServerResponseException(response)

        if "data" not in response:
            raise InvalidServerResponseException(response)

        data: data = response["data"]

        if "error" in data:
            error: str = data["error"]
            for exception in MicroserviceException.__subclasses__():
                if re.fullmatch(exception.error, error):
                    raise Exception(error, data)
            raise InvalidServerResponseException(response)
        return data

    def login(self) -> str:
        if self.logged_in:
            raise LoggedInException

        response: dict = self.request({"action": "login", "name": self.__username, "password": self.__password})

        if "error" in response:
            self.close()
            error: str = response["error"]
            if error == "permissions denied":
                raise InvalidLoginException()
            raise InvalidServerResponseException(response)

        if "token" not in response:
            self.close()
            raise InvalidServerResponseException(response)

        self.logged_in = True
        return response["token"]
