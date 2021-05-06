from CPAW.models import Wallet
from tests.test import Test, getenv


class TestWallet(Test):
    def setUp(self) -> None:
        self.wallet: Wallet = Wallet(self.client, eval(getenv("TEST_WALLET")))

