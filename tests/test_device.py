from CPAW.models import Device, File, Hardware, Service
from tests.test import Test, getenv
from unittest.mock import patch, call


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
