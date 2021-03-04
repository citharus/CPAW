from typing import Optional, Dict, Union

from CPAW import Client
from CPAW.models import File, Hardware, Wallet
from CPAW.utils import *


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

    @property
    def files(self, parent_dir_uuid: Optional[str] = None) -> List[File]:
        """
        List all files in a directory of the device. The default directory is the root one.
        :param str parent_dir_uuid: The uuid of the directory the files should be listed (Default: Root directory)
        :return: List of Files in the directory
        :rtype: list[File]
        """
        response: list = self.client.microservice("device", ["file", "all"], device_uuid=self.uuid,
                                                  parent_dir_uuid=parent_dir_uuid)["files"]
        return [File(self.client, file) for file in response]

    @property
    def hardware(self) -> List[Hardware]:
        """
        List all hardware parts of the device.
        :return: List of hardware parts
        :rtype: list[Hardware]
        """
        response: list = self.client.microservice("device", ["device", "info"], device_uuid=self.uuid)["hardware"]
        return [Hardware(self.client, hardware) for hardware in response]

    @property
    def services(self) -> List[Service]:
        """
        Return a list with services on the device.
        :return: A list with services
        :rtype: list[Service]
        """
        response: dict = self.client.microservice("service", ["list"], device_uuid=self.uuid)["services"]
        return convert_services(self.client, response)

    @property
    def info(self) -> Dict[str, Union[str, bool, List[Dict[str, str]]]]:
        """
        Return information about the device and it's hardware in a dictionary.
        :return: Dictionary containing information
        :rtype: dict
        """
        return self.client.microservice("device", ["device", "info"], device_uuid=self.uuid)

    @property
    def name(self) -> str:
        """
        Return the name of the device.
        :return: The name of the device
        :rtype: str
        """
        return self.name

    @name.setter
    def name(self, name: str) -> None:
        """
        Change the device name.
        :param str name: The new name of the device
        """
        self.name = self.client.microservice("device", ["device", "change_name"],
                                             device_uuid=self.uuid, name=name)["name"]

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
        :return: Power state of the device
        :rtype: bool
        """
        self.powered_on = self.client.microservice("device", ["device", "power"], device_uuid=self.uuid)["powered_on"]
        return self.powered_on

    def delete(self) -> bool:
        """
        Delete the device including it's services.
        :return: True
        :rtype: bool
        """
        return self.client.microservice("device", ["device", "delete"], device_uuid=self.uuid)["ok"]

    def restart(self) -> bool:
        """
        Start the enforced services of a device that hast just been started.
        :return: True if the devices has restarted
        :rtype: bool
        """
        return self.client.microservice("service", ["device_restart"], device_uuid=self.uuid, user=self.owner)["ok"]

    def init(self) -> bool:
        """
        Initiate a new device with the enforced services.
        :return: True if the device has initialized
        :rtype: bool
        """
        return self.client.microservice("service", ["device_init"], device_uuid=self.uuid, user=self.owner)["ok"]

    def exists(self) -> bool:
        """
        Check if the device still exists.
        :return: True if the device exists or False if it doesn't
        :rtype: bool
        """
        return self.client.microservice("device", ["exist"], device_uuid=self.uuid)["exist"]

    def part_owner(self) -> bool:
        """
        Return if the user has hacked this devices and still has access to it.
        :return: Access status
        :rtype: bool
        """
        return self.client.microservice("service", ["part_owner"], device_uuid=self.uuid)["ok"]

    def usage(self) -> Dict[str, Union[str, float]]:
        """
        Return the current resource usage of the devices hardware.
        :return: Dictionary with resource usage
        :rtype: dict
        """
        return self.client.microservice("device", ["hardware", "resource"], device_uuid=self.uuid)

    def create_file(self, filename: str, content: str, parent_dir_uuid: str = None,
                    is_directory: bool = False) -> File:
        """
        Creates a new file of directory on the device. By default the parent directory is root and it's a file.
        :param str filename: The file name
        :param str content: The file content
        :param str parent_dir_uuid: The parent directory (default: Root)
        :param bool is_directory: If the file is a directory (default: False)
        :return: A new file or directory
        :rtype: File
        """
        response: dict = self.client.microservice("device", ["file", "create"], device_uuid=self.uuid, content=content,
                                                  filename=filename, parent_dir_uuid=parent_dir_uuid,
                                                  is_directory=is_directory)
        return File(self.client, response)

    def create_service(self, name: str) -> Service:
        """
        Installs a new service on the device.
        :param str name: The name of the service (Available services: ssh, telnet, portscan, bruteforce)
        :return: The newly installed service
        :rtype: Service
        """
        response: dict = self.client.microservice("service", ["create"], device_uuid=self.uuid, name=name)
        return convert_services(self.client, response)[0]

    def create_miner(self) -> Miner:
        """
        Installs a new miner on the device.
        :return: The newly installed miner
        :rtype: Miner
        """
        return Miner(self.client, self.client.microservice("service", ["create"], device_uuid=self.uuid, name="miner"))

    def create_wallet(self) -> Wallet:
        """
        Create a new wallet on the device.
        :return: The new wallet
        :rtype: Wallet
        """
        return Wallet(self.client, self.client.microservice("currency", ["create"]))

    def stop_services(self) -> bool:
        """
        Stop all active service on the device.
        :return: True if all services were stopped
        :rtype: bool
        """
        return self.client.microservice("service", ["hardware", "stop"], device_uuid=self.uuid)["ok"]

    def delete_services(self) -> bool:
        """
        Delete all services on the device.
        :return: True if all services were deleted
        :rtype: bool
        """
        return self.client.microservice("service", ["hardware", "stop"], device_uuid=self.uuid)["ok"]
