from unittest.mock import patch, call

from CPAW.exceptions import FileAlreadyExistsException
from CPAW.models import File, Device
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

    @patch("CPAW.models.file.File.info")
    def test_info(self, mocked_method) -> None:
        response: dict = self.file.info()

        self.assertTrue(mocked_method.called)
        self.assertEqual(mocked_method.return_value, response)

    @patch("CPAW.models.file.File.move")
    def test_move(self, mocked_method) -> None:
        response: str = self.file.move("")

        self.assertTrue(mocked_method.called)
        self.assertEqual(
            mocked_method.call_args_list,
            [call("")]
        )
        self.assertEqual(mocked_method.return_value, response)
