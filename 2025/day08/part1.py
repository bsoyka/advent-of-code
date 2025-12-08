from itertools import combinations
from math import prod, sqrt
from pathlib import Path

from loguru import logger


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


def find_junction_in_circuit_list(junction: str, circuits: list[set[str]]) -> int:
    """Find the circuit containing a given junction in a list of circuits.

    Args:
        junction: The junction to search for.
        circuits: The list of circuits to search.

    Returns: The index of the circuit containing the given junction.

    Raises:
        ValueError: The junction was not found in the list of circuits.
    """
    for i, circuit in enumerate(circuits):
        if junction in circuit:
            return i

    raise ValueError


if __name__ == "__main__":
    INPUT_LINES = (Path(__file__).parent / "input.txt").read_text().splitlines()
    circuits = [
        {
            j,
        }
        for j in INPUT_LINES
    ]
    junctions_to_link = pair_junctions_by_distance(INPUT_LINES, 1000)

    for _, junction1, junction2 in junctions_to_link:
        j1_circuit_index = find_junction_in_circuit_list(junction1, circuits)
        j2_circuit_index = find_junction_in_circuit_list(junction2, circuits)

        j1_circuit, j2_circuit = circuits[j1_circuit_index], circuits[j2_circuit_index]

        joined_circuit = j1_circuit.union(j2_circuit)

        for i in sorted({j1_circuit_index, j2_circuit_index}, reverse=True):
            # Pop starting with the latest to avoid the earlier element shifting
            circuits.pop(i)

        circuits.append(joined_circuit)

    largest_sizes = sorted((len(c) for c in circuits), reverse=True)[:3]
    logger.success("Result: {}", prod(largest_sizes))
