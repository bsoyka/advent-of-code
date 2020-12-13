from pathlib import Path
from re import findall

import numpy as np
from advent_of_code_ocr import convert_6

with (Path(__file__).parent / "input.txt").open() as f:
    instructions = [instruction.strip() for instruction in f.readlines()]

array = np.zeros([6, 50], dtype=int)

for instruction in instructions:
    x, y = map(int, findall(r"\d+", instruction))

    inst, *text = instruction.split(" ")

    if inst == "rect":
        array[:y, :x] = 1
    elif text[0] == "row":
        array[x] = np.roll(array[x], y)
    elif text[0] == "column":
        array[:, x] = np.roll(array[:, x], y)

print(
    convert_6(
        "\n".join(map("".join, array.astype(str))), fill_pixel="1", empty_pixel="0"
    )
)
