from xrpl.models.requests import AccountInfo,AccountTx
from xrpl.models.response import Response, ResponseStatus
from api import APIClient

class Account:
    def __init__(
        self,
        address,
        data ,
    ) -> None:
        self.address = address
        self._data = data

    @classmethod
    def from_json(cls,json):
        return cls(
            address= json['account_data']['Account'],
            data = json['account_data']
        )

    def __repr__(self) -> str:
        return f'Account({self.address})'

    def fields(self):
        return self._data.items()


def get_account(account:str):
    req_account = AccountInfo(account=account)
    res_account = APIClient.request(req_account)
    if res_account.status == ResponseStatus.ERROR:
        raise ValueError('unable to get account')
    return Account.from_json(res_account.result)
