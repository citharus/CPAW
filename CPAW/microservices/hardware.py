from typing import List

from CPAW import Client
from CPAW.microservices import Device


class Hardware:
    def __init__(self, client: Client, data: dict) -> None:
        self.client: Client = client
        self.uuid: str = data["uuid"]
        self.device: str = data["device_uuid"]
        self.hardware_element: str = data["hardware_element"]
        self.hardware_type: str = data["hardware_type"]

    def create(self, gpu: List[str], cpu: List[str], mainboard: str, ram: List[str], disk: List[str],
               processorCooler: List[str], powerPack: str, case: str) -> Device:
        response: dict = self.client.microservice("device", ["device", "create"], gpu=gpu, cpu=cpu, mainboard=mainboard,
                                                  ram=ram, disk=disk, processorCooler=processorCooler, case=case,
                                                  powerPack=powerPack)
        return Device(self.client, response)