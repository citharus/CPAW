import unittest
from os import getenv

from dotenv import load_dotenv

from CPAW import Client


class Test(unittest.TestCase):
    client: Client = None
    load_dotenv()
    SERVER: str = getenv("SERVER")
    PASSWORD: str = getenv("PASSWORD")
    USERNAME: str = getenv("USERNAME")

    @classmethod
    def setUpClass(cls) -> None:
        cls.client: Client = Client(cls.SERVER, cls.USERNAME, cls.PASSWORD)
        cls.client.login()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.logout()
