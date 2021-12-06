from __future__ import annotations

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

DAYS_TO_MULTIPLY = 7
NEW_FISH_TIMER = 8
TOTAL_DAYS = 80


class Lanternfish:
    """An exponentially-multiplying lanternfish.

    Args:
        timer (int/str): The lanternfish's internal timer in days.

    Attributes:
        timer (int): The lanternfish's internal timer in days.
    """

    def __init__(self, timer: int | str):
        self.timer = int(timer)

    def cycle(self, days_to_multiply: int) -> bool:
        """Cycles the lanternfish's timer.

        Args:
            days_to_multiply (int): The number of days it takes for the
                fish to multiply.

        Returns:
            bool: Whether a new lanternfish needs to be created.
        """
        if self.timer == 0:
            self.timer = days_to_multiply - 1
            return True

        self.timer -= 1
        return False


current_fish: list[Lanternfish] = get_data(
    2021, 6, func=Lanternfish, split=","
)
logger.debug("Loaded initial fish data")

for _ in range(TOTAL_DAYS):
    new_fish = [
        Lanternfish(NEW_FISH_TIMER)
        for fish in current_fish
        if fish.cycle(DAYS_TO_MULTIPLY)
    ]

    current_fish.extend(new_fish)

logger.success("Result: {}", len(current_fish))
