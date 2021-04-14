input()

a = input()
b = input()

safe = 0

for x, y in zip(a, b):
    if x == "1" or y == "1":
        continue

    safe += 1

print(safe)
