input()

a = input()
b = input()

safe = sum(x != "1" and y != "1" for x, y in zip(a, b))

print(safe)
