from pathlib import Path
from re import findall

with (Path(__file__).parent / "input.txt").open() as f:
    instructions = [line.strip() for line in f.readlines()]

lights = [[0 for _ in range(1000)] for _ in range(1000)]

for instruction in instructions:
    coordinates = tuple(map(int, findall(r"\d{1,3}", instruction)))

    if instruction.startswith("turn on"):
        for x in range(coordinates[0], coordinates[2] + 1):
            for y in range(coordinates[1], coordinates[3] + 1):
                lights[x][y] += 1

    elif instruction.startswith("turn off"):
        for x in range(coordinates[0], coordinates[2] + 1):
            for y in range(coordinates[1], coordinates[3] + 1):
                lights[x][y] -= 1 if lights[x][y] > 0 else 0

    elif instruction.startswith("toggle"):
        for x in range(coordinates[0], coordinates[2] + 1):
            for y in range(coordinates[1], coordinates[3] + 1):
                lights[x][y] += 2

print(sum(sum(line) for line in lights))
