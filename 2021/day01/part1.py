# Input data loading
from aocd import get_data

# Simple logging
from loguru import logger

depths = list(map(int, get_data(year=2021, day=1).splitlines()))
logger.debug("Loaded depths list")

result = sum(
    1 if depths[index - 1] < depth else 0
    for index, depth in enumerate(depths)
    if index != 0
)
logger.debug("Calculated result")

logger.success(result)
