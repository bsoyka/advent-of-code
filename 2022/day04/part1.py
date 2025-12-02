import re

from bsoyka_aoc_utils import get_data
from loguru import logger

PAIR_NUMBERS = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)$")

pairs: list[str] = get_data(2022, 4, split=True)
logger.debug("Loaded pair list")

overlapping: int = 0

for pair in pairs:
    start1, end1, start2, end2 = map(int, PAIR_NUMBERS.match(pair).groups())

    # If either range fully contains the other
    if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
        overlapping += 1
        print(pair)

logger.success("Result: {}", overlapping)
