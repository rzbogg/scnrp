from .base import BaseTxData
from xrpl.utils import drops_to_xrp

class NFTTokenCreateOfferTxData:
    def __init__(self, base_data: BaseTxData, nftoken_id: str, amount, destination: str = None, owner: str = None) -> None:
        self.base = base_data
        self.nftoken_id = nftoken_id
        self._amount = amount
        self.destination = destination
        self.owner = owner

    @property
    def amount(self):
        if isinstance(self._amount, dict):
            return f"{str(self._amount['value'])} {self._amount['currency']}"
        return f'{drops_to_xrp(str(self._amount))} XRP'

    def summary(self):
        summary = f'''[NFTTokenCreateOffer][{self.base.status}]
Transaction Hash: {self.base.hash}
From: {self.base.account}
NFT Token ID: {self.nftoken_id}
Amount: {self.amount}
Date: {self.base.date}
Fee: {self.base.fee}'''
        if self.destination:
            summary += f'\nDestination: {self.destination}'
        if self.owner:
            summary += f'\nOwner: {self.owner}'
        return summary

    @classmethod
    def from_json(cls, json):
        base_data = BaseTxData.from_json(json)
        return cls(
            base_data=base_data,
            nftoken_id=json['tx_json']['NFTokenID'],
            amount=json['tx_json']['Amount'],
            destination=json['tx_json'].get('Destination'),
            owner=json['tx_json'].get('Owner'),
        )

class NFTTokenCancelOfferTxData:
    def __init__(self, base_data: BaseTxData, nftoken_offers: list) -> None:
        self.base = base_data
        self.nftoken_offers = nftoken_offers

    def summary(self):
        summary = f'''[NFTCancelOffer][{self.base.status}]
Transaction Hash: {self.base.hash}
From: {self.base.account}
NFT Token Offers: {", ".join(self.nftoken_offers)}
Date: {self.base.date}
Fee: {self.base.fee}'''
        return summary

    @classmethod
    def from_json(cls, json):
        base_data = BaseTxData.from_json(json)
        return cls(
            base_data=base_data,
            nftoken_offers=json['tx_json']['NFTokenOffers'],
        )

class NFTTokenBurnTxData:
    def __init__(self, base_data: BaseTxData, nftoken_id: str) -> None:
        self.base = base_data
        self.nftoken_id = nftoken_id

    def summary(self):
        summary = f'''[NFTTokenBurn][{self.base.status}]
Transaction Hash: {self.base.hash}
From: {self.base.account}
NFT Token ID: {self.nftoken_id}
Date: {self.base.date}
Fee: {self.base.fee}'''
        return summary

    @classmethod
    def from_json(cls, json):
        base_data = BaseTxData.from_json(json)
        return cls(
            base_data=base_data,
            nftoken_id=json['tx_json']['NFTokenID'],
        )


class NFTTokenAcceptOfferTxData:
    def __init__(self, base_data: BaseTxData, nftoken_buy_offer: str = None, nftoken_sell_offer: str = None, nftoken_broker_fee: str = None) -> None:
        self.base = base_data
        self.nftoken_buy_offer = nftoken_buy_offer
        self.nftoken_sell_offer = nftoken_sell_offer
        self.nftoken_broker_fee = nftoken_broker_fee

    def summary(self):
        summary = f'''[NFTTokenAcceptOffer][{self.base.status}]
Transaction Hash: {self.base.hash}
From: {self.base.account}
Date: {self.base.date}
Fee: {self.base.fee}'''
        if self.nftoken_buy_offer:
            summary += f'\nNFT Token Buy Offer: {self.nftoken_buy_offer}'
        if self.nftoken_sell_offer:
            summary += f'\nNFT Token Sell Offer: {self.nftoken_sell_offer}'
        if self.nftoken_broker_fee:
            summary += f'\nNFT Token Broker Fee: {self.nftoken_broker_fee}'
        return summary

    @classmethod
    def from_json(cls, json):
        base_data = BaseTxData.from_json(json)
        return cls(
            base_data=base_data,
            nftoken_buy_offer=json['tx_json'].get('NFTokenBuyOffer'),
            nftoken_sell_offer=json['tx_json'].get('NFTokenSellOffer'),
            nftoken_broker_fee=json['tx_json'].get('NFTokenBrokerFee'),
        )
