import re

with open("input.txt") as f:
    lines = [line.strip() for line in f]
regex = re.compile(r"^([a-z]+) \(\d+\) -> ([a-z, ]+)$")
holding = set()
being_held = set()
for line in lines:
    if regex.match(line):
        holding.add(regex.match(line).groups()[0])
        being_held.update(set(regex.match(line).groups()[1].split(", ")))
print(holding.difference(being_held).pop())