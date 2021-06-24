res = 202000

for _ in range(int(input())):
    total = sum([*map(int, input().split(' '))][1:])

    if total < res:
        res = total

print(res)
