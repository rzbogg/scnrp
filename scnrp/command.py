from . import account
from .cli import arg_parser, command

@command('account','shows information about an account')
class Account:
    ARGUMENTS = [
        ( 'account_address',),
        ('-a ', '--address' , {'action':'store_true'}),
        ('-b ', '--balance', {'action':'store_true'} ),
        ('-lt ', '--last-tx', {'action':'store_true'} ),
        ('-t ', '--txs',{'action':'store_true'} ),
    ]

    def __init__(
        self,
        args ,
    ) -> None:
        self.args = args

    def _no_flags(self):
        return (
            not self.args.balance and not self.args.last_tx and
            not self.args.txs and not self.args.address
        )

    def run(self):
        account_data = account.get_account(self.args.account_address)
        if self._no_flags() :
            return account_data.summary()
        return account_data.flag_summary(
            self.args.address,
            self.args.balance,
            self.args.last_tx,
            self.args.txs,
        )


def create_command(args):
    match args.command:
        case 'account':
            return Account(args)
        case _:
            raise ValueError('Unknown Command!')
