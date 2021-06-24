from pathlib import Path

with (Path(__file__).parent / 'input.txt').open() as f:
    gifts = [list(map(int, line.strip().split('x'))) for line in f.readlines()]


def surface_area(l, w, h):
    return (2 * l * w) + (2 * w * h) + (2 * h * l)


def smallest_side(l, w, h):
    # Multiply the smallest edges to get the smallest side
    return sorted([l, w, h])[0] * sorted([l, w, h])[1]


res = sum(surface_area(*gift) + smallest_side(*gift) for gift in gifts)

print(res)
