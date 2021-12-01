from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    rows = [line.strip() for line in f.readlines()]

trees = 0
column = 0

for row in rows:
    if row[column] == "#":
        trees += 1

    column = (column + 3) % len(row)

print(trees)
