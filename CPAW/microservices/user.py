from typing import List

from CPAW import Client
from CPAW.microservices import Device


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
