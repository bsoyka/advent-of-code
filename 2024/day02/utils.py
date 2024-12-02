from pathlib import Path
from typing import Callable

from loguru import logger


def load_and_check_levels(*, test_function: Callable[[list[int]], bool]) -> None:
    """Runs the main program, loading levels from a file and printing a result.

    Args:
        test_function (Callable): The function to use in checking levels.
    """
    levels: list[list[int]] = []
    with (Path(__file__).parent / "input.txt").open() as f:
        for line in f.readlines():
            levels.append(list(map(int, line.split(" "))))

    logger.debug("Loaded {} levels", len(levels))

    safe_levels = 0
    for level in levels:
        if test_function(level):
            safe_levels += 1

    logger.success("Result: {}", safe_levels)
