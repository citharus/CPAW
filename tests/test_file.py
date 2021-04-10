from CPAW.models import File, Device
from tests.test import Test, getenv
from random import randint


class TestFile(Test):
    def setUp(self) -> None:
        self.device: Device = Device(self.client, eval(getenv("TEST_DEVICE")))
        self.file: File = self.device.files[0]

    def test_content(self) -> None:
        self.file.content = "Test"

        self.assertEqual(self.file.content, self.file._data["content"])

    def test_filename(self) -> None:
        random = randint(1, 1000000)
        self.file.filename = str(random)

        self.assertEqual(self.file.filename, self.file._data["filename"])
