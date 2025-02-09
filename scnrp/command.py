from account import Account, get_account

class AccountCommand:
    def __init__(
        self,
        account,
        params,
    ) -> None:
        self.account = account
        self.params = params

    def run(self):
        account = get_account(self.account)
        result = 'balance'
        if not self.params:
            return self._run_no_params(account)
        # return self._run_params(account)

    def _run_params(self,account):
        raise NotImplementedError()

    def _run_no_params(self,account):
        result = ''
        for key, value in account.fields():
            result += f'{key.capitalize()}: {value}\n'
        return result

    @classmethod
    def from_args(cls,args):
        return cls(
            account = args[0],
            params  = [p.removeprefix('--')for p in args[1:]]
        )


def create_command(args):
    command_str = args[0]
    match command_str:
        case 'account':
            return AccountCommand.from_args(args[1:])
        case _:
            raise ValueError('Unknown Command!')
