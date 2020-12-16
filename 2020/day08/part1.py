from pathlib import Path
from re import match

with (Path(__file__).parent / "input.txt").open() as f:
    instructions = [line.strip() for line in f.readlines()]

accumulator, current = 0, 0

run = [False for _ in instructions]

while True:
    if run[current]:
        print(accumulator)
        break

    instruction_match = match(r"([a-z]{3}) ([+\-]\d+)", instructions[current])
    command, value = instruction_match.group(1), int(instruction_match.group(2))

    run[current] = True

    if command == "acc":
        accumulator += value
    elif command == "jmp":
        current += value - 1

    current += 1
    if current == len(instructions):
        break
