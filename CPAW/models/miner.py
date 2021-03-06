from CPAW import Client
from CPAW.models.service import Service
from CPAW.models.wallet import Wallet


class Miner(Service):
    """The representation of the Miner service."""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the Miner service
        """
        super(Miner, self).__init__(client, data)

    @property
    def power(self) -> float:
        """
        Get the power allocated to the miner.
        :return: The power of the miner
        :rtype: float
        """
        return self.client.microservice("service", ["miner", "get"], service_uuid=self.uuid)["power"]

    @power.setter
    def power(self, power: float) -> None:
        """
        Change the computing power allocated to the miner.
        :param float power: The new computing power
        """
        self.client.microservice("service", ["miner", "power"], service_uuid=self.uuid, power=power)

    @property
    def wallet(self) -> Wallet:
        """
        Return the current wallet the miner is connected to.
        :return: The wallet uuid
        :rtype: str
        """
        data: dict = self.client.microservice("service", ["miner", "get"], service_uuid=self.uuid)["wallet"]
        return Wallet(self.client, {"source_uuid": data})

    @wallet.setter
    def wallet(self, wallet: Wallet) -> None:
        """
        Update the wallet the miner transfers the coins to.
        :param Wallet wallet: The new wallet
        """
        self.client.microservice("service", ["miner", "wallet"], service_uuid=self.uuid, wallet_uuid=wallet.uuid)

    def info(self) -> dict:
        """
        Return information about the miner in a dictionary.
        :return: Dictionary containing information
        :rtype: dict
        """
        return self.client.microservice("service", ["miner", "get"], service_uuid=self.uuid)
