from pathlib import Path
from typing import Sequence

from loguru import logger

with (Path(__file__).parent / "input.txt").open() as f:
    BATTERY_BANKS = f.readlines()

logger.debug("Loaded input data")


def max_joltage(bank_values: Sequence[int], batteries_to_use: int = 12) -> int:
    """Calculate the maximum joltage possible with a battery bank.

    For Part 2, brute force isn't reasonable. Instead, we use a greedy algorithm,
    iterating through the values in the battery bank. For each value, we remove any
    smaller values already selected at the end of our solution (up until we are
    unable to drop any more values), then add the current value to our solution stack.

    Since we only ever drop a digit if a larger digit appears to its right while we
    still have drops allowed, every drop improves the part of the solution we've
    calculated so far. For example, a final joltage value starting with 88 will
    always be better than one starting with 818 as long as we still have the same
    number of total digits.

    Args:
        bank_values: A sequence of numbers representing the batteries in the bank.
        batteries_to_use: The exact number of battery digits to select.

    Returns:
        The total possible joltage from the bank.
    """
    drops_allowed = len(bank_values) - batteries_to_use
    stack: list[int] = []

    for battery in bank_values:
        # Drop the most recently added batteries if the current one is larger,
        # until we are unable to drop a value.
        while drops_allowed > 0 and stack and stack[-1] < battery:
            stack.pop()
            drops_allowed -= 1

        stack.append(battery)

    # Trim more off the end if needed
    stack = stack[:batteries_to_use]

    return int("".join(map(str, stack)))


result = 0

for raw_bank in BATTERY_BANKS:
    bank = list(map(int, raw_bank.strip()))

    result += max_joltage(bank)

logger.success("Result: {}", result)
