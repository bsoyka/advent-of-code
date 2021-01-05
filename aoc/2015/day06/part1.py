from pathlib import Path
from re import findall

with (Path(__file__).parent / "input.txt").open() as f:
    instructions = [line.strip() for line in f.readlines()]

lights = [[False for _ in range(1000)] for _ in range(1000)]

for instruction in instructions:
    coordinates = tuple(map(int, findall(r"\d{1,3}", instruction)))

    if instruction.startswith("turn on"):
        for x in range(coordinates[0], coordinates[2]+1):
            for y in range(coordinates[1], coordinates[3]+1):
                lights[x][y] = True

    elif instruction.startswith("turn off"):
        for x in range(coordinates[0], coordinates[2]+1):
            for y in range(coordinates[1], coordinates[3]+1):
                lights[x][y] = False

    elif instruction.startswith("toggle"):
        for x in range(coordinates[0], coordinates[2]+1):
            for y in range(coordinates[1], coordinates[3]+1):
                lights[x][y] = False if lights[x][y] else True

print(sum(line.count(True) for line in lights))
