from .base import BaseTxData
from xrpl.utils import drops_to_xrp

class PaymentTxData(BaseTxData):
    def __init__(
        self,
        hash,
        account,
        destination,
        amount,
        fee,
        date,
        status,
        ledger_index,
    ) -> None:
        super().__init__(
            hash=hash,
            account=account,
            fee=fee,
            date=date,
            status=status,
            ledger_index = ledger_index
        )
        self._amount = amount
        self.destination = destination

    @property
    def amount(self):
        if isinstance(self._amount,int):
            return drops_to_xrp(str(self._amount))
        elif isinstance(self._amount,dict):
            return f"{drops_to_xrp(str(self._amount['value']))}' {self._amount['currency']}"
        else:
            return drops_to_xrp(self._amount)

    def summary(self):
        return f'''Transaction[Payment]: {self.hash}
From: {self.account}
To: {self.destination}
Amount: {self.amount}
Date: {self.date}
Fee: {self.fee}
        '''

    @classmethod
    def from_json(cls,json):
        return cls(
            account =json['tx_json']['Account'],
            fee=json['tx_json']['Fee'],
            hash = json['hash'],
            amount = json['tx_json']['DeliverMax'],
            destination = json['tx_json']['Destination'],
            date = json['tx_json']['date'],
            status = json['validated'],
            ledger_index = json['ledger_index'],
        )
