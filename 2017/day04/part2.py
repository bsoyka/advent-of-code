with open("input.txt") as f:
    start = [["".join(sorted(word)) for word in line.strip().split(" ")] for line in f.readlines()]
result = 0
for password in start:
    if len(password) == len(set(password)):
        result += 1
print(result)  # 251