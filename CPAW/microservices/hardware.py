from CPAW import Client


class Hardware:
    def __init__(self, client: Client, data: dict):
        self.client: Client = client
        self.uuid: str = data["uuid"]
        self.device: str = data["device_uuid"]
        self.hardware_element: str = data["hardware_element"]
        self.hardware_type: str = data["hardware_type"]
