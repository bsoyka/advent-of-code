from pathlib import Path

with (Path(__file__).parent / "input.txt").open() as f:
    gifts = [list(map(int, line.strip().split("x"))) for line in f.readlines()]


def surface_area(l, w, h):
    return (2 * l * w) + (2 * w * h) + (2 * h * l)


def smallest_perimeter(l, w, h):
    # Multiply each of the smallest edges by 2 to get the smallest perimeter
    return sorted([l, w, h])[0] * 2 + sorted([l, w, h])[1] * 2


res = sum(smallest_perimeter(l, w, h) + (l * w * h) for l, w, h in gifts)

print(res)
