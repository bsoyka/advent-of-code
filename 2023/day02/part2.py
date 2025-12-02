from math import prod

from bsoyka_aoc_utils import get_data
from loguru import logger

from utils import CubeGame

if __name__ == "__main__":
    GAME_LINES: list[str] = get_data(2023, 2, split=True)
    logger.debug("Loaded game lines")

    result = 0
    for game_string in GAME_LINES:
        game = CubeGame(game_string)
        result += prod(game.minimum_cubes_by_color.values())

    logger.success("Result: {}", result)
