from pathlib import Path

SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

with (Path(__file__).parent / "input.txt").open() as f:
    rows = [line.strip() for line in f.readlines()]

result = 1

for slope, (right, down) in enumerate(SLOPES):
    trees = 0
    column = 0
    row = 0

    while row < len(rows):
        if rows[row][column] == "#":
            trees += 1

        row += down
        column = (column + right) % len(rows[0])

    result *= trees

print(result)
