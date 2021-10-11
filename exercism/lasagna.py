EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining in minutes"""

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time in minutes based on the number of
    layers"""

    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(
    number_of_layers: int, elapsed_bake_time: int
) -> int:
    """Calculate the elapsed time cooking based on the number of layers
    and the elapsed bake time"""

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
