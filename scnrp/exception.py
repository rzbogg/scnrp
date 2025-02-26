class UserError(Exception):
    pass

class InvalidLedgerIndexError(UserError):
    def __init__(
        self,
        message = 'Please provide a valid ledger index'
    ) -> None:
        super().__init__(message)

class InvalidTransactionHashError(UserError):
    def __init__(
        self,
        message = 'Please provide a valid transaction hash'
    ) -> None:
        super().__init__(message)

class InvalidAccountAddressError(UserError):
    def __init__(
        self,
        message = 'Please provide a valid account address'
    ) -> None:
        super().__init__(message)
