with open("input.txt") as f:
    start = f.readlines()[0].strip()
total = 0
for index_1, char_1 in enumerate(start):
    index_2 = (index_1 + (len(start) // 2)) % len(start)
    char_2 = start[index_2]
    if char_1 == char_2:
        total += int(char_1)
print(total)  # 1284
