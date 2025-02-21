from .base import BaseTxData


class AccountDeleteTxData:

    def __init__(self,base,destination) -> None:
        self.base = base
        self.destination = destination

    def summary(self):
        result = f'[AccountDelete][{self.base.status}]\n' + self.base.summary() + '\n'
        result += f'Destination: {self.destination}'
        return result

    @classmethod
    def from_json(cls,json):
        base = BaseTxData.from_json(json)
        return cls(
            base = base,
            destination = json['tx_json']['Destination']
        )
