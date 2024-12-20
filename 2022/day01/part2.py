from typing import Literal

from bsoyka_aoc_utils import get_data
from loguru import logger

CALORIES: list[int | Literal[""]] = get_data(
    2022, 1, func=lambda x: int(x) if len(x) > 0 else x, split=True
)
logger.debug("Loaded calories list")

elves: list[int] = [0]
index: int = 0

for calorie in CALORIES:
    if calorie == "":
        index += 1
        elves.append(0)
    else:
        elves[index] += calorie

logger.debug("Calculated {} elf calorie totals", len(elves))

top_three: list[int] = sorted(elves, reverse=True)[:3]

logger.success("Result: {}", sum(top_three))
