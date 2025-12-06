from pathlib import Path
from typing import cast

from loguru import logger

from shared import solve_problem


def is_separator_index(col_index: int, test_grid: list[str]) -> bool:
    """Check whether a given index points to a separator column in a grid.

    Args:
        col_index: The column index to check.
        test_grid: The grid to check, given as a list of row strings.

    Returns: Whether the column at the given index is entirely space characters.
    """
    return all(line[col_index] == " " for line in test_grid)


INPUT_LINES = (Path(__file__).parent / "input.txt").read_text().splitlines()
width = max(len(line) for line in INPUT_LINES)
grid = [line.ljust(width) for line in INPUT_LINES]

raw_problems: list[list[str]] = []
current_numbers: list[str] = []
current_op: str | None = None

for col in range(width - 1, -1, -1):
    if is_separator_index(col, grid):
        raw_problems.append(cast(list[str], current_numbers + [current_op]))
        current_numbers = []
        current_op = None
        continue

    if (c := grid[-1][col]) in {"+", "*"}:
        current_op = c

    digits = [grid[row][col] for row in range(len(grid) - 1)]
    current_numbers.append("".join(digits))

# One more time for the final (leftmost) problem
raw_problems.append(cast(list[str], current_numbers + [current_op]))

result = sum(solve_problem(p) for p in raw_problems)

logger.success("Result: {}", result)
