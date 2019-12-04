from string import digits

with open("input.txt") as f:
    start, stop = map(int, f.readlines()[0].strip().split("-"))
valid = 0
for check in range(start, stop + 1):
    repeats = 0
    if len(str(check)) != 6:
        continue
    for x in digits:
        repeats += str(check).count(x * 2)
    if not repeats > 0:
        continue
    if not all(x <= y for x, y in zip(str(check), str(check)[1:])):
        continue
    valid += 1
print(valid)  # 511
