from xrpl.models.requests import Tx, AccountTx
from xrpl.models.response import ResponseStatus

from .nft import (
    NFTTokenCreateOfferTxData,
    NFTTokenCancelOfferTxData,
    NFTTokenBurnTxData,
    NFTTokenAcceptOfferTxData
)

from .escrow import EscrowCreateTxData
from .offer import OfferCreateTxData, OfferCancelTxData
from .account_delete import AccountDeleteTxData
from .trustset import TrustSetTxData
from .base import BaseTxData
from .payment import PaymentTxData
from ..api import APIClient
from scnrp.exception import InvalidTransactionHashError, InvalidAccountAddressError

def create_tx(json):
    factories = {
        'Payment': PaymentTxData,
        'TrustSet': TrustSetTxData,
        'AccountDelete': AccountDeleteTxData,
        'OfferCreate': OfferCreateTxData,
        'OfferCancel': OfferCancelTxData,
        'EscrowCreate': EscrowCreateTxData,
        'NFTokenCreateOffer': NFTTokenCreateOfferTxData,
        'NFTokenCancelOffer': NFTTokenCancelOfferTxData,
        'NFTokenBurn': NFTTokenBurnTxData,
        'NFTokenAcceptOffer': NFTTokenCancelOfferTxData,
    }
    typ = json['tx_json']['TransactionType']
    return factories.get(typ,BaseTxData).from_json(json)

def get_tx(hash:str):
    tx_req = Tx(transaction=hash)
    tx_res = APIClient.request(tx_req)
    if tx_res.status == ResponseStatus.ERROR:
        raise InvalidTransactionHashError()
    return create_tx(tx_res.result)

def get_account_txs(account:str):
    tx_req = AccountTx(account=account)
    tx_res = APIClient.request(tx_req)
    result = []
    if tx_res.status == ResponseStatus.ERROR:
        raise InvalidAccountAddressError()
    for tx_json in tx_res.result['transactions']:
        result.append(create_tx(tx_json))
    return result
