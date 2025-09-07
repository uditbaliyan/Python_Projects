import datetime
import re
from typing import Any, Dict


class InvalidEmailError(Exception):
    """Raised when an email address is invalid."""


class EmailAddressValidator:
    """
    Stores and validates an email address.

    Attributes:
        _email (str): The email address.
        _created_at (datetime): Timestamp when object was created.
        _immutable (bool): If True, object is read-only after creation.
    """

    EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def __init__(self, email: str, immutable: bool = True) -> None:
        if not self.is_valid(email):
            raise InvalidEmailError(f"Invalid email address: {email}")
        self._email = email  # assign first
        self._created_at = datetime.datetime.now()
        self._immutable = immutable

    # ---------------- Properties ----------------
    @property
    def email(self) -> str:
        return self._email

    @property
    def username(self) -> str:
        return self._email.split("@")[0]

    @property
    def domain(self) -> str:
        return self._email.split("@")[1]

    @property
    def created_at(self) -> datetime.datetime:
        return self._created_at

    @classmethod
    def is_valid(cls, email: str) -> bool:
        """Check if the email matches a basic regex pattern."""
        return bool(cls.EMAIL_REGEX.fullmatch(email))

    # ---------------- Dunder Methods ----------------
    def __str__(self) -> str:
        return self._email

    def __repr__(self) -> str:
        return (
            f"EmailAddressValidator(email='{self._email}', "
            f"immutable={self._immutable}, created_at={self._created_at.isoformat()})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, EmailAddressValidator):
            return NotImplemented
        return self._email == other._email

    def __hash__(self) -> int:
        # Safe because class is immutable
        return hash(self._email)

    # ---------------- Utility Methods ----------------
    def copy(self) -> "EmailAddressValidator":
        """Return a copy preserving email and created_at."""
        copy_obj = EmailAddressValidator(self._email, immutable=self._immutable)
        copy_obj._created_at = self._created_at  # preserve timestamp
        return copy_obj

    def to_dict(self) -> Dict[str, Any]:
        """Return a dictionary representation of the object."""
        return {
            "email": self._email,
            "username": self.username,
            "domain": self.domain,
            "created_at": self._created_at.isoformat(),
            "is_valid": self.is_valid,
        }

    def to_json(self) -> Dict[str, Any]:
        """Alias for to_dict; useful for JSON serialization."""
        return self.to_dict()

    def update_email(self, new_email: str) -> None:
        """Update the email address if the object is mutable."""
        if self._immutable:
            raise AttributeError(
                "Cannot modify immutable EmailAddressValidator instance."
            )
        if self.is_valid(new_email):
            self._email = new_email
        else:
            raise InvalidEmailError(f"Invalid email address: {new_email}")
