from itertools import combinations
from pathlib import Path
from typing import Sequence

from loguru import logger

with (Path(__file__).parent / "input.txt").open() as f:
    BATTERY_BANKS = f.readlines()

logger.debug("Loaded input data")


def max_joltage(bank_values: Sequence[int]) -> int:
    """Calculate the maximum joltage possible with a battery bank.

    For Part 1, this is done with brute force, gathering all possible pairs of
    batteries and finding the max joltage from there.

    The algorithm used for Part 2 can easily be adapted to work for this part,
    but it's a little more complex and would only result in a miniscule improvement
    in execution time (yet observable; about 1.17 times faster).

    Args:
        bank_values: A sequence of numbers representing the batteries in the bank.

    Returns:
        The total possible joltage from the bank.
    """
    # Get all possible pairs of batteries
    perms = set(combinations(bank_values, 2))

    return max(p[0] * 10 + p[1] for p in perms)


result = 0

for raw_bank in BATTERY_BANKS:
    bank = list(map(int, raw_bank.strip()))

    result += max_joltage(bank)

logger.success("Result: {}", result)
