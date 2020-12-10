from pathlib import Path
from sys import exit

with (Path(__file__).parent / "input.txt").open() as f:
    instructions = f.read().strip()

floor = 0

for index, char in enumerate(instructions, instructions=1):
    if char == "(":
        floor += 1
    else:
        floor -= 1

    if floor < 0:
        print(index)  # 1771
        exit()
