from .base import BaseTxData
from xrpl.utils import drops_to_xrp

class OfferCreateTxData:
    def __init__(self, base_data: BaseTxData, taker_pays, taker_gets, expiration=None, offer_sequence=None) -> None:
        self.base = base_data
        self._taker_pays = taker_pays
        self._taker_gets = taker_gets
        self.expiration = expiration
        self.offer_sequence = offer_sequence

    @property
    def taker_pays(self):
        if isinstance(self._taker_pays, dict):
            return f"{str(self._taker_pays['value'])} {self._taker_pays['currency']}"
        return f'{drops_to_xrp(str(self._taker_pays))} XRP'

    @property
    def taker_gets(self):
        if isinstance(self._taker_gets, dict):
            return f"{str(self._taker_gets['value'])} {self._taker_gets['currency']}"
        return f'{drops_to_xrp(str(self._taker_gets))} XRP'

    def summary(self):
        summary = f'''[OfferCreate][{self.base.status}]
Transaction Hash: {self.base.hash}
From: {self.base.account}
Taker Pays: {self.taker_pays}
Taker Gets: {self.taker_gets}
Date: {self.base.date}
Fee: {self.base.fee}'''
        if self.expiration:
            summary += f'\nExpiration: {self.expiration}'
        if self.offer_sequence:
            summary += f'\nOffer Sequence: {self.offer_sequence}'
        return summary

    @classmethod
    def from_json(cls, json):
        base_data = BaseTxData.from_json(json)
        return cls(
            base_data=base_data,
            taker_pays=json['tx_json']['TakerPays'],
            taker_gets=json['tx_json']['TakerGets'],
            expiration=json['tx_json'].get('Expiration'),
            offer_sequence=json['tx_json'].get('OfferSequence'),
        )

class OfferCancelTxData:
    def __init__(self, base_data: BaseTxData, offer_sequence) -> None:
        self.base = base_data
        self.offer_sequence = offer_sequence

    def summary(self):
        summary = f'''[OfferCancel][{self.base.status}]
Transaction Hash: {self.base.hash}
From: {self.base.account}
Offer Sequence: {self.offer_sequence}
Date: {self.base.date}
Fee: {self.base.fee}'''
        return summary

    @classmethod
    def from_json(cls, json):
        base_data = BaseTxData.from_json(json)
        return cls(
            base_data=base_data,
            offer_sequence=json['tx_json']['OfferSequence'],
        )
