from itertools import cycle
from re import match

from bsoyka_aoc_utils import get_data
from loguru import logger

BOARD_SIZE = 10
DIE_SIDES = 100
END_SCORE = 1000
ROLLS_PER_MOVE = 3


class Player:
    """A Dirac Dice player.

    Args:
        position (int): The player's starting position on the game board.

    Attributes:
        position (int): The player's current position on the game board.
        score (int): The player's total score.
    """

    def __init__(self, position: int) -> None:
        self.position = position
        self.score: int = 0

    def _move_forward(self, spaces: int) -> None:
        """Move the player forward around the board.

        Args:
            spaces (int): The number of spaces to move.
        """
        self.position = (self.position + spaces) % BOARD_SIZE

        if self.position == 0:
            self.position = 10

    def move(self, spaces: int) -> int:
        """Move the player forward and increase their score.

        Args:
            spaces (int): The number of spaces to move.

        Returns:
            int: The new score.
        """
        self._move_forward(spaces)
        self.score += self.position

        return self.score


class Die:
    """An iterable deterministic die for the Dirac Dice game.

    Attributes:
        roll_count (int): The number of rolls the die has made.
    """

    def __init__(self) -> None:
        self._iterable = cycle(range(1, DIE_SIDES + 1))
        self.roll_count: int = 0

    def roll(self, times: int) -> int:
        """Rolls the die.

        Args:
            times (int): The number of times to roll the die.

        Returns:
            int: The total number from the roll.
        """
        self.roll_count += times

        return sum(next(self._iterable) for _ in range(times))


players = [
    Player(int(match(r".+(\d+)$", player_line).groups()[0]))
    for player_line in get_data(2021, 21, split=True)
]
logger.debug("Loaded players data")

players_cycle = cycle(players)

die = Die()

while True:
    current_player = next(players_cycle)

    roll = die.roll(ROLLS_PER_MOVE)
    new_score = current_player.move(roll)

    if new_score >= END_SCORE:
        break

low_score = min(player.score for player in players)

result = low_score * die.roll_count

logger.success("Result: {}", result)
