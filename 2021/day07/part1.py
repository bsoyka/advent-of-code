from statistics import median

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

CRABS = get_data(2021, 7, func=int, split=",")
logger.debug("Loaded crabs data")

# Finding the best alignment position can be done by getting the median
# of the crab positions.

align_position: int = int(median(CRABS))

fuel: int = sum(abs(crab - align_position) for crab in CRABS)

logger.success("Result: {}", fuel)
