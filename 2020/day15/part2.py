from pathlib import Path

input_text = (Path(__file__).parent / "input.txt").read_text()

numbers = list(map(int, input_text.split(",")))

for _ in range(30_000_000 - len(numbers)):
    try:
        numbers.append(numbers[::-1][1:].index(numbers[-1]) + 1)
    except:
        numbers.append(0)

print(numbers[-1])
