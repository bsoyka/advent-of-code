from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    start = [line.strip().split(" ") for line in f.readlines()]
result = 0
for password in start:
    if len(password) == len(set(password)):
        result += 1
print(result)
