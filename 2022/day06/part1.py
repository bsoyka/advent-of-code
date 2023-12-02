from pathlib import Path

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

MARKER_LENGTH = 4

data: str = get_data(2022, 6)
logger.debug("Loaded input data")

for index in range(MARKER_LENGTH - 1, len(data)):
    marker = data[
        index - MARKER_LENGTH + 1 : index + 1
    ]  # Get last few characters

    # If all characters in the marker are unique
    if len(set(marker)) == MARKER_LENGTH:
        result = index + 1
        logger.success("Result: {}", result)
        break
