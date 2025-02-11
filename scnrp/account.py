from xrpl.models.requests import AccountInfo
from xrpl.models.response import ResponseStatus
from . import api
from .transaction import get_account_txs

class AccountData:
    def __init__(
        self,
        address:str,
        last_tx:str,
        balance:int,
        txs = [],
    ) -> None:
        self.address = address
        self.last_tx = last_tx
        self.balance = balance
        self.txs = txs

    def _txs_summary(self):
        result = '\n---------\n'
        for tx in self.txs:
            result += f'{tx.direction(self.address)}\n'
            result += tx.summary()
            result += '\n---------\n'
        return result

    def summary(self):
        return f'''Address: {self.address}
Balance: {self.balance}
Last transaction: {self.last_tx}
{self._txs_summary()}
'''
    def flag_summary(self,address,balance,last_tx,txs):
        result = ''
        if address:
            result += f'Address: {self.address}\n'
        if balance:
            result += f'Balance: {self.balance}\n'
        if last_tx:
            result += f'Last Transaction: {self.last_tx}\n'
        if txs:
            result += f'Transactions:{self._txs_summary()}'
        assert result != ''
        return result

    def add_tx(self,tx):
        self.txs.append(tx)

    @classmethod
    def from_json(cls,json):
        return cls(
            address = json['Account'],
            balance = json['Balance'],
            last_tx = json['PreviousTxnID'],
        )


def get_account(account:str):
    req_account = AccountInfo(account=account)
    res_account = api.APIClient.request(req_account)
    if res_account.status == ResponseStatus.ERROR:
        raise ValueError('unable to get account')
    account_data = AccountData.from_json(res_account.result['account_data'])
    for tx in get_account_txs(account):
        account_data.add_tx(tx)

    return account_data
