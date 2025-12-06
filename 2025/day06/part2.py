from pathlib import Path

from loguru import logger
from math import prod

with (Path(__file__).parent / "input.txt").open() as f:
    INPUT_LINES = [line.rstrip("\n") for line in f]


def solve_problem(input_list: list[str]) -> int:
    numbers = map(int, input_list[:-1])

    match input_list[-1]:
        case "+":
            return sum(numbers)
        case "*":
            return prod(numbers)


def is_separator_index(col_index: int, test_grid: list[str]) -> bool:
    return all(line[col_index] == " " for line in test_grid)


width = max(len(line) for line in INPUT_LINES)
grid = [line.ljust(width) for line in INPUT_LINES]

raw_problems: list[list[str]] = []
current_numbers: list[str] = []
current_op: str | None = None

for col in range(width - 1, -1, -1):
    if is_separator_index(col, grid):
        raw_problems.append(current_numbers + [current_op])
        current_numbers = []
        current_op = None
        continue

    if (c := grid[-1][col]) in {"+", "*"}:
        current_op = c

    digits = [grid[row][col] for row in range(len(grid) - 1)]
    current_numbers.append("".join(digits))

# One more time for the final (leftmost) problem
raw_problems.append(current_numbers + [current_op])

result = sum(solve_problem(p) for p in raw_problems)

logger.success("Result: {}", result)
