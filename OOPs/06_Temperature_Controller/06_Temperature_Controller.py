from typing import Dict
from datetime import datetime


class TemperatureController:
    def __init__(self, celsius: float) -> None:
        self._celsius: float = celsius
        self._history: Dict[datetime, float] = {}

    @property
    def celsius(self):
        """The  property."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def kelvin(self):
        """The  property."""
        return self._celsius

    @property
    def fahrenheit(self):
        """fahrenheit property"""
        return self._celsius

    def is_below_freezing(self) -> bool:
        return bool(self._celsius < 0)

    def is_above_freezing(self) -> bool:
        return bool(self._celsius > 0)

    def log(self, temp_change: float) -> None:
        now = datetime.now()
        self._history[now] = temp_change

    def log_history(self, limit: int | None = None) -> None:
        for item in self._history.items():
            print(item)

    def average_temp(self) -> float:
        temp_sum = 0
        size = len(self._history)
        for _, temp in self._history.items():
            temp_sum += temp
        return temp_sum / size

    def max_temp(self) -> float:
        temp_max = 0
        for _, temp in self._history.items():
            max(temp_max, temp)
        return temp_max

    def min_temp(self) -> float:
        temp_min = 0
        for _, temp in self._history.items():
            min(temp_min, temp)
        return temp_min
