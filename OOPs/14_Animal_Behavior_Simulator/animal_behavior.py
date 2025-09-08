"""
14. **Animal Behavior Simulator**
    - **Description**: Simulate animals with unique behaviors.
    - **Requirements**:
      - Base `Animal` with `make_sound()` and `move()`.
      - Subclasses: `Dog`, `Cat`, `Bird` with specific behaviors.
      - Create a `Zoo` to iterate over animals.
    - **Constraints**: Ensure realistic behavior modeling.


"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """ """

    def __init__(self, species: str, name: str, age: int, hungry: bool) -> None:
        self._species: str = species
        self._name: str = name
        self._age: int = age
        self._hungry: bool = hungry

    @property
    def is_hungry(self) -> bool:
        return self._hungry

    def _toggle_hungry(self) -> None:
        if self.is_hungry is True:
            self._hungry = False
        else:
            self._hungry = True

    @property
    def species(self) -> str:
        """The  species property."""
        return self.species

    @species.setter
    def species(self, value: str) -> None:
        self.species = value

    @property
    def name(self):
        """The name property."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        self._age = value

    @abstractmethod
    def make_sound(self) -> str: ...

    @abstractmethod
    def move(self) -> None: ...

    @abstractmethod
    def eat(self, food: str) -> None: ...

    @abstractmethod
    def sleep(self, hours: int) -> None: ...

    @abstractmethod
    def status(self) -> None: ...

    def _consume_energy(self, amount: float) -> None: ...

    def _increase_energy(self, amount: float) -> None: ...
