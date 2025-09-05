from enum import Enum
from dataclasses import dataclass
from typing import Dict


class Gender(Enum):
    MALE = "m"
    FEMALE = "f"


@dataclass
class Customer:
    name: str
    age: int
    gender: Gender
    account_number: int
    account_balance: float
    account_status: str


class BankAccountManager:
    def __init__(self) -> None:
        self._accounts: Dict[int, Customer] = {}

    def open_account(
        self,
        name: str,
        age: int,
        gender: Gender,
        acc_number: int,
        balance: float,
        status: str,
    ):
        if balance < 0:
            raise ValueError("Balance can't be negative .")
        if acc_number in self._accounts:
            raise ValueError("Account number already exist .")
        self._accounts[acc_number] = Customer(
            name=name,
            age=age,
            gender=gender,
            account_number=acc_number,
            account_balance=balance,
            account_status=status,
        )

    def account_exists(self, acc_number: int) -> bool:
        return True if acc_number in self._accounts else False

    def withdraw(self, acc_number: int, amount: float):
        if not self.account_exists(acc_number):
            raise ValueError("No account available.")
        elif amount > self._accounts[acc_number].account_balance:
            raise ValueError("Not enough funds .")
        self._accounts[acc_number].account_balance -= amount

    def deposit(self, acc_number: int, amount: float):
        if amount < 0:
            raise ValueError("amount can't be negative .")
        elif self.account_exists(acc_number):
            self._accounts[acc_number].account_balance += amount
        else:
            raise Exception("No account available")


"""
    def transfer(self, from: int, to: int, amount: float):
        if self.account_exists(from) and self.account_exists(to):
            if self._accounts[from].account_balance >= amount:
                self._accounts[from].account_balance -= amount
                self._accounts[to].account_balance += amount
            else:
                raise ValueError("Not enough funds .")
        else:
            raise ValueError("Account does't exists .")
    
    def history(self):
        pass
"""
