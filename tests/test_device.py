from CPAW.models import Device
from tests.test import Test, getenv


class TestDevice(Test):
    def setUp(self) -> None:
        self.device: Device = Device(self.client, {'uuid': getenv("TEST_DEVICE_UUID"),
                                                   'name': getenv("TEST_DEVICE_NAME"), 'starter_device': True})
