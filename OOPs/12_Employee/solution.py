from abc import ABC, abstractmethod
from enum import Enum
import datetime
from typing import List, Optional


# ===============================
# Enums for Roles
# ===============================


class DevLevel(Enum):
    JUNIOR = "junior"
    MID = "mid"
    SENIOR = "senior"


class ManagerRole(Enum):
    MANAGER = "manager"
    SENIOR_MANAGER = "senior_manager"


# ===============================
# Abstract Employee Base
# ===============================


class Employee(ABC):
    """Base class for all employees."""

    def __init__(
        self,
        name: str,
        base_salary: float,
        joining_date: Optional[datetime.datetime] = None,
    ) -> None:
        if base_salary < 0:
            raise ValueError("Base salary cannot be negative.")

        self._name: str = name
        self._base_salary: float = base_salary
        self._join_date: datetime.datetime = joining_date or datetime.datetime.now()
        self._promotion_history: List[str] = []  # track promotions with timestamps
        self._role: str = self.__class__.__name__

    # ---- Abstract methods ----
    @abstractmethod
    def calculate_salary(self) -> float:
        """Return the current salary based on role-specific rules."""
        pass

    @abstractmethod
    def promote(self, new_role: str) -> None:
        """Promote the employee and log the promotion."""
        pass

    # ---- Helpers ----
    def log_promotion(self, new_role: str) -> None:
        """Helper to log promotion with timestamp."""
        timestamp = datetime.datetime.now().isoformat()
        self._promotion_history.append(f"{timestamp}: Promoted to {new_role}")
        self._role = new_role

    # ---- Properties ----
    @property
    def promotion_history(self) -> List[str]:
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

    @property
    def role(self) -> str:
        return self._role

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name}, salary={self.calculate_salary():.2f}, role={self._role})"


# ===============================
# Subclasses
# ===============================


class Manager(Employee):
    """Manager role with fixed bonus added to base salary."""

    def __init__(
        self,
        name: str,
        base_salary: float,
        bonus: float,
        role: ManagerRole = ManagerRole.MANAGER,
    ) -> None:
        super().__init__(name, base_salary)
        if bonus < 0:
            raise ValueError("Bonus cannot be negative.")
        self._bonus = bonus
        self._role = role.value

    def calculate_salary(self) -> float:
        return self._base_salary + self._bonus

    def promote(self, new_role: str) -> None:
        valid_roles = {ManagerRole.SENIOR_MANAGER.value}
        if new_role in valid_roles:
            self.log_promotion(new_role)
        else:
            raise ValueError(f"Invalid promotion for Manager: {new_role}")


class Developer(Employee):
    """Developer role with salary based on experience level."""

    _level_bonus = {
        DevLevel.JUNIOR.value: 100000,
        DevLevel.MID.value: 200000,
        DevLevel.SENIOR.value: 500000,
    }

    def __init__(self, name: str, base_salary: float, level: DevLevel) -> None:
        super().__init__(name, base_salary)
        self._level = level
        self._role = f"developer-{self._level.value}"

    def calculate_salary(self) -> float:
        return self._base_salary + self._level_bonus.get(self._level.value, 0)

    def promote(self, new_role: str) -> None:
        if new_role in self._level_bonus:
            self._level = DevLevel(new_role)
            self.log_promotion(f"developer-{new_role}")
        else:
            raise ValueError(f"Invalid promotion for Developer: {new_role}")


class Intern(Employee):
    """Intern role with stipend instead of full salary."""

    def __init__(self, name: str, stipend: float) -> None:
        if stipend < 0:
            raise ValueError("Stipend cannot be negative.")
        super().__init__(name, base_salary=0)
        self._stipend = stipend
        self._role = "intern"

    def calculate_salary(self) -> float:
        return self._stipend

    def promote(self, new_role: str) -> None:
        if new_role == DevLevel.JUNIOR.value:
            self.log_promotion("developer-junior")
        else:
            raise ValueError("Interns can only be promoted to Developer (junior).")


if __name__ == "__main__":
    dev = Developer("Alice", 500000, DevLevel.JUNIOR)
    print(dev)  # Developer(name=Alice, salary=600000.00, role=developer-junior)

    dev.promote("mid")
    print(dev.promotion_history)

    intern = Intern("Bob", 15000)
    print(intern)

    intern.promote("junior")
    print(intern.promotion_history)

    mgr = Manager("Charlie", 1000000, 250000)
    print(mgr)

    mgr.promote("senior_manager")
    print(mgr.promotion_history)
