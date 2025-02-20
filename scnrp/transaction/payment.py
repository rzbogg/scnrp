from .base import BaseTxData
from xrpl.utils import drops_to_xrp

class PaymentTxData:
    def __init__(self,base_data:BaseTxData,amount,destination) -> None:
        self.base = base_data
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
        return f'''[Payment][{self.base.status}]
Transaction Hash: {self.base.hash}
From: {self.base.account}
To: {self.destination}
Amount: {self.amount}
Date: {self.base.date}
Fee: {self.base.fee}'''

    @classmethod
    def from_json(cls,json):
        base_data = BaseTxData.from_json(json)
        return cls(
            base_data = base_data,
            amount = json['tx_json']['DeliverMax'],
            destination = json['tx_json']['Destination'],
        )
