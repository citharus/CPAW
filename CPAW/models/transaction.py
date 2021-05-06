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

    @property
    def id(self) -> int:
        """
        Return the id of the transaction.
        :return: The id
        """
        return int(self._data["id"])

    @property
    def sender(self) -> str:
        """
        Return the wallet the transaction originated from.
        :return: The wallet uuid of the sender
        """
        return self._data["source_uuid"]

    @property
    def amount(self) -> float:
        """
        Return the transaction amount of coins.
        :return: The amount
        """
        return self._data["send_amount"]

    @property
    def receiver(self) -> str:
        """
        Return the wallet that received the transaction.
        :return: The receiver wallet
        """
        return self._data["destination_uuid"]

    @property
    def usage(self) -> str:
        """
        Return the usage message of the transaction
        :return: The description
        """
        return self._data["usage"]
