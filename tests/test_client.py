from unittest.mock import patch, call

from tests.test import Test


class TestClient(Test):
    def test_login(self) -> None:
        self.client.logout()
        response: str = self.client.login()

        self.assertRegex(response, r"[a-z0-9]{8}(\-[a-z0-9]{4}){3}\-[a-z0-9]{12}")
        self.assertTrue(self.client.logged_in)

    def test_logout(self) -> None:
        self.client.logout()

        self.assertFalse(self.client.logged_in)
        self.assertIsNone(self.client.websocket)

        self.client.login()

    @patch("CPAW.client.Client.request")
    def test_request(self, mocked_method) -> None:
        response: dict = self.client.request({"action": "info"})

        self.assertTrue(mocked_method.called)
        self.assertEqual(
            mocked_method.call_args_list,
            [call({"action": "info"})]
        )
        self.assertEqual(mocked_method.return_value, response)
