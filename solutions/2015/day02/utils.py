def smallest_perimeter(length: int, width: int, height: int) -> int:
    """Multiply the smallest edges of a gift by 2 to get its smallest
    perimeter

    Args:
        length (int): The length of the gift
        width (int): The width of the gift
        height (int): The height of the gift

    Returns:
        int: The smallest perimeter of the gift
    """

    return (
        sorted([length, width, height])[0] * 2
        + sorted([length, width, height])[1] * 2
    )


def smallest_side(length: int, width: int, height: int) -> int:
    """Multiply the smallest edges of a gift to get its smallest side

    Args:
        length (int): The length of the gift
        width (int): The width of the gift
        height (int): The height of the gift

    Returns:
        int: The area of the smallest side of the gift
    """

    return (
        sorted([length, width, height])[0] * sorted([length, width, height])[1]
    )


def surface_area(length: int, width: int, height: int) -> int:
    """Calculate the surface area of a gift given its dimensions

    Args:
        length (int): The length of the gift
        width (int): The width of the gift
        height (int): The height of the gift

    Returns:
        int: The surface area of the gift
    """

    return (2 * length * width) + (2 * width * height) + (2 * height * length)
