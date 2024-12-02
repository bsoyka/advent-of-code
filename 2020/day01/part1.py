import sys
from typing import List

from bsoyka_aoc_utils import get_data
from loguru import logger

TOTAL = 2020

ENTRIES: List[int] = get_data(2020, 1, func=int, split=True)
logger.debug("Loaded entries list")

for entry in ENTRIES:
    if (entry2 := TOTAL - entry) in ENTRIES:
        logger.info("Final entries: {}, {}", entry, entry2)

        logger.success("Result: {}", entry * entry2)
        sys.exit()
