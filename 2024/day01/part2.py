from pathlib import Path

from loguru import logger

first = []
second = []
with (Path(__file__).parent / "input.txt").open() as f:
    lines = f.readlines()

for line in lines:
    next_first, next_second = line.split()
    first.append(int(next_first))
    second.append(int(next_second))

logger.debug("Loaded input lines")

result = 0

for first_val in first:
    result += first_val * second.count(first_val)

logger.success("Result: {}", result)
