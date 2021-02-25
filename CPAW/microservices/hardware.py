from CPAW import Client


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
