from CPAW import Client


class Service:
    def __init__(self, client: Client, data: dict) -> None:
        self.client: Client = client
        self.uuid: str = data["uuid"]
        self.name: str = data["name"]
        self.owner: str = data["owner"]
        self.running_port: int = int(data["running_port"])
        self.device: str = data["device"]
        self.speed: int = int(data["speed"])


class BruteforceService(Service):
    def __init__(self, client: Client, data: dict) -> None:
        super(BruteforceService, self).__init__(client, data)


class PortscanService(Service):
    def __init__(self, client: Client, data: dict) -> None:
        super(PortscanService, self).__init__(client, data)


class SSHService(Service):
    def __init__(self, client: Client, data: dict) -> None:
        super(SSHService, self).__init__(client, data)


class TelnetService(Service):
    def __init__(self, client: Client, data: dict) -> None:
        super(TelnetService, self).__init__(client, data)