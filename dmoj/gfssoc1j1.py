height = int(input())

plushies = 0

for _ in range(int(input())):
    if int(input()) >= height:
        plushies += 1

print(plushies)
