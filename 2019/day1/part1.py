with open("input.txt") as f:
    lines = [int(line.strip()) // 3 - 2 for line in f.readlines()]
print(sum(lines))  # 3271095
