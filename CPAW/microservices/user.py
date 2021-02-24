from typing import List

from CPAW import Client
from CPAW.microservices import Device


class User:
    def __init__(self, client: Client) -> None:
        self.client: Client = client
        data: dict = client.info()
        self.name: str = data["name"]
        self.uuid: str = data["uuid"]

    def delete_devices(self) -> bool:
        return self.client.microservice("device", ["delete_user"], user_uuid=self.uuid)["ok"]

    def devices(self) -> List[Device]:
        response: list = self.client.microservice("device", ["device", "all"])["devices"]
        return [Device(self.client, device) for device in response]

    def spot(self) -> Device:
        return Device(self.client, self.client.microservice("device", ["spot"]))
