from collections import Counter
from typing import List

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

DIAGNOSTICS: List[str] = get_data(2021, 3, split=True)
logger.debug("Loaded diagnostics list")

NUMBER_LENGTH = len(DIAGNOSTICS[0])

column_bit_counts = [Counter() for _ in range(NUMBER_LENGTH)]

# Get the number of 0s and 1s in each column
for row in DIAGNOSTICS:
    for index, col in enumerate(row):
        # Add the bit to the counter, keeping it as a string
        column_bit_counts[index][col] += 1

gamma: str = ""
epsilon: str = ""

for col_counts in column_bit_counts:
    # Add the most common bit to the gamma string
    gamma += col_counts.most_common()[0][0]

    # Add the least common bit to the epsilon string
    epsilon += col_counts.most_common()[-1][0]

# Convert from binary strings to integers
GAMMA_RESULT = int(gamma, base=2)
EPSILON_RESULT = int(epsilon, base=2)

logger.info("Final gamma rate: {} ({})", GAMMA_RESULT, gamma)
logger.info("Final epsilon rate: {} ({})", EPSILON_RESULT, epsilon)

logger.success("Result: {}", GAMMA_RESULT * EPSILON_RESULT)
