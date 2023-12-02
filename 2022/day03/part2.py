from pathlib import Path
from string import ascii_letters

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

# 1-26 for a-z, 27-52 for A-Z
PRIORITIES = {
    letter: priority for priority, letter in enumerate(ascii_letters, start=1)
}
logger.debug("Established priorities")

rucksacks: list[str] = get_data(2022, 3, split=True)
logger.debug("Loaded rucksack list")

# Divide into groups of 3
groups = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]
logger.debug("Divided rucksacks into groups")

result: int = 0

for group in groups:
    one, two, three = group

    shared = (
        set(one) & set(two) & set(three)
    ).pop()  # Get the only shared character
    priority = PRIORITIES[shared]

    result += priority

logger.success("Result: {}", result)
