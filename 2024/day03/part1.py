from pathlib import Path
from re import findall

from loguru import logger

SEARCH_EXPRESSION = r"mul\((\d+),(\d+)\)"

with (Path(__file__).parent / "input.txt").open() as f:
    INPUT_TEXT = f.read()
logger.debug("Loaded instruction data")

result = 0
for found in findall(SEARCH_EXPRESSION, INPUT_TEXT):
    first, second = tuple(map(int, found))
    result += first * second

logger.success("Result: {}", result)
