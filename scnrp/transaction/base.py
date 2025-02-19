from xrpl import account
from xrpl.utils import ripple_time_to_datetime,drops_to_xrp

class BaseTxData:
    def __init__(
        self,
        account :str,
        fee: int,
        hash: str,
        status: str,
        date: int,
        ledger_index: int,
    ) -> None:
        self.account = account
        self._fee = fee
        self.hash = hash
        self.status = 'SUCCESS' if status else 'FAIL'
        self._date = date
        self.ledger_index = ledger_index

    def direction(self,account):
        if account == self.account:
            return 'OUT'
        return "IN"

    @property
    def fee(self):
        return drops_to_xrp(str(self._fee))

    @property
    def date(self):
        return ripple_time_to_datetime(self._date)

    def summary(self):
        return f'''Transaction: {self.hash} Outcome: {self.status}
Account: {self.account}
Fee: {self.fee}
Date: {self.date}
Ledger Index: {self.ledger_index}
        '''

    @classmethod
    def from_json(cls,json):
        return cls(
            hash = json['hash'],
            account = json['tx_json']['Account'],
            fee = json['tx_json']['Fee'],
            date = json['tx_json']['date'],
            status = json['validated'],
            ledger_index = json['ledger_index']
        )
