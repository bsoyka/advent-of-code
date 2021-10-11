from pytest import raises


from ..phone_number import PhoneNumber


def raises_with_message(exception):
    return raises(exception, match=r'.+')


def test_cleans_the_number():
    number = PhoneNumber('(223) 456-7890').number
    assert number == '2234567890'


def test_cleans_numbers_with_dots():
    number = PhoneNumber('223.456.7890').number
    assert number == '2234567890'


def test_cleans_numbers_with_multiple_spaces():
    number = PhoneNumber('223 456   7890   ').number
    assert number == '2234567890'


def test_invalid_when_9_digits():
    with raises_with_message(ValueError):
        PhoneNumber('123456789')


def test_invalid_when_11_digits_does_not_start_with_a_1():
    with raises_with_message(ValueError):
        PhoneNumber('22234567890')


def test_valid_when_11_digits_and_starting_with_1():
    number = PhoneNumber('12234567890').number
    assert number == '2234567890'


def test_valid_when_11_digits_and_starting_with_1_even_with_punctuation():
    number = PhoneNumber('+1 (223) 456-7890').number
    assert number == '2234567890'


def test_invalid_when_more_than_11_digits():
    with raises_with_message(ValueError):
        PhoneNumber('321234567890')


def test_invalid_with_letters():
    with raises_with_message(ValueError):
        PhoneNumber('123-abc-7890')


def test_invalid_with_punctuations():
    with raises_with_message(ValueError):
        PhoneNumber('123-@:!-7890')


def test_invalid_if_area_code_starts_with_0():
    with raises_with_message(ValueError):
        PhoneNumber('(023) 456-7890')


def test_invalid_if_area_code_starts_with_1():
    with raises_with_message(ValueError):
        PhoneNumber('(123) 456-7890')


def test_invalid_if_exchange_code_starts_with_0():
    with raises_with_message(ValueError):
        PhoneNumber('(223) 056-7890')


def test_invalid_if_exchange_code_starts_with_1():
    with raises_with_message(ValueError):
        PhoneNumber('(223) 156-7890')


def test_invalid_if_area_code_starts_with_0_on_valid_11_digit_number():
    with raises_with_message(ValueError):
        PhoneNumber('1 (023) 456-7890')


def test_invalid_if_area_code_starts_with_1_on_valid_11_digit_number():
    with raises_with_message(ValueError):
        PhoneNumber('1 (123) 456-7890')


def test_invalid_if_exchange_code_starts_with_0_on_valid_11_digit_number():
    with raises_with_message(ValueError):
        PhoneNumber('1 (223) 056-7890')


def test_invalid_if_exchange_code_starts_with_1_on_valid_11_digit_number():
    with raises_with_message(ValueError):
        PhoneNumber('1 (223) 156-7890')


def test_area_code():
    number = PhoneNumber('2234567890')
    assert number.area_code == '223'


def test_pretty_print():
    number = PhoneNumber('2234567890')
    assert number.pretty() == '(223)-456-7890'


def test_pretty_print_with_full_us_phone_number():
    number = PhoneNumber('12234567890')
    assert number.pretty() == '(223)-456-7890'
