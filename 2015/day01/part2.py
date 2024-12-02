import sys

from aocd import get_data

instructions = get_data(year=2015, day=1)

floor: int = 0

for index, char in enumerate(instructions, start=1):
    if char == "(":
        floor += 1
    else:
        floor -= 1

    if floor < 0:
        print(index)
        sys.exit()
