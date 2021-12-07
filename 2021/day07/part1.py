# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

CRABS = get_data(2021, 7, func=int, split=",")
logger.debug("Loaded crabs data")

FUEL_VALS: list[tuple[int, int]] = []

for align_position in range(max(CRABS)):
    fuel: int = sum(abs(crab - align_position) for crab in CRABS)

    FUEL_VALS.append((align_position, fuel))

_, result = min(FUEL_VALS, key=lambda x: x[1])

logger.success("Result: {}", result)
