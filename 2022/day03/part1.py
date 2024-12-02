from string import ascii_letters

from bsoyka_aoc_utils import get_data
from loguru import logger

# 1-26 for a-z, 27-52 for A-Z
PRIORITIES = {
    letter: priority for priority, letter in enumerate(ascii_letters, start=1)
}
logger.debug("Established priorities")

rucksacks: list[str] = get_data(2022, 3, split=True)
logger.debug("Loaded rucksack list")

result: int = 0

for sack in rucksacks:
    half = len(sack) // 2
    one, two = sack[:half], sack[half:]

    shared = (set(one) & set(two)).pop()  # Get the only shared character
    priority = PRIORITIES[shared]

    result += priority

logger.success("Result: {}", result)
