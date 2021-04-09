from CPAW import Client


class BaseModel:
    """The base of all models."""
    def __init__(self, client: Client, data: dict):
        """
        :param Client client: The client used by the user
        :param dict data: The data of the model
        """
        self.client: Client = client
        self._data: dict = data

    @property
    def uuid(self) -> str:
        """
        Return the uuid of the model.
        :return: The uuid
        :rtype: str
        """
        return self._data["uuid"]
