height = int(input())

plushies = sum(int(input()) >= height for _ in range(int(input())))

print(plushies)
