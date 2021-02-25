from typing import Dict, Tuple, Union

from CPAW import Client


class File:
    """The representation of a File."""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the file
        """
        self.client: Client = client
        self.uuid: str = data["uuid"]
        self.device: str = data["device"]
        self.filename: str = data["filename"]
        self.content: str = data["content"]
        self.parent_dir_uuid: str = data["parent_dir_uuid"]
        self.is_directory: bool = bool(data["id_directory"])

    def info(self) -> Dict[str, Union[str, bool]]:
        """
        Return information about the file.
        :return: Dictionary containing information
        :rtype: dict
        """
        return self.client.microservice("device", ["file", "info"], device_uuid=self.device, file_uuid=self.uuid)

    def move(self, new_parent_dir_uuid: str, new_filename: str) -> Tuple[str, str]:
        """
        Move or rename a file to another location.
        :param str new_parent_dir_uuid: The new directory of the file
        :param str new_filename: The new file name
        """
        response: dict = self.client.microservice("device", ["file", "move"], new_parent_dir_uuid=new_parent_dir_uuid,
                                                  new_filename=new_filename)
        self.filename = response["new_filename"]
        self.parent_dir_uuid = response["new_parent_dir_uuid"]
        return self.filename, self.parent_dir_uuid

    def update(self, content: str) -> str:
        """
        Update the content of a file.
        :param str content: The new content of the file
        :return: File content
        :rtype: str
        """
        self.content = self.client.microservice("device", ["file", "update"], device_uuid=self.device, content=content,
                                                file_uuid=self.uuid)["content"]
        return self.content

    def delete(self) -> bool:
        """
        Delete the file
        :return: True if the file was deleted
        :rtype: bool
        """
        return self.client.microservice("device", ["file", "delete"], device_uuid=self.device, file_uuid=self.uuid)["ok"]
