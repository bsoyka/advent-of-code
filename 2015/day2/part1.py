with open("input.txt") as f:
    start = [list(map(int, line.strip().split("x"))) for line in f.readlines()]
print(start)


def surface_area(l, w, h):
    return 2 * l * w + 2 * w * h + 2 * h * l


def smallest_side(l, w, h):
    return sorted([l, w, h])[0] * sorted([l, w, h])[1]


res = 0
for gift in start:
    res += surface_area(*gift) + smallest_side(*gift)
print(res)
