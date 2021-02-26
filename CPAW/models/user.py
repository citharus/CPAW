from typing import List

from CPAW import Client
from CPAW.models import Device


class User:
    """The representation of an Cryptic Game user account"""
    def __init__(self, client: Client) -> None:
        """
        :param Client client: The client used by the user
        """
        self.client: Client = client
        data: dict = client.info()
        self.name: str = data["name"]
        self.uuid: str = data["uuid"]

    def delete_devices(self) -> None:
        """Delete all devices of the user."""
        self.client.microservice("device", ["delete_user"], user_uuid=self.uuid)

    def devices(self) -> List[Device]:
        """
        List all devices of the user.
        :return: List of devices
        :rtype: list[Device]
        """
        response: list = self.client.microservice("device", ["device", "all"])["devices"]
        return [Device(self.client, device) for device in response]

    def spot(self) -> Device:
        """
        Find a random device.
        :return: A random device
        :rtype: Device
        """
        return Device(self.client, self.client.microservice("device", ["spot"]))

    def create(self, gpu: List[str], cpu: List[str], mainboard: str, ram: List[str], disk: List[str],
               processorCooler: List[str], powerPack: str, case: str) -> Device:
        """
        Creates a new device from provided hardware parts.
        :param list[str] gpu: The names of the graphics processing units
        :param list[str] cpu: The names of the central processing units
        :param str mainboard: The name of the motherboard
        :param list[str] ram: The names of the memory units
        :param list[str] disk: The names of the disks
        :param list[str] processorCooler: The names of the cpu coolers
        :param str powerPack: The name of the power pack
        :param str case: The name of the case
        :return: A new device
        :rtype: Device
        """
        response: dict = self.client.microservice("device", ["device", "create"], gpu=gpu, cpu=cpu, mainboard=mainboard,
                                                  ram=ram, disk=disk, processorCooler=processorCooler, case=case,
                                                  powerPack=powerPack)
        return Device(self.client, response)

    def starter_device(self) -> Device:
        """
        Creates the starter device for the user.
        :return: The starter device
        :rtype: Device
        """
        return Device(self.client, self.client.microservice("device", ["device", "starter_device"]))

    def build_compatibility(self, gpu: List[str], cpu: List[str], mainboard: str, ram: List[str], disk: List[str],
                            processorCooler: List[str], powerPack: str, case: str) -> bool:
        """
        Checks the compatibility of the hardware parts.
        :param list[str] gpu: The names of the graphics processing units
        :param list[str] cpu: The names of the central processing units
        :param str mainboard: The name of the motherboard
        :param list[str] ram: The names of the memory units
        :param list[str] disk: The names of the disks
        :param list[str] processorCooler: The names of the cpu coolers
        :param str powerPack: The name of the power pack
        :param str case: The name of the case
        :return: A new device
        :rtype: Device
        """
        return self.client.microservice("device", ["hardware", "build"], gpu=gpu, cpu=cpu, mainboard=mainboard,
                                        ram=ram, disk=disk, processorCooler=processorCooler, case=case,
                                        powerPack=powerPack)["success"]
