import sys
from typing import List

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

TOTAL = 2020

ENTRIES: List[int] = get_data(2020, 1, func=int, split_lines=True)
logger.debug("Loaded entries list")

for entry in ENTRIES:
    if (entry2 := TOTAL - entry) in ENTRIES:
        logger.info("Final entries: {}, {}", entry, entry2)

        logger.success("Result: {}", entry * entry2)
        sys.exit()
