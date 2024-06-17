from datetime import date


from bank.exceptions.account_exceptions import NegativeBalanceError, InvalidAmountError, InsufficientFundsError


class Account:
    """
    Represents a bank account.

    Attributes:
        account_number (str): The account number.
        balance (float): The balance of the account.
        created_date (date): The date the account was created.
        transactions (List[str]): A list of transactions associated with the account.

    Methods:
        deposit(amount: float):
            Deposits a specified amount into the account.
        withdraw(amount: float):
            Withdraws a specified amount from the account, if sufficient funds are available.
        __str__() -> str:
            Returns a human-readable string representation of the account.
        __repr__() -> str:
            Returns an unambiguous string representation of the account, useful for debugging.
    """

    def __init__(self, account_number: str, balance: float = 0.0, created_date: str = None):
        self.account_number = account_number
        self.balance = balance
        self.created_date = created_date or date.today().isoformat()

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, amount: float):
        if amount < 0:
            raise NegativeBalanceError(self._balance, amount)
        self._balance = amount

    def deposit(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError(
                amount, "Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError(
                amount, "Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'Account'):
        if amount <= 0:
            raise InvalidAmountError(
                amount, "Transfer amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.withdraw(amount)
        target_account.deposit(amount)

    def __str__(self) -> str:
        return f'Account(account_number={self.account_number}, balance={self.balance}, created_date={self.created_date})'
