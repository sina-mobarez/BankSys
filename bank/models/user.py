from datetime import date
import hashlib


class User:
    """
    Represents a user with personal details and authentication information.

    Attributes:
        username (str): The username of the customer.
        _password (str): The hashed password of the user.
        phone_number (str): The phone number of the user.
        address (str): The address of the user.
        date_of_birth (date): The date of birth of the user.


    Methods:
        __init__(username: str, password: str, phone_number: str, address: str, date_of_birth: str):
            Initializes a new user with the given details.
        _hash_password(password: str) -> str:
            Hashes the given password using SHA-256.
        _validate_phone_number(phone_number: str) -> str:
            Validates the phone number format.
        _validate_date_of_birth(date_of_birth: str) -> date:
            Validates the date of birth format and ensures it is in the past.
        password() -> str:
            Raises an AttributeError, indicating that the password attribute is write-only.
        password(new_password: str):
            Sets a new hashed password.
        phone_number() -> str:
            Gets the phone number of the user.
        phone_number(new_phone_number: str):
            Sets a new validated phone number.
        address() -> str:
            Gets the address of the user.
        address(new_address: str):
            Sets a new validated address.
        check_password(password: str) -> bool:
            Checks if the given password matches the stored hashed password.
        __str__() -> str:
            Returns a human-readable string representation of the customer.


    Example Usage:
        >>> user = User('john_doe', 'password123', '1234567890', '123 Main St', '1980-01-01')
        >>> print(user)
        User(username=john_doe, phone_number=1234567890, address=123 Main St, date_of_birth=1980-01-01)

        >>> user.phone_number = '0987654321'
        >>> print(user.phone_number)
        0987654321

        >>> print(user.check_password('password123'))
        True

    """
    def __init__(self, username: str, password: str, phone_number: str, address: str, date_of_birth: str):
        self.username = username
        self.password = self._hash_password(password)
        self.phone_number = self._validate_phone_number(phone_number)
        self.address = address
        self.date_of_birth = self._validate_date_of_birth(date_of_birth)

    @staticmethod
    def _hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def _validate_phone_number(phone_number: str) -> str:
        if len(phone_number) != 10 or not phone_number.isdigit():
            raise ValueError("Phone number must be 10 digits long.")
        return phone_number

    @staticmethod
    def _validate_date_of_birth(date_of_birth: str) -> date:
        try:
            dob = date.fromisoformat(date_of_birth)
            if dob >= date.today():
                raise ValueError("Date of birth must be in the past.")
            return dob
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    @property
    def password(self) -> str:
        raise AttributeError("Password is write-only.")

    @password.setter
    def password(self, new_password: str):
        self._password = self._hash_password(new_password)

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @phone_number.setter
    def phone_number(self, new_phone_number: str):
        self._phone_number = self._validate_phone_number(new_phone_number)

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, new_address: str):
        if not new_address:
            raise ValueError("Address cannot be empty.")
        self._address = new_address

    def check_password(self, password: str) -> bool:
        return self._password == self._hash_password(password)

    def __str__(self):
        return f'User(username={self.username}, phone_number={self.phone_number}, address={self.address}, date_of_birth={self.date_of_birth})'
