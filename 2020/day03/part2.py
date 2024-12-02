from bsoyka_aoc_utils import get_data
from loguru import logger

SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

ROWS = get_data(2020, 3, split=True)
logger.debug("Loaded map data")

result: int = 1

for slope_index, (right, down) in enumerate(SLOPES):
    trees, column, row = 0, 0, 0

    while row < len(ROWS):
        if ROWS[row][column] == "#":
            trees += 1

        row += down
        column = (column + right) % len(ROWS[0])

    result *= trees

logger.success("Result: {}", result)
