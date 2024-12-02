from re import findall

from aocd import get_data

triangles = [
    list(map(int, findall(r"\d+", line.strip())))
    for line in get_data(year=2016, day=3).splitlines()
]

VALID = 0

for triangle in triangles:
    if triangle[0] + triangle[1] <= triangle[2]:
        continue

    if triangle[1] + triangle[2] <= triangle[0]:
        continue

    if triangle[0] + triangle[2] <= triangle[1]:
        continue

    VALID += 1

print(VALID)
