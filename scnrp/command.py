from . import account

class AccountCommand:
    def __init__(
        self,
        address,
        params,
    ) -> None:
        self.address = address
        self.params = params

    def run(self):
        account_data = account.get_account(self.address)
        result = 'balance'
        if not self.params:
            return account_data.summary()
        # return self._run_params(account)

    def _run_params(self,account):
        raise NotImplementedError()

    @classmethod
    def from_args(cls,args):
        return cls(
            address = args[0],
            params  = [p.removeprefix('--')for p in args[1:]]
        )


def create_command(args):
    command_str = args[0]
    match command_str:
        case 'account':
            return AccountCommand.from_args(args[1:])
        case _:
            raise ValueError('Unknown Command!')
