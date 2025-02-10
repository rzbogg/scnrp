from .transaction import Tx

class PaymentTx(Tx):
    def __init__(
        self,
        hash,
        account,
        destination,
        amount,
        fee,
    ) -> None:
        super().__init__(hash=hash,account=account,fee=fee)
        self.amount = amount
        self.destination = destination

    def summary(self):
        return f'''Transaction: {self.hash}
From: {self.account}
To: {self.destination}
        '''

    @classmethod
    def from_json(cls,json):
        return cls(
            account =json['tx_json']['Account'],
            fee=json['tx_json']['Fee'],
            hash = json['hash'],
            amount = json['tx_json']['DeliverMax'],
            destination = json['tx_json']['Destination']
        )
