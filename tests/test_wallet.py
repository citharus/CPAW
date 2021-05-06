from unittest.mock import patch, call

from CPAW.models import Wallet
from tests.test import Test, getenv


class TestWallet(Test):
    def setUp(self) -> None:
        self.wallet: Wallet = Wallet(self.client, eval(getenv("TEST_WALLET")))

    @patch("CPAW.models.wallet.Wallet.info")
    def test_info(self, mocked_method) -> None:
        response: dict = self.wallet.info(self.wallet.key)

        self.assertTrue(mocked_method.called)
        self.assertEqual(
            mocked_method.call_args_list,
            [call(self.wallet.key)]
        )
        self.assertEqual(mocked_method.return_value, response)

    @patch("CPAW.models.wallet.Wallet.amount")
    def test_amount(self, mocked_method) -> None:
        response: float = self.wallet.amount(self.wallet.key)

        self.assertTrue(mocked_method.called)
        self.assertEqual(
            mocked_method.call_args_list,
            [call(self.wallet.key)]
        )
        self.assertEqual(mocked_method.return_value, response)

    @patch("CPAW.models.wallet.Wallet.transactions")
    def test_transactions(self, mocked_method) -> None:
        response: list = self.wallet.transactions(self.wallet.key)

        self.assertTrue(mocked_method.called)
        self.assertEqual(
            mocked_method.call_args_list,
            [call(self.wallet.key)]
        )
        self.assertEqual(mocked_method.return_value, response)
