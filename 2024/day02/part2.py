from part1 import check_level as check_level_simple
from utils import load_and_check_levels


def check_level(level: list[int], *, recursive: bool = False) -> bool:
    """Checks whether a level is strictly increasing or decreasing, including by
    checking whether removing one value would make the condition true.

    Args:
        level (list): The values in the level.
        recursive (bool): Whether this function is being called recursively. If
            not, the function checks whether removing one value helps.

    Returns:
        bool: Whether the level is "safe" by our standards.
    """
    # First, check using the rules from Part 1.
    if check_level_simple(level):
        return True

    if not recursive:
        # Attempt to remove single values to make the level safe.
        for exclude_index in range(len(level)):
            test_level = level[:exclude_index] + level[exclude_index + 1:]
            if check_level(test_level, recursive=True):
                return True

    # Either:
    # - The function was called recursively and the level isn't safe.
    # - Removing single values didn't make the level safe.
    return False


if __name__ == '__main__':
    load_and_check_levels(test_function=check_level)
