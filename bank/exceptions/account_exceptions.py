from bank.exceptions.base import AccountError

class InvalidAmountError(AccountError):
    """Raised when an invalid amount is provided for a transaction."""
    def __init__(self, amount, message="Invalid amount provided for transaction."):
        self.amount = amount
        self.message = message

    def __str__(self):
        return f'{self.message} Amount: {self.amount}'

class InsufficientFundsError(AccountError):
    """Raised when there are insufficient funds for a withdrawal."""
    def __init__(self, balance, amount, message="Insufficient funds for withdrawal."):
        self.balance = balance
        self.amount = amount
        self.message = message

    def __str__(self):
        return f'{self.message} Balance: {self.balance}, Attempted Withdrawal: {self.amount}'

class NegativeBalanceError(AccountError):
    """Raised when a balance operation would result in a negative balance."""
    def __init__(self, balance, amount, message="Operation would result in negative balance."):
        self.balance = balance
        self.amount = amount
        self.message = message

    def __str__(self):
        return f'{self.message} Balance: {self.balance}, Amount: {self.amount}'