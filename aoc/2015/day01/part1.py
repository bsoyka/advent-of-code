from pathlib import Path

with (Path(__file__).parent / 'input.txt').open() as f:
    instructions = f.read().strip()

floor = 0

for char in instructions:
    if char == '(':
        floor += 1
    else:
        floor -= 1

print(floor)
