from bsoyka_aoc_utils import get_data
from loguru import logger

NOTE_LINES: list[str] = get_data(2021, 8, split=True)
logger.debug("Loaded notes data")

result: int = 0

for line in NOTE_LINES:
    _, output = line.split(" | ")  # Only get the output
    output = output.split()  # Split into each segment list

    # The number of segments for 1, 4, 7, and 8 are all unique, so the
    # number of segments can be used to find the digit in those cases.

    result += sum(len(x) in (2, 3, 4, 7) for x in output)

logger.success("Result: {}", result)
