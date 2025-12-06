from pathlib import Path

from loguru import logger

from shared import solve_problem

INPUT_LINES = (Path(__file__).parent / "input.txt").read_text().splitlines()
raw_problems = [list(col) for col in zip(*(line.split() for line in INPUT_LINES))]

result = sum(solve_problem(p) for p in raw_problems)
logger.success("Result: {}", result)
