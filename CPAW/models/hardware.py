from CPAW import Client
from CPAW.models import BaseModel


class Hardware(BaseModel):
    """The representation of a hardware part"""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the hardware part
        """
        super().__init__(client, data)

    def __repr__(self) -> str:
        return f"Hardware({self.client}, {self._data})"

    @property
    def device(self) -> str:
        """
        Return the device uuid of the hardware component.
        :return: The device uuid
        :rtype: str
        """
        return self._data["device_uuid"]

    @property
    def name(self) -> str:
        """
        Return the name of the hardware component.
        :return: The name
        :rtype: str
        """
        return self._data["hardware_element"]

    @property
    def type(self) -> str:
        """
        Return the type of the hardware component.
        :return: The type
        :rtype: str
        """
        return self._data["hardware_type"]
