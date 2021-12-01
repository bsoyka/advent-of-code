# Input data loading
from aocd import get_data

instructions = get_data(year=2015, day=1)

floor: int = 0

for char in instructions:
    if char == "(":
        floor += 1
    else:
        floor -= 1

print(floor)
