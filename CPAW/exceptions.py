import json


class InvalidServerResponseError(Exception):
    def __init__(self, response: dict):
        super().__init__("Invalid Server Response: " + json.dumps(response))


class UnknownMicroserviceError(Exception):
    def __init__(self, microservice: str):
        super().__init__("Unknown Microservice: " + microservice)
