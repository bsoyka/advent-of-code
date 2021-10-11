from pytest import raises

from ..grains import square, total


def raises_with_message(exception):
    return raises(exception, match=r'.+')


def test_grains_on_square_1():
    assert square(1) == 1


def test_grains_on_square_2():
    assert square(2) == 2


def test_grains_on_square_3():
    assert square(3) == 4


def test_grains_on_square_4():
    assert square(4) == 8


def test_grains_on_square_16():
    assert square(16) == 32768


def test_grains_on_square_32():
    assert square(32) == 2147483648


def test_grains_on_square_64():
    assert square(64) == 9223372036854775808


def test_square_0_raises_an_exception():
    with raises_with_message(ValueError):
        square(0)


def test_negative_square_raises_an_exception():
    with raises_with_message(ValueError):
        square(-1)


def test_square_greater_than_64_raises_an_exception():
    with raises_with_message(ValueError):
        square(65)


def test_total_number_of_grains_on_board():
    assert total() == 18446744073709551615
