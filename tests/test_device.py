from CPAW.models import Device, File, Hardware, Service
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
