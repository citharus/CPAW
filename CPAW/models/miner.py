from CPAW import Client
from CPAW.models.service import Service


class Miner(Service):
    """The representation of the Miner service."""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the Miner service
        """
        super(Miner, self).__init__(client, data)
        self._data: dict = data

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
    def wallet(self) -> str:
        """
        Return the current wallet the miner is connected to.
        :return: The wallet uuid
        :rtype: str
        """
        return self.client.microservice("service", ["miner", "get"], service_uuid=self.uuid)["wallet"]

    def info(self) -> dict:
        """
        Return information about the miner in a dictionary.
        :return: Dictionary containing information
        :rtype: dict
        """
        return self.client.microservice("service", ["miner", "get"], service_uuid=self.uuid)
