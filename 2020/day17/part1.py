import collections
import itertools
from pathlib import Path

active = []

with (Path(__file__).parent / "input.txt").open() as f:
    for row, line in enumerate(line.strip() for line in f.readlines()):
        for col, char in enumerate(line):
            if char == "#":
                active.append((col, row, 0))


def active_neighbors(active, x, y, z):
    result = 0

    for nx in range(x - 1, x + 2):
        for ny in range(y - 1, y + 2):
            for nz in range(z - 1, z + 2):
                if (nx, ny, nz) in active:
                    result += 1

    return result


for _ in range(6):
    new_active = set()

    xs, ys, zs = zip(*active)

    for x in range(min(xs) - 1, max(xs) + 2):
        for y in range(min(ys) - 1, max(ys) + 2):
            for z in range(min(zs) - 1, max(zs) + 2):
                if (x, y, z) in active:
                    if active_neighbors(active, x, y, z) in (2, 3):
                        new_active.add((x, y, z))
                elif active_neighbors(active, x, y, z) == 3:
                    new_active.add((x, y, z))

    active = list(new_active)

    print(len(active))

# needs to be 287, pt 2 1724
