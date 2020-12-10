from itertools import groupby


with open("input.txt") as f:
    input_lines = [line.strip() for line in f.readlines()]

groups = list(
    set("".join(list(y))) for x, y in groupby(input_lines, key=lambda x: x != "") if x
)

print(sum(len(group) for group in groups))
