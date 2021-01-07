name = input()
names = [input() for _ in range(5)]

print("Y" if name in names else "N")
