from pathlib import Path

from loguru import logger
from shared import adjacent_positions, forklifts_in_positions

with (Path(__file__).parent / "input.txt").open() as f:
    INPUT_ROWS = f.readlines()

logger.debug("Loaded input data")


def get_removable_forklifts(input_data: list[str]) -> set[tuple[int, int]]:
    """Get the currently removable forklifts in a grid.

    Args:
        input_data: The list of rows given as input.

    Returns: A set of (row, col) cells containing forklifts that can be removed.
    """
    removable: set[tuple[int, int]] = set()

    for row_index, row in enumerate(input_data):
        row = row.strip()

        for col_index, cell in enumerate(row):
            if cell != "@":
                continue

            adjacent_cells = adjacent_positions(row_index, col_index)
            adjacent_forklifts = forklifts_in_positions(adjacent_cells, input_data)

            if adjacent_forklifts < 4:
                removable.add((row_index, col_index))

    return removable


removed = 0
current_data = [row for row in INPUT_ROWS]

while removable_forklifts := get_removable_forklifts(current_data):
    for forklift_row, forklift_col in removable_forklifts:
        row = current_data[forklift_row].rstrip("\n")
        row = row[:forklift_col] + "." + row[forklift_col + 1 :]
        current_data[forklift_row] = row + "\n"
        removed += 1

logger.success("Result: {}", removed)
