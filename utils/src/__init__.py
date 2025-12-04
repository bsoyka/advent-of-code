"""Personal utilities for solving Advent of Code challenges"""

from typing import Any, Callable, Optional

from aocd import get_data as _get_data

__all__ = ("get_data",)


def get_data(
    year: int,
    day: int,
    *,
    func: Optional[Callable[[str], Any]] = None,
    split: Optional[bool | str] = False,
) -> Any:
    """Get and clean the data for a specific Advent of Code day.

    Args:
        year (int): The event year.
        day (int): The challenge day.
        func (Callable): A function to call for each line (or the entire
            input if not splitting). Default is None.
        split (bool, optional): The character(s) to split the input by,
            or True to split by newlines. Defaults to False.
    """
    raw_data = _get_data(year=year, day=day)  # Get the raw data as a string

    if split is not False:
        if isinstance(split, str):
            data = raw_data.split(split)
        else:
            data = raw_data.splitlines()  # Split by newlines if needed

        if func:
            data = list(map(func, data))  # Map each line to the given type
    elif func:
        data = func(raw_data)  # Not splitting by lines, map to given type

    return data
