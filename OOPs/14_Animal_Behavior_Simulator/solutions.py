from abc import ABC, abstractmethod
import random


# ---------------- Base Class ----------------
class Animal(ABC):
    """Abstract base class for all animals."""

    def __init__(
        self, name: str, species: str, age: int, energy_level: float = 100.0
    ) -> None:
        self._name = name
        self._species = species
        self._age = age
        self._energy_level = energy_level
        self._is_hungry = True

    # -------- Properties --------
    @property
    def name(self) -> str:
        return self._name

    @property
    def species(self) -> str:
        return self._species

    @property
    def age(self) -> int:
        return self._age

    @property
    def energy_level(self) -> float:
        return self._energy_level

    @property
    def is_hungry(self) -> bool:
        return self._is_hungry

    # -------- Abstract Methods --------
    @abstractmethod
    def make_sound(self) -> str:
        pass

    @abstractmethod
    def move(self) -> str:
        pass

    # -------- Common Methods --------
    def eat(self, food: str) -> str:
        self._increase_energy(20)
        self._is_hungry = False
        return f"{self._name} the {self._species} eats {food}."

    def sleep(self, hours: int) -> str:
        self._increase_energy(hours * 10)
        return f"{self._name} the {self._species} sleeps for {hours} hours."

    def status(self) -> str:
        return (
            f"{self._name} ({self._species}) - Age: {self._age}, "
            f"Energy: {self._energy_level:.1f}, Hungry: {self._is_hungry}"
        )

    # -------- Helpers --------
    def _consume_energy(self, amount: float) -> None:
        self._energy_level = max(0, self._energy_level - amount)
        if self._energy_level == 0:
            self._is_hungry = True

    def _increase_energy(self, amount: float) -> None:
        self._energy_level = min(100, self._energy_level + amount)


# ---------------- Subclasses ----------------
class Dog(Animal):
    def __init__(
        self, name: str, age: int, breed: str, is_playful: bool = True
    ) -> None:
        super().__init__(name, "Dog", age)
        self._breed = breed
        self._is_playful = is_playful

    def make_sound(self) -> str:
        sound = "Woof! Woof!" if self._energy_level > 20 else "Whine..."
        return f"{self.name} the Dog says: {sound}"

    def move(self) -> str:
        self._consume_energy(15)
        return f"{self.name} the Dog runs happily."

    def fetch(self, item: str) -> str:
        self._consume_energy(10)
        return f"{self.name} fetches the {item}."

    def wag_tail(self) -> str:
        return f"{self.name} wags its tail excitedly."


class Cat(Animal):
    def __init__(self, name: str, age: int, color: str, lives_left: int = 9) -> None:
        super().__init__(name, "Cat", age)
        self._color = color
        self._lives_left = lives_left

    def make_sound(self) -> str:
        sound = "Meow!" if self._energy_level > 30 else "Purr..."
        return f"{self.name} the Cat says: {sound}"

    def move(self) -> str:
        self._consume_energy(10)
        return f"{self.name} the Cat prowls gracefully."

    def scratch(self, surface: str) -> str:
        self._consume_energy(5)
        return f"{self.name} scratches the {surface}."

    def climb(self) -> str:
        self._consume_energy(20)
        return f"{self.name} climbs a tree."


class Bird(Animal):
    def __init__(
        self, name: str, age: int, wing_span: float, can_fly: bool = True
    ) -> None:
        super().__init__(name, "Bird", age)
        self._wing_span = wing_span
        self._can_fly = can_fly

    def make_sound(self) -> str:
        return f"{self.name} the Bird chirps cheerfully!"

    def move(self) -> str:
        if self._can_fly:
            return self.fly(10)
        else:
            self._consume_energy(5)
            return f"{self.name} hops along the ground."

    def fly(self, distance: float) -> str:
        self._consume_energy(distance * 0.5)
        return f"{self.name} flies {distance} meters."

    def build_nest(self) -> str:
        self._consume_energy(10)
        return f"{self.name} builds a cozy nest."


# ---------------- Zoo ----------------
class Zoo:
    def __init__(self) -> None:
        self._animals: list[Animal] = []

    def add_animal(self, animal: Animal) -> None:
        self._animals.append(animal)

    def remove_animal(self, name: str) -> None:
        self._animals = [a for a in self._animals if a.name != name]

    def list_animals(self) -> str:
        return "\n".join(a.status() for a in self._animals)

    def feed_all(self, food: str) -> None:
        for a in self._animals:
            print(a.eat(food))

    def make_all_sounds(self) -> None:
        for a in self._animals:
            print(a.make_sound())

    def simulate_day(self) -> None:
        """Each animal performs a random action."""
        actions = ["make_sound", "move", "sleep"]
        for a in self._animals:
            action = random.choice(actions)
            if action == "make_sound":
                print(a.make_sound())
            elif action == "move":
                print(a.move())
            elif action == "sleep":
                print(a.sleep(random.randint(1, 3)))


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    zoo = Zoo()
    zoo.add_animal(Dog(name="Rex", age=5, breed="Labrador"))
    zoo.add_animal(Cat(name="Whiskers", age=3, color="Black"))
    zoo.add_animal(Bird(name="Tweety", age=1, wing_span=0.25))

    print("=== Zoo Animals ===")
    print(zoo.list_animals())

    print("\n=== Feeding Time ===")
    zoo.feed_all("food")

    print("\n=== Animal Sounds ===")
    zoo.make_all_sounds()

    print("\n=== Simulate a Day ===")
    zoo.simulate_day()
