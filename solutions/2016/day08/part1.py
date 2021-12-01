from re import findall

# Input data loading
from aocd import get_data

from numpy import count_nonzero, roll, zeros

instructions = get_data(year=2016, day=8).splitlines()

array = zeros([6, 50], dtype=int)

for instruction in instructions:
    x, y = map(int, findall(r"\d+", instruction))

    inst, *text = instruction.split(" ")

    if inst == "rect":
        array[:y, :x] = 1
    elif text[0] == "row":
        array[x] = roll(array[x], y)
    elif text[0] == "column":
        array[:, x] = roll(array[:, x], y)

print(count_nonzero(array))
