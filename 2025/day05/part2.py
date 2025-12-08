from pathlib import Path

from loguru import logger
from shared import FreshRange

with (Path(__file__).parent / "input.txt").open() as f:
    RAW_INPUT = f.readlines()

logger.debug("Loaded input data")


def add_range(new_line: str, existing_ranges: list[FreshRange]) -> None:
    """Add an item ID range from input to the list of unique ranges.

    This modifies the given list in place, adding the new range in sorted order and
    reconciling any overlaps if needed.

    Args:
        new_line: The new line of input to process, as given in the input file.
        existing_ranges: The current list of unique ID ranges.

    Returns:
        None
    """
    new_range = FreshRange.from_input_line(new_line)

    merged: list[FreshRange] = []
    inserted_new_range = False

    for old_range in existing_ranges:
        # Old range is completely before new range
        if old_range.end < new_range.start - 1:
            merged.append(old_range)

        # Old range is completely after new range
        elif old_range.start > new_range.end + 1:
            if not inserted_new_range:
                merged.append(new_range)
                inserted_new_range = True
            merged.append(old_range)

        # Old and new ranges touch/overlap in some way, so merge them into the new range
        else:
            new_range.start = min(new_range.start, old_range.start)
            new_range.end = max(new_range.end, old_range.end)

    if not inserted_new_range:
        merged.append(new_range)

    existing_ranges.clear()
    existing_ranges.extend(merged)


unique_fresh_ranges: list[FreshRange] = []

for line in RAW_INPUT:
    # Fresh ranges are terminated with a blank line, and we don't need available IDs
    if line == "\n":
        break

    add_range(line.strip(), unique_fresh_ranges)

logger.success(
    "Result: {}", sum(len(fresh_range) for fresh_range in unique_fresh_ranges)
)
