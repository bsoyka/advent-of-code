from pathlib import Path
from typing import Iterable

from loguru import logger

from shared import FreshRange

with (Path(__file__).parent / "input.txt").open() as f:
    RAW_FRESH_RANGES, RAW_AVAILABLE_IDS = f.read().split("\n\n")

logger.debug("Loaded input data")


def is_item_in_any_range(item_id: int, ranges: Iterable[FreshRange]) -> bool:
    return any(test_range.contains(item_id) for test_range in ranges)


fresh_ranges = list(map(FreshRange.from_input_line, RAW_FRESH_RANGES.split("\n")))
available_ids = map(int, RAW_AVAILABLE_IDS.split("\n"))
result = 0

logger.success(
    "Result: {}",
    sum(
        is_item_in_any_range(available_id, fresh_ranges)
        for available_id in available_ids
    ),
)
