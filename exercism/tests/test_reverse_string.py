from ..reverse_string import reverse


def test_an_empty_string():
    assert reverse('') == ''


def test_a_word():
    assert reverse('robot') == 'tobor'


def test_a_capitalized_word():
    assert reverse('Ramen') == 'nemaR'


def test_a_sentence_with_punctuation():
    assert reverse("I'm hungry!") == "!yrgnuh m'I"


def test_a_palindrome():
    assert reverse('racecar') == 'racecar'


def test_an_even_sized_word():
    assert reverse('drawer') == 'reward'
