from unittest.mock import patch

from CPAW.models import Device, Miner
from tests.test import Test, getenv


class TestMiner(Test):
    def setUp(self) -> None:
        self.device: Device = Device(self.client, eval(getenv("TEST_DEVICE")))
        self.miner: Miner = self.device.miner

    def test_power(self) -> None:
        self.miner.power = 1.0

        self.assertEqual(self.miner.power, 1.0)
