# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

MAP_LINES = get_data(2021, 9, split=True)
logger.debug("Loaded map data")

MAP_HEIGHT = len(MAP_LINES)
MAP_WIDTH = len(MAP_LINES[0])

result: int = 0

for row, line in enumerate(MAP_LINES):
    for column, height in enumerate(line):
        adjacent_heights = []

        if row > 0:
            # Not on the top row
            adjacent_heights.append(MAP_LINES[row - 1][column])
        if row < MAP_HEIGHT - 1:
            # Not on the bottom row
            adjacent_heights.append(MAP_LINES[row + 1][column])

        if column > 0:
            # Not on the left column
            adjacent_heights.append(MAP_LINES[row][column - 1])
        if column < MAP_WIDTH - 1:
            # Not on the right column
            adjacent_heights.append(MAP_LINES[row][column + 1])

        if all(
            height < adjacent_height for adjacent_height in adjacent_heights
        ):
            result += int(height) + 1

logger.success("Result: {}", result)
