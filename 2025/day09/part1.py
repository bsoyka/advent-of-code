from itertools import combinations
from pathlib import Path

from loguru import logger

if __name__ == "__main__":
    RED_TILES = (Path(__file__).parent / "input.txt").read_text().splitlines()

    result = 0

    for tile1, tile2 in combinations(RED_TILES, 2):
        t1x, t1y = tile1.split(",")
        t2x, t2y = tile2.split(",")
        area = (abs(int(t1x) - int(t2x)) + 1) * (abs(int(t1y) - int(t2y)) + 1)

        if area > result:
            result = area

    logger.success("Result: {}", result)
