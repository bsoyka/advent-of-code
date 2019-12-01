import math
with open("input.txt") as f:
	lines = [math.floor(int(line.strip())/3)-2 for line in f.readlines()]
print(sum(lines))
