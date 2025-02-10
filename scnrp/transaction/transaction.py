from xrpl import account


class Tx():
    def __init__(
        self,
        account :str,
        fee: int,
        hash: str,
    ) -> None:
        self.account = account
        self.fee = fee
        self.hash = hash

    def direction(self,account):
        if account == self.account:
            return 'OUT'
        return "IN"


    def summary(self):
        return f'''Transaction: {self.hash}
Account: {self.account}
Fee: {self.fee}
        '''

    @classmethod
    def from_json(cls,json):
        return cls(
            hash = json['hash'],
            account = json['tx_json']['Account'],
            fee = json['tx_json']['Fee']
        )
