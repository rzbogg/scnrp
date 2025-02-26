from xrpl.models.requests import Ledger
from xrpl.models.response import ResponseStatus
from xrpl.utils.xrp_conversions import drops_to_xrp
from .api import APIClient
from scnrp.exception import InvalidLedgerIndexError


class LedgerData:
    def __init__(
        self,
        index,
        hash,
        parent_hash,
        txs_hash,
        closed_on,
        total_coins,
    ) -> None:
        self.index = index
        self.hash = hash
        self.parent_hash = parent_hash
        self.txs_hash = txs_hash
        self.closed_on = closed_on
        self.total_coins = total_coins

    def summary(self):
        return f'''Ledger index: {self.index}
Ledger hash: {self.hash}
Parent hash: {self.parent_hash}
Transactions hash: {self.txs_hash}
Closed On: {self.closed_on}
Total coins: {drops_to_xrp(self.total_coins)}'''

    @classmethod
    def from_json(cls,json):
        return cls(
            index = json['ledger_index'],
            hash = json['ledger_hash'],
            parent_hash = json['ledger']['parent_hash'],
            txs_hash= json['ledger']['transaction_hash'],
            closed_on = json['ledger']['close_time_human'],
            total_coins = json['ledger']['total_coins'],
        )



def get_ledger(ledger_index:int):
    req_ledger = Ledger(ledger_index=ledger_index)
    response = APIClient.request(req_ledger)
    if response.status == ResponseStatus.ERROR:
        raise InvalidLedgerIndexError()
    return LedgerData.from_json(response.result)
