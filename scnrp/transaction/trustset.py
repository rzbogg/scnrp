from .base import BaseTxData

class TrustSetTxData:
    def __init__(self,base_data: BaseTxData,limit_amount) -> None:
        self.base = base_data
        self.limit_amount = limit_amount


    def summary(self):
        return f'''[TRUSTSET][{self.base.status}]
Transaction Hash: {self.base.hash}
Date: {self.base.date}
Source: {self.base.account}
Ledger: {self.base.ledger_index}
Fee: {self.base.fee}
Limit Amount:
    Currency: {self.limit_amount['currency']}
    Issuer: {self.limit_amount['issuer']}
    Value: {self.limit_amount['value']}'''

    @classmethod
    def from_json(cls,json):
        base = BaseTxData.from_json(json)
        return cls(
            base_data = base,
            limit_amount = json['tx_json']['LimitAmount'],
        )
