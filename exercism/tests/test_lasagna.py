from typing import Callable

from pytest import mark

from ..lasagna import (
    EXPECTED_BAKE_TIME,
    bake_time_remaining,
    elapsed_time_in_minutes,
    preparation_time_in_minutes,
)


def test_expected_bake_time():
    assert EXPECTED_BAKE_TIME == 40


@mark.parametrize(
    ('time', 'remaining'),
    {
        (1, 39),
        (2, 38),
        (5, 35),
        (10, 30),
        (15, 25),
        (23, 17),
        (33, 7),
        (39, 1),
    },
)
def test_bake_time_remaining(time: int, remaining: int):
    assert bake_time_remaining(time) == remaining


@mark.parametrize(
    ('layers', 'time'),
    {
        (1, 2),
        (2, 4),
        (5, 10),
        (8, 16),
        (11, 22),
        (15, 30),
    },
)
def test_preparation_time_in_minutes(layers: int, time: int):
    assert preparation_time_in_minutes(layers) == time


@mark.parametrize(
    ('layers', 'bake_time', 'total_time'),
    {
        (1, 3, 5),
        (2, 7, 11),
        (5, 8, 18),
        (8, 4, 20),
        (11, 15, 37),
        (15, 20, 50),
    },
)
def test_elapsed_time_in_minutes(layers: int, bake_time: int, total_time: int):
    assert elapsed_time_in_minutes(layers, bake_time) == total_time


@mark.parametrize(
    'function',
    {
        bake_time_remaining,
        preparation_time_in_minutes,
        elapsed_time_in_minutes,
    },
)
def test_docstrings_were_written(function: Callable):
    assert function.__doc__ is not None
