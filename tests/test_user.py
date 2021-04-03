from unittest.mock import patch, call
from CPAW.models import User, Service, Device, Wallet
from tests.test import Test


class TestUser(Test):
    user: User = None

    def setUp(self) -> None:
        self.user = User(self.client)

    def test_attributes(self) -> None:
        self.assertEqual(self.user.name, "citharus")
        self.assertRegex(self.user.uuid, r"^[\w\d]{8}(-[\w\d]{4}){3}-[\w\d]{12}$")

    def test_part_owner(self) -> None:
        response: list = self.user.part_owner

        self.assertIsInstance(response[0], Service)

    def test_devices(self) -> None:
        response: list = self.user.devices

        self.assertIsInstance(response[0], Device)

    def test_wallets(self) -> None:
        response: list = self.user.wallets

        self.assertIsInstance(response[0], Wallet)

    @patch("CPAW.models.user.User.spot")
    def test_spot(self, mocked_method) -> None:
        response: Device = self.user.spot()

        self.assertTrue(mocked_method.called)
        self.assertEqual(mocked_method.return_value, response)
