from re import findall
from typing import Tuple

# Input data loading
from aocd import get_data

instructions = get_data(year=2015, day=6).splitlines()

lights = [[False for _ in range(1000)] for _ in range(1000)]

for instruction in instructions:
    coordinates: Tuple[int, int, int, int] = tuple(
        map(int, findall(r"\d{1,3}", instruction))
    )

    if instruction.startswith("turn on"):
        for x in range(coordinates[0], coordinates[2] + 1):
            for y in range(coordinates[1], coordinates[3] + 1):
                lights[x][y] = True

    elif instruction.startswith("turn off"):
        for x in range(coordinates[0], coordinates[2] + 1):
            for y in range(coordinates[1], coordinates[3] + 1):
                lights[x][y] = False

    elif instruction.startswith("toggle"):
        for x in range(coordinates[0], coordinates[2] + 1):
            for y in range(coordinates[1], coordinates[3] + 1):
                lights[x][y] = not lights[x][y]

print(sum(line.count(True) for line in lights))
