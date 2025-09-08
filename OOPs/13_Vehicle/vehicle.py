from abc import ABC, abstractmethod

""" 
13. **Vehicle Family**  
    - **Description**: Model vehicles with type-specific behaviors.  
    - **Requirements**:  
      - Base `Vehicle` with `start_engine()` and `fuel_efficiency()`.  
      - Subclasses: `Car`, `Bike`, `Truck` with distinct implementations.  
      - Simulate travel distance based on fuel.  
    - **Constraints**: Handle invalid states (e.g., no fuel).
"""


class Vehicle(ABC):
    """Abstract base class for all vehicles."""

    def __init__(self, fuel_capacity: float, fuel_level: float = 0.0) -> None:
        if fuel_capacity <= 0:
            raise ValueError("Fuel capacity must be positive.")
        if not (0 <= fuel_level <= fuel_capacity):
            raise ValueError("Fuel level must be between 0 and fuel capacity.")

        self._fuel_capacity = fuel_capacity
        self._fuel_level = fuel_level
        self._engine_started = False

    # ---------------- Abstract Contract ----------------
    @abstractmethod
    def start_engine(self) -> None:
        """Start the vehicle's engine."""
        pass

    @abstractmethod
    def fuel_efficiency(self) -> float:
        """Fuel efficiency in km/l."""
        pass

    # ---------------- Properties ----------------
    @property
    def fuel_capacity(self) -> float:
        return self._fuel_capacity

    @property
    def fuel_level(self) -> float:
        return self._fuel_level

    @property
    def engine_started(self) -> bool:
        return self._engine_started

    @property
    def remaining_range(self) -> float:
        """Estimated distance the vehicle can travel with remaining fuel."""
        return self._fuel_level * self.fuel_efficiency()

    # ---------------- Public Methods ----------------
    def refuel(self, liters: float) -> None:
        """Add fuel up to the capacity."""
        if liters <= 0:
            raise ValueError("Refuel amount must be positive.")
        if self._fuel_level + liters > self._fuel_capacity:
            raise ValueError("Cannot exceed fuel capacity.")
        self._fuel_level += liters

    def travel(self, distance: float) -> None:
        """Travel a distance, consuming fuel accordingly."""
        if not self._engine_started:
            raise RuntimeError("Engine must be started before traveling.")

        fuel_needed = distance / self.fuel_efficiency()
        if fuel_needed > self._fuel_level:
            raise RuntimeError("Not enough fuel for this journey.")

        self._consume_fuel(distance)
        print(f"{self.__class__.__name__} traveled {distance} km.")

    # ---------------- Helpers ----------------
    def _consume_fuel(self, distance: float) -> None:
        """Private helper to reduce fuel level."""
        fuel_used = distance / self.fuel_efficiency()
        self._fuel_level -= fuel_used


class Car(Vehicle):
    """Concrete Car class implementing Vehicle behavior."""

    def __init__(
        self,
        fuel_capacity: float,
        fuel_level: float = 0.0,
        num_doors: int = 4,
        trunk_capacity: float = 300.0,
    ) -> None:
        super().__init__(fuel_capacity, fuel_level)
        self._num_doors = num_doors
        self._trunk_capacity = trunk_capacity
        self._current_load = 0.0
        self._ac_on = False

    # ---------------- Overrides ----------------
    def start_engine(self) -> None:
        if self._fuel_level <= 0:
            raise RuntimeError("Cannot start engine: No fuel.")
        self._engine_started = True
        print("Car engine started with a smooth ignition sound!")

    def fuel_efficiency(self) -> float:
        """Return fuel efficiency in km/l. AC reduces efficiency slightly."""
        base_efficiency = 15.0  # default km/l
        return base_efficiency * (0.9 if self._ac_on else 1.0)

    # ---------------- Properties ----------------
    @property
    def num_doors(self) -> int:
        return self._num_doors

    @property
    def trunk_capacity(self) -> float:
        return self._trunk_capacity

    @property
    def ac_on(self) -> bool:
        return self._ac_on

    # ---------------- Public Methods ----------------
    def load_trunk(self, weight: float) -> None:
        """Load items into the trunk."""
        if weight <= 0:
            raise ValueError("Weight must be positive.")
        if self._current_load + weight > self._trunk_capacity:
            raise RuntimeError("Exceeds trunk capacity.")
        self._current_load += weight

    def toggle_ac(self, on: bool) -> None:
        """Turn the AC on or off."""
        self._ac_on = on
        state = "on" if on else "off"
        print(f"Air conditioning turned {state}.")

    # ---------------- Safety Helper ----------------
    def _check_safety(self) -> None:
        """Simulate safety checks before travel."""
        if self._num_doors < 2:
            raise RuntimeError("Car must have at least 2 doors.")
        print("Safety checks passed. All doors locked.")

    def travel(self, distance: float) -> None:
        """Extend base travel with car-specific checks."""
        self._check_safety()
        super().travel(distance)


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    my_car = Car(fuel_capacity=50, fuel_level=10, num_doors=4, trunk_capacity=200)
    my_car.start_engine()
    my_car.toggle_ac(True)
    print(f"Remaining range: {my_car.remaining_range:.2f} km")
    my_car.load_trunk(50)
    my_car.travel(30)
    print(f"Fuel left: {my_car.fuel_level:.2f} L")
