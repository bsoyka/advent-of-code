from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Point2D:
    """A two-dimensional point.

    Args:
        x (int/float): The x-coordinate of the point.
        y (int/float): The y-coordinate of the point.

    Attributes:
        x (int/float): The x-coordinate of the point.
        y (int/float): The y-coordinate of the point.
    """

    x: int | float
    y: int | float

    def distance(self, other: Optional[Point2D] = None) -> int | float:
        """Get the Manhattan distance to another two-dimensional point.

        Args:
            other (Point2D, optional): The other point. Defaults to the
                origin, or (0,0).

        Returns:
            int/float: The distance in units.
        """
        if other is None:
            other = Point2D(0, 0)

        return abs(self.x - other.x) + abs(self.y - other.y)
