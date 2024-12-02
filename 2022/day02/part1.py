from bsoyka_aoc_utils import get_data
from bsoyka_aoc_utils.rps import Move, get_result
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
    if letter in {"X", "A"}:
        return Move.ROCK

    if letter in {"Y", "B"}:
        return Move.PAPER

    if letter in {"Z", "C"}:
        return Move.SCISSORS

    raise ValueError(f"Invalid move: {letter}")


score: int = 0

for round_ in rounds:
    opponent_move, player_move = map(get_move, round_.split(" "))

    score += player_move.value

    result = get_result(player_move, opponent_move)

    score += result.value

logger.success("Result: {}", score)
