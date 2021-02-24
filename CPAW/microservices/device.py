from typing import Dict, List, Union, Optional

from CPAW import Client
from CPAW.microservices import File, Hardware


class Device:
    """The representation of a device"""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the device
        """
        self.client: Client = client
        self.uuid: str = data["uuid"]
        self.name: str = data["name"]
        self.owner: str = data["owner"]
        self.powered_on: bool = bool(data["powered_on"])
        self.starter_device: bool = bool(data["starter_device"])

    def ping(self) -> bool:
        """
        Return the power state of the device, True if the device is on and False if it's not.
        :return: Power state
        :rtype: bool
        """
        return self.client.microservice("device", ["device", "ping"], device_uuid=self.uuid)["online"]

    def power(self) -> bool:
        """
        Turn the device on or off.
        :return: Power state
        :rtype: bool
        """
        self.powered_on = self.client.microservice("device", ["device", "power"], device_uuid=self.uuid)["powered_on"]
        return self.powered_on

    def change_name(self, name: str) -> str:
        """
        Change the device name.
        :param str name: The new name of the device
        :return: The changed name of the device
        :rtype: str
        """
        return self.client.microservice("device", ["device", "change_name"], device_uuid=self.uuid, name=name)["name"]

    def delete(self) -> bool:
        """
        Delete the device including it's services.
        :return: True
        :rtype: bool
        """
        return self.client.microservice("device", ["device", "delete"], device_uuid=self.uuid)["ok"]

    def exists(self) -> bool:
        """
        Check if the device still exists.
        :return: True if the device exists or False if it doesn't
        :rtype: bool
        """
        return self.client.microservice("device", ["exist"], device_uuid=self.uuid)["exist"]

    def files(self, parent_dir_uuid: Optional[str] = None) -> List[File]:
        """
        List all files in a directory of the device. The default directory is the root one.
        :param parent_dir_uuid: The uuid of the directory the files should be listed (Default: Root directory)
        :return: List of Files in the directory
        :rtype: list[File]
        """
        response: list = self.client.microservice("device", ["file", "all"], device_uuid=self.uuid,
                                                  parent_dir_uuid=parent_dir_uuid)["files"]
        return [File(self.client, file) for file in response]

    def hardware(self) -> List[Hardware]:
        """
        List all hardware parts of the device.
        :return: List of hardware parts
        :rtype: list[Hardware]
        """
        response: list = self.client.microservice("device", ["device", "info"], device_uuid=self.uuid)["hardware"]
        return [Hardware(self.client, hardware) for hardware in response]
