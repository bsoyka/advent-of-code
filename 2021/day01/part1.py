from bsoyka_aoc_utils import get_data
from loguru import logger

DEPTHS = get_data(2021, 1, func=int, split=True)
logger.debug("Loaded depths list")

result: int = 0

for index, depth in enumerate(DEPTHS):
    if index == 0:
        logger.trace("Skipping index 0, depth {}", depth)
        continue

    if DEPTHS[index - 1] < depth:
        result += 1

logger.success("Result: {}", result)
