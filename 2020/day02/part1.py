from typing import Tuple

from bsoyka_aoc_utils import get_data
from loguru import logger


def process_line(line: str) -> Tuple[int, int, str, str]:
    raw_split = line.split()

    min_count, max_count = map(int, raw_split[0].split("-"))
    letter = raw_split[1][0]
    password = raw_split[2]

    if min_count <= password.count(letter) <= max_count:
        return 1

    return 0


ENTRIES = get_data(2020, 2, func=process_line, split=True)

logger.success("Result: {}", sum(ENTRIES))
