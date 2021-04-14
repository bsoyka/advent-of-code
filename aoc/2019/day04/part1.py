import re
from pathlib import Path
from string import digits

with (Path(__file__).parent / "input.txt").open() as f:
    start, stop = map(int, f.readlines()[0].strip().split("-"))
valid = 0
for check in range(start, stop + 1):
    check = str(check)
    repeats = 0
    if len(check) != 6:
        continue
    for x in digits:
        repeats += check.count(x * 2)
    if not repeats > 0:
        continue
    if not re.match(r"^1*2*3*4*5*6*7*8*9*$", check):
        continue
    valid += 1
print(valid)
