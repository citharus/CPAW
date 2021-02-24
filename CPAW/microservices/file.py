from CPAW import Client


class File:
    def __init__(self, client: Client, data: dict) -> None:
        self.microservice = client.microservice
        self.uuid: str = data["uuid"]
        self.device: str = data["device"]
        self.filename: str = data["filename"]
        self.content: str = data["content"]
        self.parent_dir_uuid: str = data["parent_dir_uuid"]
        self.is_directory: bool = bool(data["id_directory"])
