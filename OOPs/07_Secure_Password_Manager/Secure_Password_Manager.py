from datetime import datetime
from typing import Dict, List, Any
import hashlib
import json

"""
class WeakPasswordException(Exception):
    pass


class ManagerLockedException(Exception):
    pass


class SecurePasswordManager:
    LOCKOUT_THRESHOLD = 10

    def __init__(self, username: str, password: str) -> None:
        if self._validate_strength(password):
            self._username = username
            self._password_hash: str = self._hash_password(password)
            self._password_strength: str = self.password_strength(password)
            self._history: Dict[str, List[datetime]] = {
                "SUCESS": [],
                "FAILED": [],
                "UPDATE": [],
            }
            self._failed_attempts = 0
            self._last_updated: datetime
            self._is_locked: bool = False
        else:
            raise WeakPasswordException

    @property
    def is_locked(self):
        return self._is_locked

    @property
    def password_strength(self, password: str | None) -> str:
        

    @property
    def failed_attempt_count(self):
        return len(self._history["FAILED"])

    @property
    def sucess_attempt_count(self):
        return len(self._history["SUCESS"])

    @property
    def update_attempt_count(self):
        return len(self._history["UPDATE"])

    @property
    def last_updated(self):
        return self._last_updated

    def _hash_password(self, password):
        
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def _validate_strength(self, password: str) -> bool:
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(not c.isalnum() for c in password)

        return (
            len(password) >= 8 and has_upper and has_lower and has_digit and has_symbol
        )

    def verify_password(self, password: str) -> bool:

        if self.LOCKOUT_THRESHOLD < 0:
            raise ManagerLockedException("Volt is locked .")
        if self._hash_password(password) == self._password_hash:
            self.LOCKOUT_THRESHOLD = 10
            self.log("SUCESS")
            return True
        self.LOCKOUT_THRESHOLD -= 1
        self.log("FAILED")
        return False

    def update_password(self, new_password):

        if self._validate_strength(new_password):
            self._password_hash = self._hash_password(new_password)
            self.log("UPDATE")
        else:
            raise WeakPasswordException("Try strong password")

    def reset_failed_attempts(self):

        self._failed_attempts = 0

    def export_log(self):
        pass

    def log(self, activity: str):
        
        now = datetime.now()
        if activity == "SUCESS":
            self._history["SUCESS"].append(now)
        elif activity == "FAILED":
            self._history["FAILED"].append(now)
        else:
            self._history["UPDATE"].append(now)

    def history(self):
        return self._history

    def to_json(self):
        pass

    def from_json(self):
        pass
"""


class WeakPasswordException(Exception):
    """Raised when a password does not meet strength requirements."""

    pass


class ManagerLockedException(Exception):
    """Raised when too many failed attempts lock the manager."""

    pass


class SecurePasswordManager:
    """Secure password manager with hashing, strength validation,
    lockout mechanism, and audit logging."""

    LOCKOUT_THRESHOLD = 5  # configurable

    def __init__(self, username: str, password: str) -> None:
        if not self._validate_strength(password):
            raise WeakPasswordException("Password does not meet strength requirements.")

        self._username: str = username
        self._password_hash: str = self._hash_password(password)
        self._password_strength: str = self._get_strength_label(password)

        self._history: Dict[str, List[datetime]] = {
            "SUCCESS": [],
            "FAILED": [],
            "UPDATE": [],
        }
        self._failed_attempts: int = 0
        self._is_locked: bool = False
        self._last_updated: datetime = datetime.now()

    # ─── Properties ──────────────────────────────────────────
    @property
    def is_locked(self) -> bool:
        return self._is_locked

    @property
    def failed_attempt_count(self) -> int:
        return len(self._history["FAILED"])

    @property
    def success_attempt_count(self) -> int:
        return len(self._history["SUCCESS"])

    @property
    def update_attempt_count(self) -> int:
        return len(self._history["UPDATE"])

    @property
    def last_updated(self) -> datetime:
        return self._last_updated

    @property
    def password_strength(self) -> str:
        """Returns the label of current password strength."""
        return self._password_strength

    # ─── Internal Helpers ─────────────────────────────────────
    def _hash_password(self, password: str) -> str:
        """Return a SHA-256 hash of the password."""
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def _validate_strength(self, password: str) -> bool:
        """Check if the password meets baseline strength requirements."""
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(not c.isalnum() for c in password)
        return (
            len(password) >= 8 and has_upper and has_lower and has_digit and has_symbol
        )

    def _get_strength_label(self, password: str) -> str:
        """Return a qualitative strength label for the password."""
        score = 0
        if len(password) >= 12:
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(not c.isalnum() for c in password):
            score += 1

        if score <= 2:
            return "Weak"
        elif score == 3 or score == 4:
            return "Moderate"
        return "Strong"

    def _log(self, activity: str) -> None:
        """Log an activity with current timestamp."""
        now = datetime.now()
        if activity in self._history:
            self._history[activity].append(now)
        else:
            raise ValueError(f"Invalid activity type: {activity}")

    # ─── Public Methods ──────────────────────────────────────
    def verify_password(self, password: str) -> bool:
        """Verify a password against the stored hash."""
        if self._is_locked:
            raise ManagerLockedException("Vault is locked.")

        if self._hash_password(password) == self._password_hash:
            self._failed_attempts = 0
            self._log("SUCCESS")
            return True

        self._failed_attempts += 1
        self._log("FAILED")

        if self._failed_attempts >= self.LOCKOUT_THRESHOLD:
            self._is_locked = True
            raise ManagerLockedException(
                "Vault is now locked after too many failed attempts."
            )

        return False

    def update_password(self, old_password: str, new_password: str) -> None:
        """Update the password if old one matches and new one is strong."""
        if not self.verify_password(old_password):
            raise ValueError("Old password is incorrect.")

        if not self._validate_strength(new_password):
            raise WeakPasswordException(
                "New password does not meet strength requirements."
            )

        self._password_hash = self._hash_password(new_password)
        self._password_strength = self._get_strength_label(new_password)
        self._last_updated = datetime.now()
        self._log("UPDATE")

    def reset_failed_attempts(self) -> None:
        """Reset failed attempts count."""
        self._failed_attempts = 0

    def history(self) -> Dict[str, List[datetime]]:
        """Return full audit history."""
        return self._history

    def to_json(self) -> str:
        """Export manager state as JSON."""
        data: Dict[str, Any] = {
            "username": self._username,
            "password_hash": self._password_hash,
            "password_strength": self._password_strength,
            "history": {
                key: [dt.isoformat() for dt in value]
                for key, value in self._history.items()
            },
            "failed_attempts": self._failed_attempts,
            "is_locked": self._is_locked,
            "last_updated": self._last_updated.isoformat(),
        }
        return json.dumps(data, indent=2)

    @classmethod
    def from_json(cls, json_data: str) -> "SecurePasswordManager":
        """Rebuild a manager instance from JSON (dangerous in real systems)."""
        data = json.loads(json_data)
        obj = cls.__new__(cls)  # bypass __init__
        obj._username = data["username"]
        obj._password_hash = data["password_hash"]
        obj._password_strength = data["password_strength"]
        obj._history = {
            key: [datetime.fromisoformat(ts) for ts in value]
            for key, value in data["history"].items()
        }
        obj._failed_attempts = data["failed_attempts"]
        obj._is_locked = data["is_locked"]
        obj._last_updated = datetime.fromisoformat(data["last_updated"])
        return obj
