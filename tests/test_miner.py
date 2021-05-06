from unittest.mock import patch

from CPAW.models import Device, Miner, Wallet
from tests.test import Test, getenv


class TestMiner(Test):
    def setUp(self) -> None:
        self.device: Device = Device(self.client, eval(getenv("TEST_DEVICE")))
        self.miner: Miner = self.device.miner

    def test_power(self) -> None:
        self.miner.power = 1.0

        self.assertEqual(self.miner.power, 1.0)

    def test_wallet(self) -> None:
        self.assertIsInstance(self.miner.wallet, Wallet)
        self.miner.wallet = self.miner.wallet

    @patch("CPAW.models.miner.Miner.info")
    def test_info(self, mocked_method) -> None:
        response: dict = self.miner.info()

        self.assertTrue(mocked_method.called)
        self.assertEqual(mocked_method.return_value, response)
