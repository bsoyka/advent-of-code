from pathlib import Path

from loguru import logger
from shared import adjacent_positions, forklifts_in_positions

with (Path(__file__).parent / "input.txt").open() as f:
    INPUT_ROWS = f.readlines()

logger.debug("Loaded input data")

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
