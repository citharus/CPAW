from typing import Dict, Union

from CPAW import Client


class File:
    """The representation of a File."""
    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the file
        """
        self.client: Client = client
        self._data: dict = data
        self.uuid: str = data["uuid"]
        self.device: str = data["device"]
        self.filename: str = data["filename"]
        self.content: str = data["content"]
        self.directory: str = data["parent_dir_uuid"]
        self.is_directory: bool = bool(data["is_directory"])

    def info(self) -> Dict[str, Union[str, bool]]:
        """
        Return information about the file.
        :return: Dictionary containing information
        :rtype: dict
        """
        return self.client.microservice("device", ["file", "info"], device_uuid=self.device, file_uuid=self.uuid)

    @property
    def content(self) -> str:
        """
        Return the content of the file.
        :return: File content
        :rtype: str
        """
        return self.content

    @content.setter
    def content(self, content: str) -> None:
        """
        Update the content of the file.
        :param str content: The new content of the file
        """
        self.content = self.client.microservice("device", ["file", "update"], device_uuid=self.device, content=content,
                                                file_uuid=self.uuid)["content"]

    @property
    def filename(self) -> str:
        """
        Return the filename of the file
        :return: The name
        :rtype: str
        """
        return self.filename

    @filename.setter
    def filename(self, new_filename: str) -> None:
        """
        Sets a new filename for the file
        :param str new_filename: The new name
        """
        self.client.microservice("device", ["file", "move"], device_uuid=self.device, file_uuid=self.uuid,
                                 new_parent_dir_uuid=self.directory, new_filename=new_filename)

    def move(self, new_directory: str) -> str:
        """
        Move the file to a new directory.
        :param str new_directory: The new directory
        :return: The new directory
        :rtype: str
        """
        response: dict = self.client.microservice("device", ["file", "move"], device_uuid=self.device,
                                                  file_uuid=self.uuid, new_parent_dir_uuid=new_directory,
                                                  new_filename=self.filename)
        self.directory = response["parent_dir_uuid"]
        return self.directory

    def delete(self) -> bool:
        """
        Delete the file
        :return: True if the file was deleted
        :rtype: bool
        """
        return self.client.microservice("device", ["file", "delete"], device_uuid=self.device, file_uuid=self.uuid)["ok"]
