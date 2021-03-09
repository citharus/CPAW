from typing import Optional
from CPAW import Client


class Wallet:
    def __init__(self, client: Client, data: dict) -> None:
        self.client: Client = client
        self.uuid: str = data["source_uuid"]
        self.key: Optional[str] = data["key"]
        self.owner: Optional[str] = data["user_uuid"]

    def amount(self, key: str) -> float:
        return self.client.microservice("currency", ["get"], source_uuid=self.uuid, key=key)["amount"]
