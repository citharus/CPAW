from typing import Optional, Dict, Union

from CPAW import Client
from CPAW.exceptions import NoWalletKeyException
from CPAW.models import BaseModel


class Wallet(BaseModel):
    def __init__(self, client: Client, data: dict) -> None:
        super().__init__(client, data)

    @property
    def uuid(self) -> str:
        """
        Return the uuid of the wallet.
        :return: The uuid
        :rtype: str
        """
        return self._data["source_uuid"]

    @property
    def key(self) -> str:
        """
        Return the secure key of the wallet.
        :return: The key of the wallet
        :rtype: str
        """
        try:
            return self._data["key"]
        except KeyError:
            raise NoWalletKeyException

    @key.setter
    def key(self, key: str) -> None:
        """
        Set or update the secure key of the wallet.
        :param str key: The secure key
        """
        self._data["key"] = key

    def info(self, key: str) -> Dict[str, Union[str, float]]:
        """
        Return information about the wallet in a dictionary.
        :param key:
        :return: Dictionary containing information
        :rtype: dict
        """
        return self.client.microservice("currency", ["get"], source_uuid=self.uuid, key=key)

    def amount(self, key: str) -> float:
        """
        Return the current amount of morphcoins in the wallet.
        :param str key: The secure key of the wallet
        :return: The current amount of morphcoins
        :rtype: float
        """
        return self.client.microservice("currency", ["get"], source_uuid=self.uuid, key=key)["amount"]

    def delete(self, key: Optional[str] = None) -> bool:
        """
        Delete the wallet. If the wallet is not yours the secret key is required.
        :param str key: The secure key of the wallet
        :return: True if wallet was deleted
        :rtype: bool
        """
        if key:
            return self.client.microservice("currency", ["delete"], source_uuid=self.uuid, key=key or self.key)["ok"]
        return self.client.microservice("currency", ["reset"], source_uuid=self.uuid)["ok"]

    def send(self, wallet: "Wallet", amount: float, usage: Optional[str] = None, key: Optional[str] = None) -> bool:
        """
        Send the specified amount of coins to the specified wallet.
        :param str key: The secure key of the wallet
        :param Wallet wallet: The wallet which receives the coins
        :param float amount: The amount of coins to send
        :param str usage: The description of the transaction
        :return: True if the transaction was successful
        :rtype: bool
        """
        return self.client.microservice("currency", ["send"], source_uuid=self.uuid, key=key or self.key, usage=usage,
                                        send_amount=amount, destionation_uuid=wallet.uuid)["ok"]
