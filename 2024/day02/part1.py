from pathlib import Path
from typing import Callable

from loguru import logger


def check_level(level: list[int]) -> bool:
    """Checks whether a level is strictly increasing or decreasing.

    Args:
        level (list): The values in the level.

    Returns:
        bool: Whether the level is "safe" by our standards.
    """
    if all(1 <= (level[i + 1] - level[i]) <= 3 for i in range(len(level) - 1)):
        # Level is increasing by 1-3 each value
        return True
    elif all(1 <= (level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1)):
        # Level is decreasing by 1-3 each value
        return True

    return False


def load_and_check_levels(*, test_function: Callable[
    [list[int]], bool] = check_level) -> None:
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
        if check_level(level):
            safe_levels += 1

    logger.success("Result: {}", safe_levels)


if __name__ == '__main__':
    load_and_check_levels()
