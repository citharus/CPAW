from typing import Dict, Union

from CPAW import Client
from CPAW.utils import *


class Service:
    """Representation of the service base class."""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the service
        """
        self.client: Client = client
        self.uuid: str = data["uuid"]
        self.name: str = data["name"]
        self.owner: str = data["owner"]
        self.running_port: int = int(data["running_port"])
        self.device: str = data["device"]
        self.speed: int = int(data["speed"])

    def info(self) -> Dict[str, Union[str, int]]:
        """
        Return public information about the service in a dictionary.
        :return: Dictionary containing information
        :rtype: dict
        """
        return self.client.microservice("service", ["public_info"], device_uuid=self.device, service_uuid=self.uuid)

    def private_info(self) -> Dict[str, Union[str, int, bool]]:
        """
        Return private information about the service in a dictionary.
        :return: Dictionary containing information
        :rtype: dict
        """
        return self.client.microservice("service", ["private_info"], device_uuid=self.device, service_uuid=self.uuid)

    def usage(self) -> Dict[str, int]:
        """
        Return the resource usage of the service.
        :return: Dictionary with resource usage
        :rtype: dict
        """
        return self.client.microservice("device", ["hardware", "process"], service_uuid=self.uuid)

    def toggle(self) -> bool:
        """
        Turn the service on or off.
        :return: Power state of the service
        :rtype: bool
        """
        return self.client.microservice("service", ["toggle"], device_uuid=self.device, service_uuid=self.uuid)["running"]

    def delete(self) -> bool:
        """
        Delete the service.
        :return: True if the service was deleted
        :rtype: bool
        """
        return self.client.microservice("service", ["delete"], device_uuid=self.device, service_uuid=self.uuid)["ok"]


class BruteforceService(Service):
    """Representation of the bruteforce service."""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the bruteforce service
        """
        super(BruteforceService, self).__init__(client, data)


class PortscanService(Service):
    """Representation of the portscan service."""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the portscan service
        """
        super(PortscanService, self).__init__(client, data)

    def scan(self, target_device: str) -> List[Service]:
        """
        Scan a device for running services.
        :param str target_device:
        :return: List with services of the target device
        :rtype: list[Services]
        """
        response: dict = self.client.microservice("service", ["use"], device_uuid=self.device, service_uuid=self.uuid,
                                                  target_device=target_device)["services"]
        return convert_services(self.client, response)


class SSHService(Service):
    """Representation of the ssh service."""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the ssh service
        """
        super(SSHService, self).__init__(client, data)


class TelnetService(Service):
    """Representation of the telnet service."""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the telnet service
        """
        super(TelnetService, self).__init__(client, data)