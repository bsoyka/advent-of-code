from pathlib import Path

from loguru import logger

START_MACHINE = "you"
END_MACHINE = "out"


def get_paths_starting_at_machine(
    search_start: str, search_end: str, connections: dict[str, list[str]]
) -> int:
    """Determine the number of paths between given start and end machines.

    This function works recursively through our directed acyclic graph (DAG) of
    machines, calling itself for each first-level connection from the given node,
    repeating until reaching the ending node on all branches of recursion.

    Args:
        search_start: The machine to start with.
        search_end: The machine to end with.
        connections: The device connections given in the input.

    Returns:
        The number of possible paths from the starting machine to the ending machine.
    """
    total_paths = 0

    for connected_device in connections[search_start]:
        if connected_device == search_end:
            total_paths += 1
        else:
            total_paths += get_paths_starting_at_machine(
                connected_device, search_end, connections
            )

    return total_paths


if __name__ == "__main__":
    INPUT_LINES = (Path(__file__).parent / "input.txt").read_text().splitlines()

    devices: dict[str, list[str]] = {}
    for input_line in INPUT_LINES:
        input_parts = input_line.split()
        devices[input_parts[0][:-1]] = input_parts[1:]

    logger.debug("Loaded input data")

    result = get_paths_starting_at_machine(START_MACHINE, END_MACHINE, devices)
    logger.success("Result: {}", result)
