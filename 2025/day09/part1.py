from itertools import combinations
from pathlib import Path

from loguru import logger

if __name__ == "__main__":
    RED_TILES = (Path(__file__).parent / "input.txt").read_text().splitlines()

    result = 0

    for tile1, tile2 in combinations(RED_TILES, 2):
        t1x, t1y = map(int, tile1.split(","))
        t2x, t2y = map(int, tile2.split(","))
        area = (abs(t1x - t2x) + 1) * (abs(t1y - t2y) + 1)

        result = max(result, area)

    logger.success("Result: {}", result)
