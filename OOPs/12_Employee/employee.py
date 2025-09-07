from abc import ABC, abstractmethod
import datetime
from typing import List


class Employee(ABC):
    """Base class for all employees."""

    def __init__(
        self, name: str, base_salary: float, joining_date: datetime.datetime
    ) -> None:
        self._name: str = name
        self._base_salary: float = base_salary
        self._join_date: datetime.datetime = joining_date
        self._promotion_history: List[str] = []  # track promotions with timestamps

    @abstractmethod
    def calculate_salary(self) -> float:
        """Return the current salary based on role-specific rules."""
        pass

    @abstractmethod
    def promote(self, new_role: str) -> None:
        """Promote the employee and log the promotion."""
        pass

    def log_promotion(self, new_role: str) -> None:
        """Helper to log promotion with timestamp."""
        timestamp = datetime.datetime.now().isoformat()
        self._promotion_history.append(f"{timestamp}: Promoted to {new_role}")

    @property
    def promotion_history(self) -> List[str]:
        """Return the list of promotions."""
        return self._promotion_history

    @property
    def name(self) -> str:
        return self._name

    @property
    def base_salary(self) -> float:
        return self._base_salary

    @property
    def join_date(self) -> datetime.datetime:
        return self._join_date

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name}, salary={self.calculate_salary():.2f})"


class Manager(Employee):
    """Manager role with fixed bonus added to base salary."""

    def __init__(self, name: str, base_salary: float, bonus: float) -> None:
        super().__init__(name, base_salary, datetime.datetime.now())
        self._bonus = bonus

    def calculate_salary(self) -> float:
        # TODO: implement manager salary logic
        return self._base_salary + self._bonus

    def promote(self, new_role: str) -> None:
        # TODO: logic for promoting a manager
        if new_role.lower() == "senior manager":
            self.log_promotion(new_role)
        else:
            raise ValueError("Invalid role for Manager promotion")


class Developer(Employee):
    """Developer role with salary based on experience level."""

    def __init__(self, name: str, base_salary: float, level: str) -> None:
        super().__init__(name, base_salary, datetime.datetime.now())
        self._level = level.lower()  # e.g., "junior", "mid", "senior"

    def calculate_salary(self) -> float:
        # TODO: implement developer salary logic
        return self._base_salary + (
            500000
            if self._level == "senior"
            else 200000
            if self._level == "mid"
            else 100000
        )

    def promote(self, new_role: str) -> None:
        # TODO: logic for promoting a developer
        if new_role.lower() in ["junior", "mid", "senior"]:
            self._level = new_role.lower()
            self.log_promotion(new_role)
        else:
            raise ValueError("Invalid role for Developer promotion")


class Intern(Employee):
    """Intern role with stipend instead of full salary."""

    def __init__(self, name: str, stipend: float) -> None:
        super().__init__(name, base_salary=0, joining_date=datetime.datetime.now())
        self._stipend = stipend

    def calculate_salary(self) -> float:
        # TODO: implement intern salary logic
        return self._stipend

    def promote(self, new_role: str) -> None:
        # TODO: logic for promoting an intern
        if new_role.lower() == "developer":
            self.log_promotion(new_role)
        else:
            raise ValueError("Interns can only be promoted to Developer")
