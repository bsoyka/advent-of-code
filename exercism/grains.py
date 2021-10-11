def square(number: int) -> int:
    """Calculate the number of grains on a square"""

    if not 1 <= number <= 64:
        raise ValueError('Square number must be between 1 and 64')

    return 2 ** (number - 1)


def total():
    """Calculate the total number of grains on the board"""

    return sum(square(i) for i in range(1, 65))
