from string import digits
import re

with open("input.txt") as f:
    start, stop = map(int, f.readlines()[0].strip().split("-"))
valid = 0
for check in range(start, stop + 1):
    repeats = 0
    if len(str(check)) != 6:
        continue
    if not re.match(r"^1*2*3*4*5*6*7*8*9*$", str(check)):
        continue
    for x in digits:
        check = str(check).replace(x*5, "")
        check = str(check).replace(x*4, "")
        check = str(check).replace(x*3, "")
        repeats += str(check).count(x * 2)
    if not repeats > 0:
        continue
    valid += 1
print(valid)  # 316