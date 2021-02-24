from CPAW import Client


class File:
    def __init__(self, client: Client, data: dict) -> None:
        self.client: Client = client
        self.uuid: str = data["uuid"]
        self.device: str = data["device"]
        self.filename: str = data["filename"]
        self.content: str = data["content"]
        self.parent_dir_uuid: str = data["parent_dir_uuid"]
        self.is_directory: bool = bool(data["id_directory"])

    def move(self, new_parent_dir_uuid: str, new_filename: str) -> None:
        response: dict = self.client.microservice("device", ["file", "move"], new_parent_dir_uuid=new_parent_dir_uuid,
                                                  new_filename=new_filename)
        self.filename = response["new_filename"]
        self.parent_dir_uuid = response["new_parent_dir_uuid"]

    def update(self, content: str) -> None:
        self.content = self.client.microservice("device", ["file", "update"], device_uuid=self.device, content=content,
                                                file_uuid=self.uuid)["content"]

    def delete(self) -> None:
        self.client.microservice("device", ["file", "delete"], device_uuid=self.device, file_uuid=self.uuid)
