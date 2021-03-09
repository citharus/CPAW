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

    def exists(self) -> bool:
        """
        Check if the wallet exists.
        :return: True if the wallet exists or False if it doesn't
        :rtype: bool
        """
        return self.client.microservice("currency", ["exists"], source_uuid=self.uuid)["exists"]

    def delete(self, key: Optional[str] = None) -> bool:
        """
        Delete the wallet. If the wallet is not yours the secret key is required.
        :return: True if wallet was deleted
        :rtype: bool
        """
        if key:
            return self.client.microservice("currency", ["delete"], source_uuid=self.uuid, key=key)["ok"]
        return self.client.microservice("currency", ["reset"], source_uuid=self.uuid)["ok"]
