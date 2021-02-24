from typing import Dict

from CPAW import Client


class Device:
    def __init__(self, client: Client, data: dict) -> None:
        self.microservice = client.microservice
        self.uuid: str = data["uuid"]
        self.name: str = data["name"]
        self.owner: str = data["owner"]
        self.powered_on: bool = bool(data["powered_on"])
        self.starter_device: bool = bool(data["starter_device"])

    def info(self) -> Dict:
        return self.microservice("device", ["device", "info"])

    def ping(self) -> bool:
        return self.microservice("device", ["device", "ping"])["online"]
