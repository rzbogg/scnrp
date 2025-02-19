from .account import get_account
from . import cli
from .ledger import get_ledger
from .transaction import get_tx


@cli.argument('-a','--address', action='store_true')
@cli.argument('-b','--balance', action='store_true')
@cli.argument('-lt','--last-tx', action='store_true')
@cli.argument('-t','--txs', action='store_true')
@cli.argument('account_address')
@cli.command('shows information about an account')
def account(args):
    account_data = get_account(args.account_address)
    return account_data.summary()

@cli.argument('ledger_index')
@cli.command('shows information about a specific ledger')
def ledger(args):
    ledger = get_ledger(args.ledger_index)
    return ledger.summary()


@cli.argument('transaction_hash')
@cli.command('shows information about a specific transaction')
def transaction(args):
    hash = args.transaction_hash
    tx = get_tx(hash)
    return tx.summary()


def run_command(args):
    match args.command:
        case 'account':
            return account(args)
        case 'ledger':
            return ledger(args)
        case 'transaction':
            return transaction(args)
        case _:
            raise ValueError('Unknown Command!')
