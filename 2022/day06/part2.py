from bsoyka_aoc_utils import get_data
from loguru import logger

MARKER_LENGTH = 14

data: str = get_data(2022, 6)
logger.debug("Loaded input data")

for index in range(MARKER_LENGTH - 1, len(data)):
    marker = data[index - MARKER_LENGTH + 1 : index + 1]  # Get last few characters

    # If all characters in the marker are unique
    if len(set(marker)) == MARKER_LENGTH:
        result = index + 1
        logger.success("Result: {}", result)
        break
