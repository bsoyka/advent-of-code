# Input data loading
from aocd import get_data

# Simple logging
from loguru import logger

depths = list(map(int, get_data(year=2021, day=1).splitlines()))
logger.info("Loaded depths list")

result: int = 0

for index, depth in enumerate(depths):
    if index == 0:
        logger.trace("Skipping index 0, depth {}", depth)
        continue

    if depths[index - 1] < depth:
        result += 1

logger.success("Result: {}", result)
