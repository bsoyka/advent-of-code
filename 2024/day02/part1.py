from utils import load_and_check_levels


def check_level(level: list[int]) -> bool:
    """Checks whether a level is strictly increasing or decreasing.

    Args:
        level (list): The values in the level.

    Returns:
        bool: Whether the level is "safe" by our standards.
    """
    if all(1 <= (level[i + 1] - level[i]) <= 3 for i in range(len(level) - 1)):
        # Level is increasing by 1-3 each value
        return True
    elif all(1 <= (level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1)):
        # Level is decreasing by 1-3 each value
        return True

    return False


if __name__ == '__main__':
    load_and_check_levels(test_function=check_level)
