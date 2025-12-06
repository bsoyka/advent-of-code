from pathlib import Path

from loguru import logger
from math import prod

with (Path(__file__).parent / "input.txt").open() as f:
    INPUT_DATA = [line.split() for line in f.readlines()]

raw_problems = [list(line) for line in zip(*INPUT_DATA)]


def solve_problem(input_list: list[str]) -> int:
    numbers = map(int, input_list[:-1])

    match input_list[-1]:
        case "+":
            return sum(numbers)
        case "*":
            return prod(numbers)


result = sum(solve_problem(p) for p in raw_problems)

logger.success("Result: {}", result)
