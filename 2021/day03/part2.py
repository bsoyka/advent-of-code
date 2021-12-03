from typing import List

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

DIAGNOSTICS: List[str] = get_data(2021, 3, split_lines=True)
logger.debug("Loaded diagnostics list")

NUMBER_LENGTH = len(DIAGNOSTICS[0])

# Make a copy of the diagnostics for each value
oxygen_possible = DIAGNOSTICS.copy()
co2_possible = DIAGNOSTICS.copy()

# Loop through the bits
for bit_index in range(NUMBER_LENGTH):
    if len(oxygen_possible) > 1:
        # Narrow down the oxygen possibilities, count the 0s and 1s
        oxy_one_count, oxy_zero_count = 0, 0

        for entry in oxygen_possible:
            if entry[bit_index] == "1":
                oxy_one_count += 1
            else:
                oxy_zero_count += 1

        MOST_COMMON = "1" if oxy_one_count >= oxy_zero_count else "0"

        # Remove the ones that don't match this most common bit
        oxygen_possible = [
            entry
            for entry in oxygen_possible
            if entry[bit_index] == MOST_COMMON
        ]

    if len(co2_possible) > 1:
        # Narrow down the CO2 possibilities, count the 0s and 1s
        co2_one_count, co2_zero_count = 0, 0

        for entry in co2_possible:
            if entry[bit_index] == "1":
                co2_one_count += 1
            else:
                co2_zero_count += 1

        MOST_COMMON = "0" if co2_one_count >= co2_zero_count else "1"

        # Remove the ones that don't match this most common bit
        co2_possible = [
            entry for entry in co2_possible if entry[bit_index] == MOST_COMMON
        ]

# Convert from binary strings to integers
OXYGEN_RESULT = int(oxygen_possible[0], base=2)
CO2_RESULT = int(co2_possible[0], base=2)

logger.info("Final oxygen reading: {} ({})", OXYGEN_RESULT, oxygen_possible[0])
logger.info("Final CO2 reading: {} ({})", CO2_RESULT, co2_possible[0])

logger.success("Result: {}", OXYGEN_RESULT * CO2_RESULT)
