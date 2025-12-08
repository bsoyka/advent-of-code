from math import prod
from pathlib import Path

from loguru import logger
from shared import find_junction_in_circuit_list, pair_junctions_by_distance

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
