# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

ROWS = get_data(2020, 3, split=True)
logger.debug("Loaded map data")

trees, column = 0, 0

for row in ROWS:
    if row[column] == "#":
        trees += 1

    column = (column + 3) % len(row)

logger.success("Result: {}", trees)
