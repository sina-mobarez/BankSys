from bank.exceptions.base import UserError


class InvalidPhoneError(UserError):
    """Raised when an invalid phone number is provided."""
    def __init__(self, phone, message="Invalid phone number provided."):
        self.phone = phone
        self.message = message

    def __str__(self):
        return f'{self.message} Phone: {self.phone}'

