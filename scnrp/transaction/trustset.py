from .transaction import Tx

class TrustSetTx(Tx):
    def __init__(
        self,
        account: str,
        fee: int,
        hash: str,
        limit_amount,
    ) -> None:
        super().__init__(account, fee, hash)
        self.limit_amount = limit_amount
