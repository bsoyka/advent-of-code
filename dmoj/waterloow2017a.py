n = int(input())
r = 0

for t in range(1, n + 1):
    for b in range(1, n + 1):
        if t != b:
            r += 1

print(r)
