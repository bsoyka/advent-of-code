with open("input.txt") as f:
    steps = [int(line.strip()) for line in f.readlines()]
value = 0
for step in steps:
    value += step
print(value)