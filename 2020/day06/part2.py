from itertools import groupby
from typing import List

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

CUSTOMS_LINES: List[str] = get_data(2020, 6, split=True)
CUSTOMS_FORMS = [
    list(y) for x, y in groupby(CUSTOMS_LINES, key=lambda x: x != "") if x
]
logger.debug("Loaded customs forms data")

GROUPS_ALL = [set(group[0]).intersection(*group) for group in CUSTOMS_FORMS]

RESULT = sum(len(group) for group in GROUPS_ALL)

logger.success("Result: {}", RESULT)
