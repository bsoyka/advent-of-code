from pathlib import Path

from loguru import logger

manifold_rows = (Path(__file__).parent / "input.txt").read_text().splitlines()

# Skip every other row as they're all dots
manifold_rows = manifold_rows[::2]

current_tachyons = [False for _ in manifold_rows[0]]
splits = 0

for row in manifold_rows:
    for char_index, character in enumerate(row):
        if character == "S":
            # Tachyon source
            current_tachyons[char_index] = True
        elif character == "^" and current_tachyons[char_index]:
            # Tachyon splitter
            current_tachyons[char_index] = False
            current_tachyons[char_index - 1] = True
            current_tachyons[char_index + 1] = True

            splits += 1

logger.success("Result: {}", splits)
