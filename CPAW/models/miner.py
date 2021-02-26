from CPAW import Client
from CPAW.models import Service


class Miner(Service):
    """The representation of the Miner service."""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the Miner service
        """
        super(Miner, self).__init__(client, data)
        self.wallet: str = data["wallet"]
        self.power: int = int(data["power"])
