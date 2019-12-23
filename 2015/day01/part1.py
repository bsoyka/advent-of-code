with open("input.txt") as f:
    start = f.readlines()[0].strip()
floor = 0
for char in start:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    else:
        raise ValueError(f"Unknown character: {char}")
print(floor)