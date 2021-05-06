from CPAW import Client
from CPAW.models import BaseModel


class Transaction(BaseModel):
    """The representation af an transaction"""
    def __init__(self, client: Client, data: dict):
        """
        :param Client client: The client used by the user
        :param dict data: The data of the device
        """
        super().__init__(client, data)
