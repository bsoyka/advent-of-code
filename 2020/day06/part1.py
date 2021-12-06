from itertools import groupby
from typing import List

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

CUSTOMS_LINES: List[str] = get_data(2020, 6, split=True)
CUSTOMS_FORMS = [
    set("".join(y))
    for x, y in groupby(CUSTOMS_LINES, key=lambda x: x != "")
    if x
]
logger.debug("Loaded customs forms data")

RESULT = sum(len(group) for group in CUSTOMS_FORMS)

logger.success("Result: {}", RESULT)
