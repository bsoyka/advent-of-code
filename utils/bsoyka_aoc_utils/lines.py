from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .points import Point2D


@dataclass
class Line2D:
    """A straight two-dimensional line.

    Args:
        start (Point2D): The starting point of the line.
        end (Point2D): The ending point of the line.

    Attributes:
        start (Point2D): The starting point of the line.
        end (Point2D): The ending point of the line.
    """

    start: Point2D
    end: Point2D

    @classmethod
    def from_data(cls, data: str) -> Line2D:
        """Create a line object from an input line.

        Args:
            data (str): The data to create the line from, formatted as
                "x1,y1 -> x2,y2".

        Returns:
            Line2D: The created bingo card.
        """
        start, end = data.split(" -> ")

        start = Point2D(*map(int, start.split(",")))
        end = Point2D(*map(int, end.split(",")))

        return cls(start, end)

    def get_points(self, *, include_diagonals: bool = False) -> Optional[list[Point2D]]:
        """Get the points of the line.

        Keyword Args:
            include_diagonals (bool, optional): Whether to include
                diagonal points. Defaults to False.

        Returns:
            list[Point2D], optional: The points of the line. Defaults to
                None.
        """
        if self.start.x == self.end.x:
            # The line is vertical.

            min_y, max_y = min(self.start.y, self.end.y), max(self.start.y, self.end.y)

            return [Point2D(self.start.x, y) for y in range(min_y, max_y + 1)]

        if self.start.y == self.end.y:
            # The line is horizontal.

            min_x, max_x = min(self.start.x, self.end.x), max(self.start.x, self.end.x)

            return [Point2D(x, self.start.y) for x in range(min_x, max_x + 1)]

        # The line is a 45 degrees diagonal.
        if include_diagonals:

            if self.start.x > self.end.x:
                # The line is going from right to left.

                min_x, max_x = self.end.x, self.start.x
                min_y, max_y = self.end.y, self.start.y
            else:
                # The line is going from left to right.

                min_x, max_x = self.start.x, self.end.x
                min_y, max_y = self.start.y, self.end.y

            return [
                Point2D(x, min_y + (x - min_x) * (max_y - min_y) // (max_x - min_x))
                for x in range(min_x, max_x + 1)
            ]

        return None
