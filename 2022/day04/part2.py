import re
from pathlib import Path

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

PAIR_NUMBERS = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)$")

pairs: list[str] = get_data(2022, 4, split=True)
logger.debug("Loaded pair list")

overlapping: int = 0

for pair in pairs:
    start1, end1, start2, end2 = map(int, PAIR_NUMBERS.match(pair).groups())

    # If either range starts or ends inside the other
    if (start1 <= start2 <= end1 or start1 <= end2 <= end1) or (
        start2 <= start1 <= end2 or start2 <= end1 <= end2
    ):
        overlapping += 1
        print(pair)

logger.success("Result: {}", overlapping)
