count = int(input())
towers = [*map(int, input().split(" "))]

good = 0

for index, tower in enumerate(towers):
    if index in {0, count - 1}:
        continue

    if towers[index - 1] < tower < towers[index + 1]:
        good += 1

print(good)
