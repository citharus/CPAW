from typing import List

from CPAW import Client
from CPAW.microservices import Device


class Hardware:
    """The representation of a hardware part"""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the hardware part
        """
        self.client: Client = client
        self.uuid: str = data["uuid"]
        self.device: str = data["device_uuid"]
        self.hardware_element: str = data["hardware_element"]
        self.hardware_type: str = data["hardware_type"]

    def create(self, gpu: List[str], cpu: List[str], mainboard: str, ram: List[str], disk: List[str],
               processorCooler: List[str], powerPack: str, case: str) -> Device:
        """

        :param list[str] gpu: The names of the graphics processing units
        :param list[str] cpu: The names of the central processing units
        :param str mainboard: The name of the motherboard
        :param list[str] ram: The names of the memory units
        :param list[str] disk: The names of the disks
        :param list[str] processorCooler: The names of the cpu coolers
        :param str powerPack: The name of the power pack
        :param str case: The name of the case
        :return: A new Device
        :rtype: Device
        """
        response: dict = self.client.microservice("device", ["device", "create"], gpu=gpu, cpu=cpu, mainboard=mainboard,
                                                  ram=ram, disk=disk, processorCooler=processorCooler, case=case,
                                                  powerPack=powerPack)
        return Device(self.client, response)
