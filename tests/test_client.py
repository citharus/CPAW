from unittest.mock import patch, call

from tests.test import Test


class TestClient(Test):
    @patch("CPAW.client.Client.request")
    def test_request(self, mocked_method) -> None:
        response: dict = self.client.request({"action": "info"})

        self.assertTrue(mocked_method.called)
        self.assertEqual(
            mocked_method.call_args_list,
            [call({"action": "info"})]
        )
        self.assertEqual(mocked_method.return_value, response)

    @patch("CPAW.client.Client.microservice")
    def test_microservice(self, mocked_method) -> None:
        response: dict = self.client.microservice("device", ["spot"])

        self.assertTrue(mocked_method.called)
        self.assertEqual(
            mocked_method.call_args_list,
            [call("device", ["spot"])]
        )
        self.assertEqual(mocked_method.return_value, response)
