# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

DEPTHS = get_data(2021, 1, func=int, split=True)
logger.debug("Loaded depths list")

result: int = 0

# Get the value of window A first
compare_value = DEPTHS[0] + DEPTHS[1] + DEPTHS[2]

# Loop through the starting indices of each following window
for index in range(1, len(DEPTHS) - 2):
    current_sum = DEPTHS[index] + DEPTHS[index + 1] + DEPTHS[index + 2]

    if current_sum > compare_value:
        result += 1

    compare_value = current_sum  # Store the current sum to compare next

logger.success("Result: {}", result)
