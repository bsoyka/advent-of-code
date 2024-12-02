from collections import defaultdict

from bsoyka_aoc_utils import get_data
from bsoyka_aoc_utils.lines import Line2D
from bsoyka_aoc_utils.points import Point2D
from loguru import logger

LINES_DATA: list[str] = get_data(2021, 5, split=True)

FIELD_COUNTS: defaultdict[Point2D, int] = defaultdict(int)

for line_data in LINES_DATA:
    line = Line2D.from_data(line_data)
    points = line.get_points(include_diagonals=True)

    for point in points:
        FIELD_COUNTS[point] += 1

RESULT = sum(count >= 2 for count in FIELD_COUNTS.values())

logger.success("Result: {}", RESULT)
