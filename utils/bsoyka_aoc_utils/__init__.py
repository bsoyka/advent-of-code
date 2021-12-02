"""Personal utilities for solving Advent of Code challenges"""

from typing import Any, Callable, Optional

# Input data loading
from aocd import get_data as _get_data


def get_data(
    year: int,
    day: int,
    *,
    func: Optional[Callable[[str], Any]] = None,
    split_lines: Optional[bool] = False,
) -> Any:
    """Get and clean the data for a specific Advent of Code day.

    Args:
        year (int): The event year.
        day (int): The challenge day.
        func (Callable): A function to call for each line (or the entire
            input if not splitting). Default is None.
        split_lines (bool, optional): Whether to split the input by
            newlines. Defaults to False.
    """

    raw_data = _get_data(year=year, day=day)  # Get the raw data as a string

    if split_lines:
        data = raw_data.splitlines()  # Split by newlines if needed

        if func:
            data = list(map(func, data))  # Map each line to the given type
    elif func:
        data = func(raw_data)  # Not splitting by lines, map to given type

    return data
