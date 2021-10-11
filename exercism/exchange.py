def exchange_money(budget: float, exchange_rate: float) -> float:
    """Calculate the value of exchanged currency with specified budget"""

    return budget / exchange_rate


def get_change(budget: float, exchanging_value: int) -> float:
    """Calculate remaining budget after exchanging set amount"""

    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculate the value of the specified bills"""

    return denomination * number_of_bills


def get_number_of_bills(budget: float, denomination: int) -> int:
    """Calculate the number of the specified denomination you can get
    using the given budget"""

    return budget // denomination


def exchangeable_value(
    budget: float, exchange_rate: float, spread: int, denomination: int
) -> int:
    """Calculate value after exchange using only one denomination"""

    actual_exchange_rate = exchange_rate * (1 + (spread / 100))
    exchanged_value = exchange_money(budget, actual_exchange_rate)
    number_of_bills = get_number_of_bills(exchanged_value, denomination)

    return get_value_of_bills(denomination, number_of_bills)


def non_exchangeable_value(
    budget: float, exchange_rate: float, spread: int, denomination: int
) -> int:
    """Calculate value lost after exchange due to denomination"""

    actual_exchange_rate = exchange_rate * (1 + (spread / 100))
    exchanged_value = exchange_money(budget, actual_exchange_rate)
    number_of_bills = get_number_of_bills(exchanged_value, denomination)
    bill_value = get_value_of_bills(denomination, number_of_bills)

    return int(exchanged_value - bill_value)
