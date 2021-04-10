from typing import Dict, Union, List

from CPAW import Client
from CPAW.models import BaseModel
from CPAW.utils import convert_services


class Service(BaseModel):
    """Representation of the service base class."""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the service
        """
        super().__init__(client, data)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.client}, {self.__data})"

    @property
    def name(self) -> str:
        """
        Return the name of the service.
        :return: The name
        :rtype: str
        """
        return self.__data["name"]

    @property
    def owner(self) -> str:
        """
        Return the owner of the service.
        :return: The owner
        :rtype: str
        """
        return self.__data["owner"]

    @property
    def device(self) -> str:
        """
        Return the device uuid of the service.
        :return: The device uuid
        :rtype: str
        """
        return self.__data["device"]

    @property
    def port(self) -> int:
        """
        Return the port of the service.
        :return: The port
        :rtype: int
        """
        return self.__data["running_port"]

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

    def scale(self, cpu: int, ram: int, gpu: int, disk: int, network: int) -> bool:
        """
        Scale a service to only use the assigned hardware resources.
        :param int cpu: Given cpu resources
        :param int ram: Given ram resources
        :param int gpu: Given gpu resources
        :param int disk: Given disk resources
        :param int network: Given network resources
        :return: True if services was scaled
        :rtype: bool
        """
        return self.client.microservice("device", ["hardware", "scale"], device_uuid=self.device, service_uuid=self.uuid,
                                        user=self.owner, cpu=cpu, ram=ram, gpu=gpu, disk=disk, network=network)["ok"]

    def stop(self) -> bool:
        """
        Stop the service and scale all other services accordingly.
        :return: True if the service was stopped
        :rtype: bool
        """
        return self.client.microservice("device", ["hardware", "stop"], device_uuid=self.device, service_uuid=self.uuid,
                                        user=self.owner)["ok"]


class BruteforceService(Service):
    """Representation of the bruteforce service."""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the bruteforce service
        """
        super(BruteforceService, self).__init__(client, data)

    def attack(self, target_service: Service) -> bool:
        """
        Start a bruteforce attack against the target service.
        :param Service target_service: The service to hack
        :return: True if attack has started
        :rtype: bool
        """
        return self.client.microservice("service", ["bruteforce", "attack"], device_uuid=self.device,
                                        service_uuid=self.uuid, target_device=target_service.device,
                                        target_service=target_service.uuid)["ok"]

    def status(self) -> int:
        """
        Return the progress of the running bruteforce attack.
        :return: Progress
        :rtype: int
        """
        return self.client.microservice("service", ["bruteforce", "status"], device_uuid=self.device,
                                        service_uuid=self.uuid)["progress"]

    def stop_attack(self) -> bool:
        """
        Stop the running bruteforce attack.
        :return: If user has access to the device
        :rtype: bool
        """
        return self.client.microservice("service", ["bruteforce", "stop"], device_uuid=self.device,
                                        service_uuid=self.uuid)["access"]


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
