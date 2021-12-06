import sys
from typing import List

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

TOTAL = 2020

ENTRIES: List[int] = get_data(2020, 1, func=int, split=True)
logger.debug("Loaded entries list")

for entry in ENTRIES:
    for entry2 in ENTRIES:
        if (entry3 := TOTAL - entry - entry2) in ENTRIES:
            logger.info("Final entries: {}, {}, {}", entry, entry2, entry3)

            logger.success("Result: {}", entry * entry2 * entry3)
            sys.exit()
