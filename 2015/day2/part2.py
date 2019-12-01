with open("input.txt") as f:
    start = [list(map(int, line.strip().split("x"))) for line in f.readlines()]
print(start)


def surface_area(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * h * l


def smallest_perimeter(l, w, h):
    return sorted([l, w, h])[0]*2 + sorted([l, w, h])[1]*2


res = 0
for l, w, h in start:
    res += smallest_perimeter(l, w, h) + l*w*h
print(res)
