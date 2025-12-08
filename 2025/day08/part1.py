from itertools import combinations
from math import sqrt
from pathlib import Path


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


def pair_junctions_by_distance(
    junctions: list[str], limit: int = 1000
) -> list[tuple[float, str, str]]:
    """Makes pairs of junctions in ascending order by the distance between them.

    Args:
        junctions: The list of junctions to consider.
        limit: The maximum number of pairs to return.

    Returns: A list of tuples of (distance, junction1, junction2).
    """
    junction_pairs = combinations(junctions, 2)
    distance_results = [
        (calculate_distance(j1, j2), j1, j2) for j1, j2 in junction_pairs
    ]

    return sorted(distance_results)[:limit]


if __name__ == "__main__":
    INPUT_LINES = (Path(__file__).parent / "input.txt").read_text().splitlines()

    junctions_to_link = pair_junctions_by_distance(INPUT_LINES, 1000)

    # TODO: use list of distances and pairs to connect circuits
    # TODO: find 3 largest circuits
    # TODO: multiply sizes of 3 largest circuits to get result
