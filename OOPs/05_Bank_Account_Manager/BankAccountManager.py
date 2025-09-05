"""5. **Bank Account Manager**
- **Description**: Simulate bank accounts with transaction history.
- **Requirements**:
  - Support deposit, withdraw, and transfer with private balance.
  - Maintain a transaction log (list of dicts with timestamps via `datetime`).
  - Export history to CSV using `csv`.
- **Constraints**: Prevent overdrafts; ensure non-negative balances.

"""

from typing import Dict, Tuple, List
from datetime import datetime


class Customer:
    def __init__(self, name: str, customer_id: int):
        self.name = name
        self.customer_id = customer_id

    def __repr__(self):
        return f"Customer({self.name}, ID={self.customer_id})"


class Account:
    def __init__(self, acc_number: int, customer: Customer):
        self.acc_number = acc_number
        self.customer = customer
        self.account_balance = 0.0
        self.status = "OPEN"  # can be "OPEN" or "CLOSED"

    def __repr__(self):
        return f"Account({self.acc_number}, {self.customer.name}, Balance={self.account_balance}, Status={self.status})"


class BankManager:
    def __init__(self):
        self._accounts: Dict[int, Account] = {}
        self._account_history: Dict[
            int, Tuple[Customer, List[Tuple[str, float, str]]]
        ] = {}

    def open_account(self, acc_number: int, customer: Customer):
        """Create new account and initialize history"""
        if acc_number in self._accounts:
            raise ValueError("Account already exists")
        account = Account(acc_number, customer)
        self._accounts[acc_number] = account
        self._account_history[acc_number] = (customer, [])
        self._log(acc_number, "Opened", 0.0)

    def close_account(self, acc_number: int):
        """Mark account as closed"""
        account = self._get_account(acc_number)
        account.status = "CLOSED"
        self._log(acc_number, "Closed", 0.0)

    def deposit(self, acc_number: int, amount: float):
        """TODO: check status and deposit money, log history"""
        acc = self._get_account(acc_number)
        acc.account_balance += amount
        self._log(acc_number, "deposit", amount)

    def withdraw(self, acc_number: int, amount: float):
        """TODO: check status, check balance, withdraw money, log history"""
        acc = self._get_account(acc_number)
        if acc.account_balance < amount:
            raise ValueError("Not enough funds .")
        acc.account_balance -= amount

    def get_balance(self, acc_number: int) -> float:
        """TODO: return balance if account open"""
        return self._get_account(acc_number).account_balance

    def print_history(self, acc_number: int):
        """Pretty-print history for account"""
        _, history = self._account_history.get(acc_number, (None, []))
        for action, amount, timestamp in history:
            print(f"{timestamp}: {action} {amount}")

    # --- internal helpers ---
    def _get_account(self, acc_number: int) -> Account:
        account = self._accounts.get(acc_number)
        if not account:
            raise ValueError("Account not found")
        return account

    def _log(self, acc_number: int, action: str, amount: float):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._account_history[acc_number][1].append((action, amount, timestamp))
