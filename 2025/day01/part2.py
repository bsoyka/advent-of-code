from pathlib import Path
from typing import Literal

from loguru import logger

with (Path(__file__).parent / "input.txt").open() as f:
    INPUT_TEXT = f.readlines()
logger.debug("Loaded instruction data")


def complete_move(
    starting_position: int, direction_str: str, steps: int
) -> tuple[int | Literal[0], int]:
    """Executes a full instruction.

    Args:
        starting_position: The numerical starting position.
        direction_str: The direction to move in (R is positive, L is negative)
        steps: The total number of steps to take

    Returns: A tuple containing the final position and the number of 0s.
    """

    position = starting_position
    zeroes = 0

    each_step = 1 if direction_str == "R" else -1

    for _ in range(steps):
        position = (position + each_step) % 100  # keep in [0, 99]
        if position == 0:
            zeroes += 1

    return position, zeroes


location = 50
result = 0

for instruction in INPUT_TEXT:
    direction, distance = instruction[0], int(instruction[1:])
    logger.debug(instruction.strip())

    location, zeroes = complete_move(location, direction, distance)

    result += zeroes

logger.success("Result: {}", result)
