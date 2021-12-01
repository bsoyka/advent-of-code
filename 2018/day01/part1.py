from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    steps = [int(line.strip()) for line in f.readlines()]
value = sum(steps)
print(value)
