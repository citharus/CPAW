from typing import Dict, List, Union, Optional

from CPAW import Client
from CPAW.microservices import File, Hardware


class Device:
    def __init__(self, client: Client, data: dict) -> None:
        self.client: Client = client
        self.uuid: str = data["uuid"]
        self.name: str = data["name"]
        self.owner: str = data["owner"]
        self.powered_on: bool = bool(data["powered_on"])
        self.starter_device: bool = bool(data["starter_device"])

    def ping(self) -> bool:
        return self.client.microservice("device", ["device", "ping"], device_uuid=self.uuid)["online"]

    def all(self) -> List[Dict[str, Union[str, bool]]]:
        return self.client.microservice("device", ["device", "all"])["devices"]

    def power(self) -> bool:
        self.powered_on = self.client.microservice("device", ["device", "power"], device_uuid=self.uuid)["powered_on"]
        return self.powered_on

    def change_name(self, name: str) -> str:
        return self.client.microservice("device", ["device", "change_name"], device_uuid=self.uuid, name=name)["name"]

    def delete(self) -> bool:
        return self.client.microservice("device", ["device", "delete"], device_uuid=self.uuid)["ok"]

    def exists(self) -> bool:
        return self.client.microservice("device", ["exist"], device_uuid=self.uuid)["exist"]

    def files(self, parent_dir_uuid: Optional[str] = None) -> List[File]:
        response: list = self.client.microservice("device", ["file", "all"], device_uuid=self.uuid,
                                                  parent_dir_uuid=parent_dir_uuid)["files"]
        return [File(self.client, file) for file in response]

    def hardware(self) -> List[Hardware]:
        response: list = self.client.microservice("device", ["device", "info"], device_uuid=self.uuid)["hardware"]
        return [Hardware(self.client, hardware) for hardware in response]
