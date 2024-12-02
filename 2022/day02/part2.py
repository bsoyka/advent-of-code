from bsoyka_aoc_utils import get_data
from bsoyka_aoc_utils.rps import Move, Result, get_one_move
from loguru import logger

rounds: list[str] = get_data(2022, 2, split=True)
logger.debug("Loaded rounds list")


def get_move(letter: str) -> Move:
    """Convert a letter to a Move.

    Args:
        letter (str): The move from the input

    Raises:
        ValueError: The letter is not a valid move

    Returns:
        Move: The move
    """
    if letter == "A":
        return Move.ROCK

    if letter == "B":
        return Move.PAPER

    if letter == "C":
        return Move.SCISSORS

    raise ValueError(f"Invalid move: {letter}")


def get_result(letter: str) -> Result:
    """Convert a letter to a Result.

    Args:
        letter (str): The result from the input

    Raises:
        ValueError: The letter is not a valid result

    Returns:
        Result: The result
    """
    if letter == "X":
        return Result.LOSE

    if letter == "Y":
        return Result.DRAW

    if letter == "Z":
        return Result.WIN

    raise ValueError(f"Invalid result: {letter}")


score: int = 0

for round_ in rounds:
    opponent_move, result = round_.split(" ")
    opponent_move = get_move(opponent_move)
    result = get_result(result)

    player_move = get_one_move(opponent_move, result)

    score += player_move.value
    score += result.value

logger.success("Result: {}", score)
