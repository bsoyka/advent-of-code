from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    steps = [int(line.strip()) for line in f.readlines()]
value = 0
for step in steps:
    value += step
print(value)
