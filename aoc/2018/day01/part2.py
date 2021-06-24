from pathlib import Path

with (Path(__file__).parent / 'input.txt').open() as f:
    steps = [int(line.strip()) for line in f.readlines()]
value = 0
past = {0}
found = False
while not found:
    for step in steps:
        value += step
        if value in past:
            print(value)
            found = True
            break
        past.add(value)
