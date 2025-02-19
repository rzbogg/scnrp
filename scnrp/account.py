from xrpl.models.requests import AccountInfo
from xrpl.models.response import ResponseStatus
from xrpl.utils import drops_to_xrp

from . import api
from .transaction import get_account_txs

class AccountData:
    def __init__(
        self,
        address:str,
        last_tx:str,
        balance:int,
        next_seq:int,
        txs = [],
    ) -> None:
        self.address = address
        self.last_tx = last_tx
        self._balance = balance
        self.next_seq = next_seq
        self.txs = txs

    @property
    def balance(self):
        return drops_to_xrp(str(self._balance))

    @property
    def activated_by(self):
        return self.txs[-1].account

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
Next Sequence: {self.next_seq}
Activated By: {self.activated_by}'''
    def flag_summary(self,address,balance,last_tx,txs):
        result = ''
        if address:
            result += f'Address: {self.address}\n'
        if balance:
            result += f'Balance: {self.balance}\n'
        if last_tx:
            result += f'{self.txs[0].summary()}\n'
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
            next_seq = json['Sequence']
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
