from pathlib import Path

from loguru import logger

with (Path(__file__).parent / "input.txt").open() as f:
    INPUT_ROWS = f.readlines()

logger.debug("Loaded input data")


def adjacent_positions(
    row_position: int,
    col_position: int,
    total_rows: int = len(INPUT_ROWS),
    total_cols: int = len(INPUT_ROWS[0]) - 1,  # Subtract 1 for the newline
) -> set[tuple[int, int]]:
    """Gather the adjacent grid positions to a cell.

    At most, this is the 8 cells surrounding the cell. However, this function
    accounts for cells on the edges or corners of the grid, returning fewer adjacent
    cells if applicable.

    Args:
        row_position: The row index of the cell.
        col_position: The column index of the cell.
        total_rows: The number of rows in the grid.
        total_cols: The number of columns in the grid.

    Returns: A set of the adjacent (row, col) cells to the given cell.
    """
    min_row = max(0, row_position - 1)
    max_row = min(total_rows - 1, row_position + 1)

    min_col = max(0, col_position - 1)
    max_col = min(total_cols - 1, col_position + 1)

    positions: set[tuple[int, int]] = {
        (adj_row, adj_col)
        for adj_row in range(min_row, max_row + 1)
        for adj_col in range(min_col, max_col + 1)
    }

    positions.discard((row_position, col_position))

    return positions


def forklifts_in_positions(
    positions: set[tuple[int, int]], input_data: list[str]
) -> int:
    """Calculates the number of forklifts (@s) present in the given positions.

    Args:
        positions: A set of (row, col) cells to check for forklifts.
        input_data: The list of rows given as input.

    Returns: The number of forklifts present in the given cells.
    """
    forklifts = 0

    for cell_row, cell_col in positions:
        if INPUT_ROWS[cell_row][cell_col] == "@":
            forklifts += 1

    return forklifts


result = 0

for row_index, row in enumerate(INPUT_ROWS):
    row = row.strip()

    for col_index, cell in enumerate(row):
        if cell != "@":
            continue

        adjacent_cells = adjacent_positions(row_index, col_index)
        adjacent_forklifts = forklifts_in_positions(adjacent_cells, INPUT_ROWS)

        if adjacent_forklifts < 4:
            result += 1

logger.success("Result: {}", result)
