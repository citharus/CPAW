from unittest.mock import patch, call

from CPAW.models import Device, File, Hardware, Service, Wallet, Miner
from tests.test import Test, getenv


class TestDevice(Test):
    def setUp(self) -> None:
        self.device: Device = Device(self.client, eval(getenv("TEST_DEVICE")))

    def test_power(self) -> None:
        response: bool = self.device.power

        self.assertIsInstance(response, bool)

    def test_files(self) -> None:
        response: list[File] = self.device.files

        self.assertIsInstance(response[0], File)

    def test_hardware(self) -> None:
        response: list[Hardware] = self.device.hardware

        self.assertIsInstance(response[0], Hardware)

    def test_services(self) -> None:
        response: list[Service] = self.device.services

        self.assertIsInstance(response[0], Service)

    def test_name(self) -> None:
        self.device.name = "Cuauhtli"

    def test_miner(self) -> None:
        response: Miner = self.device.miner

        self.assertIsInstance(response, Miner)

    @patch("CPAW.models.device.Device.info")
    def test_info(self, mocked_method) -> None:
        response: dict = self.device.info()

        self.assertTrue(mocked_method.called)
        self.assertEqual(mocked_method.return_value, response)

    @patch("CPAW.models.device.Device.restart")
    def test_restart(self, mocked_method) -> None:
        response: bool = self.device.restart()

        self.assertTrue(mocked_method.called)
        self.assertEqual(mocked_method.return_value, response)

    @patch("CPAW.models.device.Device.init")
    def test_init(self, mocked_method) -> None:
        response: bool = self.device.init()

        self.assertTrue(mocked_method.called)
        self.assertEqual(mocked_method.return_value, response)

    @patch("CPAW.models.device.Device.exists")
    def test_exists(self, mocked_method) -> None:
        response: bool = self.device.exists()

        self.assertTrue(mocked_method.called)
        self.assertEqual(mocked_method.return_value, response)

    @patch("CPAW.models.device.Device.part_owner")
    def test_part_owner(self, mocked_method) -> None:
        response: bool = self.device.part_owner()

        self.assertTrue(mocked_method.called)
        self.assertEqual(mocked_method.return_value, response)

    @patch("CPAW.models.device.Device.usage")
    def test_usage(self, mocked_method) -> None:
        response: dict = self.device.usage()

        self.assertTrue(mocked_method.called)
        self.assertEqual(mocked_method.return_value, response)

    @patch("CPAW.models.device.Device.create_file")
    def test_create_file(self, mocked_method) -> None:
        response: File = self.device.create_file("", "", "")

        self.assertTrue(mocked_method.called)
        self.assertEqual(
            mocked_method.call_args_list,
            [call("", "", "")]
        )
        self.assertEqual(mocked_method.return_value, response)

    @patch("CPAW.models.device.Device.create_service")
    def test_create_service(self, mocked_method) -> None:
        response: Service = self.device.create_service("ssh")

        self.assertTrue(mocked_method.called)
        self.assertEqual(
            mocked_method.call_args_list,
            [call("ssh")]
        )
        self.assertEqual(mocked_method.return_value, response)

    @patch("CPAW.models.device.Device.create_miner")
    def test_create_miner(self, mocked_method) -> None:
        response: Miner = self.device.create_miner()

        self.assertTrue(mocked_method.called)
        self.assertEqual(mocked_method.return_value, response)

    @patch("CPAW.models.device.Device.create_wallet")
    def test_create_wallet(self, mocked_method) -> None:
        response: Wallet = self.device.create_wallet()

        self.assertTrue(mocked_method.called)
        self.assertEqual(mocked_method.return_value, response)
