from tests.test import Test


class TestClient(Test):
    def test_login(self) -> None:
        self.client.logout()
        response: str = self.client.login()
        self.assertRegex(response, r"[a-z0-9]{8}(\-[a-z0-9]{4}){3}\-[a-z0-9]{12}")
        self.assertTrue(self.client.logged_in)

    def test_logout(self) -> None:
        self.client.logout()
        print(self.client.logged_in)
        self.assertFalse(self.client.logged_in)
        self.assertIsNone(self.client.websocket)
        self.client.login()
