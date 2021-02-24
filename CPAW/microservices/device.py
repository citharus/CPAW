from typing import Dict, List, Union

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
        return self.microservice("device", ["device", "info"], device_uuid=self.uuid)

    def ping(self) -> bool:
        return self.microservice("device", ["device", "ping"], device_uuid=self.uuid)["online"]

    def all(self) -> List[Dict[str, Union[str, bool]]]:
        return self.microservice("device", ["device", "all"])["devices"]

    def power(self) -> bool:
        self.powered_on = self.microservice("device", ["device", "power"], device_uuid=self.uuid)["powered_on"]
        return self.powered_on

    def change_name(self, name: str) -> str:
        return self.microservice("device", ["device", "change_name"], device_uuid=self.uuid, name=name)["name"]

    def delete(self) -> bool:
        return self.microservice("device", ["device", "delete"], device_uuid=self.uuid)["ok"]

    def exists(self) -> bool:
        return self.microservice("device", ["exist"], device_uuid=self.uuid)["exist"]