from itertools import combinations
from pathlib import Path

from math import sqrt


def calculate_distance(junction1: str, junction2: str) -> float:
    """Calculate the straight-line distance between two junctions.

    This is the square root of the sum of the squares of the differences of the
    coordinate values for each dimension.

    That is: sqrt((j1x-j2x)^2 + (j1y-j2y)^2 + (j1z-j2z)^2)

    Args:
        junction1: The first junction, given in the input format.
        junction2: The first junction, given in the input format.

    Returns: The distance between the two points given.
    """
    junction1_coords = map(int, junction1.split(","))
    junction2_coords = map(int, junction2.split(","))

    dimension_coord_pairs = zip(junction1_coords, junction2_coords)

    return sqrt(sum((j1x - j2x) ** 2 for j1x, j2x in dimension_coord_pairs))


INPUT_LINES = (Path(__file__).parent / "input.txt").read_text().splitlines()

junction_pairs = combinations(INPUT_LINES, 2)
distance_results = [(calculate_distance(j1, j2), j1, j2) for j1, j2 in junction_pairs]

distance_results = sorted(distance_results)[:1000]

# TODO: use list of distances and pairs to connect circuits
# TODO: find 3 largest circuits
# TODO: multiply sizes of 3 largest circuits to get result
