from CPAW import Client


class Wallet:
    def __init__(self, client: Client, data: dict):
        self.client: Client = client
        self.uuid: str = data["source_uuid"]
        self.key: str = data["key"]
        self.owner: str = data["user_uuid"]
