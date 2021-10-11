from pytest import mark

from ..exchange import (
    exchange_money,
    exchangeable_value,
    get_change,
    get_number_of_bills,
    get_value_of_bills,
    non_exchangeable_value,
)


@mark.parametrize(
    ('budget', 'exchange_rate', 'output'),
    {(100000, 0.84, 119047), (700000, 10.1, 69306)},
)
def test_exchange_money(budget: int, exchange_rate: float, output: int):
    assert int(exchange_money(budget, exchange_rate)) == output


@mark.parametrize(
    ('budget', 'exchanging_value', 'output'),
    {(463000, 5000, 458000), (1250, 120, 1130), (15000, 1380, 13620)},
)
def test_get_change(budget: float, exchanging_value: int, output: float):
    assert get_change(budget, exchanging_value) == output


@mark.parametrize(
    ('denomination', 'number_of_bills', 'output'),
    {(10000, 128, 1280000), (50, 360, 18000), (200, 200, 40000)},
)
def test_get_value_of_bills(
    denomination: int, number_of_bills: int, output: int
):
    assert get_value_of_bills(denomination, number_of_bills) == output


@mark.parametrize(
    ('budget', 'denomination', 'output'),
    {(163270, 50000, 3), (54361, 1000, 54)},
)
def test_get_number_of_bills(budget: float, denomination: int, output: int):
    assert get_number_of_bills(budget, denomination) == output


@mark.parametrize(
    ('budget', 'exchange_rate', 'spread', 'denomination', 'output'),
    {
        (100000, 10.61, 10, 1, 8568),
        (1500, 0.84, 25, 40, 1400),
        (470000, 1050, 30, 700, 0),
        (470000, 0.00000009, 30, 700, 4017094016600),
        (425.33, 0.0009, 30, 700, 363300),
    },
)
def test_exchangeable_value(
    budget: float,
    exchange_rate: float,
    spread: int,
    denomination: int,
    output: int,
):
    assert (
        exchangeable_value(budget, exchange_rate, spread, denomination)
        == output
    )


@mark.parametrize(
    ('budget', 'exchange_rate', 'spread', 'denomination', 'output'),
    {
        (100000, 10.61, 10, 1, 0),
        (1500, 0.84, 25, 40, 28),
        (425.33, 0.0009, 30, 700, 229),
        (12000, 0.0096, 10, 50, 13),
    },
)
def test_non_exchangeable_value(
    budget: float,
    exchange_rate: float,
    spread: int,
    denomination: int,
    output: int,
):
    assert (
        non_exchangeable_value(budget, exchange_rate, spread, denomination)
        == output
    )
