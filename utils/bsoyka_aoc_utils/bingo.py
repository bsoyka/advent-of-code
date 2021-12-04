from dataclasses import dataclass


@dataclass
class BingoSpace:
    """A bingo space.

    Args:
        number (int): The number on the bingo space.
        marked (bool): Whether the bingo space has been marked.

    Attributes:
        number (int): The number on the bingo space.
        marked (bool): Whether the bingo space has been marked.
    """

    number: int
    marked: bool = False

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


def count_not_won_cards(cards: list[BingoCard]) -> int:
    """Count the number of cards that have not won.

    Args:
        cards (list[BingoCard]): The cards to count.

    Returns:
        int: The number of cards that have not won.
    """
    return sum(not card.won for card in cards)
