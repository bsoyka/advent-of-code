with open("input.txt") as f:
    start = f.readlines()[0].strip()
floor = 0
for index, char in enumerate(start, start=1):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    else:
        raise ValueError(f"Unknown character: {char}")
    if floor < 0:
        print(index)
        break
