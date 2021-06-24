from itertools import groupby
from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    input_lines = [line.strip() for line in f.readlines()]

groups = [list(y) for x, y in groupby(input_lines, key=lambda x: x != "") if x]

groups_all = [set(group[0]).intersection(*group) for group in groups]

print(sum(len(group) for group in groups_all))
