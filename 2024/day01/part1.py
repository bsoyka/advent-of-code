from pathlib import Path

from loguru import logger

first = []
second = []
with (Path(__file__).parent / "input.txt").open() as f:
    lines = f.readlines()

for line in lines:
    next_first, next_second = line.strip().split()
    first.append(int(next_first))
    second.append(int(next_second))

logger.debug("Loaded input lines")

result = 0

first.sort()
second.sort()

for i in range(len(first)):
    result += abs(first[i] - second[i])

logger.success("Result: {}", result)
