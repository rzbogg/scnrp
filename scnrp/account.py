from xrpl.models.requests import AccountInfo,AccountTx
from api import APIClient

class Account:
    def __init__(
        self,
        address,
        balance: int = 0,
    ) -> None:
        self.address = address
        self.balance = balance

    @classmethod
    def from_json(cls,json):
        return cls(
            address= json['account_data']['Account'],
            balance= json['account_data']['Balance']
        )

    def __repr__(self) -> str:
        return f'Account({self.address},{self.balance})'

def get_account(account:str):
    req_account = AccountInfo(account=account)
    res_account = APIClient.request(req_account)
    return Account.from_json(res_account.result)
