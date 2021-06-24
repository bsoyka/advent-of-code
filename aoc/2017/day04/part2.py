from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    start = [
        ["".join(sorted(word)) for word in line.strip().split(" ")]
        for line in f.readlines()
    ]
result = sum(len(password) == len(set(password)) for password in start)
print(result)
