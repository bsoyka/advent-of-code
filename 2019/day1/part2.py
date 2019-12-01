import math
def func(module):
	rs = 0 - module
	ch = module + 0
	while ch > 0:
		rs += ch
		ch = math.floor(ch/3)-2
	return rs
with open("1-1.txt") as f:
	lines = [func(int(line.strip())) for line in f.readlines()]
print(sum(lines))
