from typing import List

from CPAW import Client
from CPAW.microservices import Device


class User:
    def __init__(self, client: Client) -> None:
        self.client: Client = client
        data: dict = client.info()
        self.name: str = data["name"]
        self.uuid: str = data["uuid"]

    def devices(self) -> List[Device]:
        return self.client.microservice("device", ["device", "all"])["devices"]
