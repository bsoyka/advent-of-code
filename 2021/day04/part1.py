import sys
from itertools import groupby

# Simple logging
from loguru import logger

# Personal utilities
from bsoyka_aoc_utils import get_data

DATA_LINES: list[str] = get_data(2021, 4, split_lines=True)


class BingoSpace:
    """A bingo space.

    Args:
        number (int): The number on the bingo space.

    Attributes:
        number (int): The number on the bingo space.
        marked (bool): Whether the bingo space has been marked.
    """

    def __init__(self, number: int):
        self.number = number
        self.marked: bool = False

    def mark(self):
        """Mark the bingo space."""
        self.marked = True


class BingoCard:
    def __init__(self, data: list[list[BingoSpace]]):
        self.data = data

    @classmethod
    def from_data(cls, data: list[str]):
        """Create a bingo card from the given data.

        Args:
            data (list[str]): The data to create the card from.

        Returns:
            BingoCard: The created bingo card.
        """
        card_data = [
            [BingoSpace(int(number)) for number in line.split()]
            for line in data
        ]

        return cls(card_data)

    def mark_number(self, number: int):
        """Mark the bingo space with the given number.

        Args:
            number (int): The number to mark.
        """
        for row in self.data:
            for space in row:
                if space.number == number:
                    space.mark()

    @property
    def won(self) -> bool:
        """bool: Whether the bingo card has won.

        A bingo card has won if it has a full row or column of marked
        spaces.
        """
        for row in self.data:
            if all(space.marked for space in row):
                return True

        return any(
            all(space.marked for space in column) for column in zip(*self.data)
        )

    @property
    def unmarked_sum(self) -> int:
        """int: The sum of the unmarked spaces on the bingo card."""
        return sum(
            space.number
            for row in self.data
            for space in row
            if not space.marked
        )


DATA_LINE_GROUPS = [
    list(y) for x, y in groupby(DATA_LINES, key=lambda x: x != "") if x
]

CALL_NUMBERS = [
    int(number) for number in DATA_LINE_GROUPS.pop(0)[0].split(",")
]

BINGO_CARDS = [BingoCard.from_data(data) for data in DATA_LINE_GROUPS]

for number in CALL_NUMBERS:
    for card in BINGO_CARDS:
        card.mark_number(number)

        if card.won:
            RESULT = card.unmarked_sum * number

            logger.success("Result: {}", RESULT)
            sys.exit()
