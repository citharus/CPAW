from CPAW import Client
from CPAW.models import Service


class Miner(Service):
    def __init__(self, client: Client, data: dict) -> None:
        super(Miner, self).__init__(client, data)
        self.wallet: str = data["wallet"]
        self.power: int = int(data["power"])
