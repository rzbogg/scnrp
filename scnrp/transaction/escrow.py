from .base import BaseTxData
from xrpl.utils import drops_to_xrp, ripple_time_to_datetime

class EscrowCreateTxData:
    def __init__(self, base_data: BaseTxData, amount, destination, condition=None, cancel_after=None, finish_after=None) -> None:
        self.base = base_data
        self._amount = amount
        self.destination = destination
        self.condition = condition
        self._cancel_after = cancel_after
        self._finish_after = finish_after

    @property
    def amount(self):
        if isinstance(self._amount, dict):
            return f"{str(self._amount['value'])} {self._amount['currency']}"
        return f'{drops_to_xrp(str(self._amount))} XRP'

    @property
    def cancel_after(self):
        if self._cancel_after:
            return ripple_time_to_datetime(self._cancel_after)
        return None

    @property
    def finish_after(self):
        if self._finish_after:
            return ripple_time_to_datetime(self._finish_after)
        return None

    def summary(self):
        summary = f'''[Escrow][{self.base.status}]
Transaction Hash: {self.base.hash}
From: {self.base.account}
To: {self.destination}
Amount: {self.amount}
Date: {self.base.date}
Fee: {self.base.fee}'''
        if self.condition:
            summary += f'\nCondition: {self.condition}'
        if self.cancel_after:
            summary += f'\nCancel After: {self.cancel_after}'
        if self.finish_after:
            summary += f'\nFinish After: {self.finish_after}'
        return summary

    @classmethod
    def from_json(cls, json):
        base_data = BaseTxData.from_json(json)
        return cls(
            base_data=base_data,
            amount=json['tx_json']['Amount'],
            destination=json['tx_json']['Destination'],
            condition=json['tx_json'].get('Condition'),
            cancel_after=json['tx_json'].get('CancelAfter'),
            finish_after=json['tx_json'].get('FinishAfter'),
        )
