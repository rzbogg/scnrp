from xrpl.models import requests
from ..api import APIClient
from .transaction import Tx
from .payment import PaymentTx


def create_tx(json):
    factories = {
        'Payment' : PaymentTx
    }
    typ = json['tx_json']['TransactionType']
    return factories.get(typ,Tx).from_json(json)

def get_tx(hash:str):
    tx_req = requests.Tx(transaction=hash)
    tx_res = APIClient.request(tx_req)
    return create_tx(tx_res.result)

def get_account_txs(account:str):
    tx_req = requests.AccountTx(account=account)
    tx_res = APIClient.request(tx_req)
    result = []
    for tx_json in tx_res.result['transactions']:
        result.append(create_tx(tx_json))
    return result
