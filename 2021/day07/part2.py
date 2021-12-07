# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

# This solution is a bit slow, but it still gets the correct solution in
# a fairly reasonable amount of time. (Took about 19 seconds with my
# input.)

CRABS = get_data(2021, 7, func=int, split=",")
logger.debug("Loaded crabs data")

FUEL_VALS: list[tuple[int, int]] = []

for align_position in range(max(CRABS)):
    fuel: int = 0

    for crab in CRABS:
        steps = abs(crab - align_position)
        fuel += sum(range(1, steps + 1))

    FUEL_VALS.append((align_position, fuel))

_, result = min(FUEL_VALS, key=lambda x: x[1])

logger.success("Result: {}", result)
