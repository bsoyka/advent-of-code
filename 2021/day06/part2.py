from collections import Counter, defaultdict
from typing import DefaultDict

from bsoyka_aoc_utils import get_data
from loguru import logger

DAYS_TO_MULTIPLY = 7
NEW_FISH_TIMER = 8
TOTAL_DAYS = 256

# I opted not to reuse my initial object-oriented approach from part 1
# due to the incredible amount of recursion it would take for 256 days.

current_fish: dict[int, int] = dict(
    Counter(get_data(2021, 6, func=int, split=","))
)
logger.debug("Loaded initial fish data")

for _ in range(TOTAL_DAYS):
    new_fish: DefaultDict[int, int] = defaultdict(int)

    for timer, count in current_fish.items():
        timer -= 1

        if timer == -1:
            new_fish[NEW_FISH_TIMER] += count
            timer = DAYS_TO_MULTIPLY - 1

        new_fish[timer] += count

    current_fish = dict(new_fish)

logger.success("Result: {}", sum(current_fish.values()))
