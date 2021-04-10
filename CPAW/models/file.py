from typing import Dict, Union

from CPAW import Client
from CPAW.models import BaseModel


class File(BaseModel):
    """The representation of a File."""

    def __init__(self, client: Client, data: dict) -> None:
        """
        :param Client client: The client used by the user
        :param dict data: The data of the file
        """
        super().__init__(client, data)

    @property
    def device(self) -> str:
        """
        Return the device uuid from the host device.
        :return: The uuid of the device
        :rtype: str
        """
        return self._data["device"]

    @property
    def directory(self) -> str:
        """
        Return the directory uuid of the parent directory.
        :return: The directory uuid
        :rtype: str
        """
        return self._data["parent_dir_uuid"]

    @directory.setter
    def directory(self, new_parent_directory: str) -> None:
        """
        Update the directory to the new parent directory.
        :param str new_parent_directory: The new directory of the file
        """
        self._data["parent_dir_uuid"] = new_parent_directory

    @property
    def is_directory(self) -> bool:
        """
        Return if the file is a directory.
        :return: True or False
        :rtype: bool
        """
        return self._data["is_directory"]

    @property
    def content(self) -> str:
        """
        Return the content of the file.
        :return: File content
        :rtype: str
        """
        return self._data["content"]

    @content.setter
    def content(self, content: str) -> None:
        """
        Update the content of the file.
        :param str content: The new content of the file
        """
        self._data["content"] = self.client.microservice("device", ["file", "update"], device_uuid=self.device,
                                                         content=content, file_uuid=self.uuid)["content"]

    @property
    def filename(self) -> str:
        """
        Return the filename of the file
        :return: The name
        :rtype: str
        """
        return self._data["filename"]

    @filename.setter
    def filename(self, new_filename: str) -> None:
        """
        Set a new filename for the file
        :param str new_filename: The new name
        """
        self._data["filename"] = self.client.microservice("device", ["file", "move"], device_uuid=self.device,
                                                          file_uuid=self.uuid, new_parent_dir_uuid=self.directory,
                                                          new_filename=new_filename)["filename"]

    def info(self) -> Dict[str, Union[str, bool]]:
        """
        Return information about the file.
        :return: Dictionary containing information
        :rtype: dict
        """
        return self.client.microservice("device", ["file", "info"], device_uuid=self.device, file_uuid=self.uuid)

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
