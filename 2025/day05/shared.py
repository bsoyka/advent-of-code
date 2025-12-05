class FreshRange:
    """A range of item IDs considered to be fresh."""

    def __init__(self, start, end):
        """Initialize a range object.

        Args:
            start: The starting ID, inclusive.
            end: The ending ID, inclusive.
        """
        self.start = start
        self.end = end

    @classmethod
    def from_input_line(cls, line: str) -> FreshRange:
        """Initialize a range object from a raw input line.

        Args:
            line: A line of input from the file.

        Returns: A range object.
        """
        start, end = map(int, line.split("-"))
        return cls(start, end)

    def __contains__(self, item_id):
        """Check whether the range contains an item.

        Args:
            item_id: The ID of the item to check.

        Returns: Whether the given item is in the ID range.
        """
        return self.start <= item_id <= self.end

    def __len__(self):
        """Calculate the number of IDs within the range.

        Returns: The size of the range.
        """
        return self.end - self.start + 1
