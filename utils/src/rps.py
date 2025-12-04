from enum import Enum


class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3


def get_result(move1: Move, move2: Move) -> Result:
    """Determine Player 1's result in a round.

    Args:
        move1 (Move): Player 1's move
        move2 (Move): Player 2's move

    Returns:
        Result: Player 1's result
    """
    if move1 == move2:
        return Result.DRAW

    if move1 == Move.ROCK:
        return Result.LOSE if move2 == Move.PAPER else Result.WIN

    if move1 == Move.PAPER:
        return Result.LOSE if move2 == Move.SCISSORS else Result.WIN

    if move1 == Move.SCISSORS:
        return Result.LOSE if move2 == Move.ROCK else Result.WIN


def get_one_move(move2: Move, result: Result) -> Move:
    """Get Player 1's move given Player 2's move and the outcome.

    Args:
        move2 (Move): Player 2's move
        result (Result): Player 1's result

    Returns:
        Move: Player 1's move
    """
    if result == Result.DRAW:
        return move2

    if result == Result.LOSE:
        if move2 == Move.ROCK:
            return Move.SCISSORS

        if move2 == Move.PAPER:
            return Move.ROCK

        if move2 == Move.SCISSORS:
            return Move.PAPER

    if result == Result.WIN:
        if move2 == Move.ROCK:
            return Move.PAPER

        if move2 == Move.PAPER:
            return Move.SCISSORS

        if move2 == Move.SCISSORS:
            return Move.ROCK
