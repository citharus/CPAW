from CPAW.models import File, Device
from CPAW.exceptions import FileAlreadyExistsException
from tests.test import Test, getenv


class TestFile(Test):
    def setUp(self) -> None:
        self.device: Device = Device(self.client, eval(getenv("TEST_DEVICE")))
        self.file: File = self.device.files[0]

    def test_content(self) -> None:
        self.file.content = "Test"

        self.assertEqual(self.file.content, self.file._data["content"])

    def test_filename(self) -> None:
        with self.assertRaises(FileAlreadyExistsException):
            self.file.filename = "Test"
