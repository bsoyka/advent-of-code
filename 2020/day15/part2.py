from collections import defaultdict, deque
from pathlib import Path

input_text = (Path(__file__).parent / "input.txt").read_text()
numbers = list(map(int, input_text.split(",")))

called = defaultdict(lambda: deque([], maxlen=2))

last = numbers[-1]

for i, number in enumerate(numbers, start=1):
    called[number].append(i)

for turn in range(len(numbers)+1, 30_000_001):
    if len(called[last]) < 2:
        last = 0
    else:
        last = called[last][-1] - called[last][-2]

    called[last].append(turn)

print(last)
