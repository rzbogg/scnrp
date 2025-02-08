from xrpl import account
from xrpl.models.requests import AccountTx, Tx
from api import APIClient

class Transaction:
    def __init__(
        self,
        account:str,
        fee: int,
        date: int,
        hash: str,
        ledger_index: int,
        tx_type:str,
    ) -> None:
        self.account = account
        self.fee = fee
        self.date = date
        self.hash = hash
        self.leger_index = ledger_index
        self.tx_type = tx_type

    @classmethod
    def from_json(cls,json):
        return cls(
            hash=json['hash'],
            ledger_index=json['ledger_index'],
            account=json['tx_json']['Account'],
            fee=json['tx_json']['Fee'],
            date=json['tx_json']['date'],
            tx_type=json['tx_json']['TransactionType'],
        )

    def __repr__(self) -> str:
        return f'''Transaction #{self.hash}
From: {self.account}
Fee: {self.fee}
Date: {self.date}
Type: {self.tx_type}
Ledger: {self.leger_index}'''

def get_tx(hash:str):
    tx_req = Tx(transaction=hash)
    tx_res = APIClient.request(tx_req)
    return Transaction.from_json(tx_res.result)


def get_account_txs(account:str):
    tx_req = AccountTx(account=account)
    tx_res = APIClient.request(tx_req)
    result = []
    for tx_json in tx_res.result['transactions']:
        result.append(Transaction.from_json(tx_json))
    return result
