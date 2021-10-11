from ..anagram import find_anagrams


def assert_test_with_same_items(word, candidates, expected):
    assert sorted(find_anagrams(word, candidates)) == sorted(expected)


def test_no_matches():
    candidates = ['hello', 'world', 'zombies', 'pants']
    expected = []

    assert_test_with_same_items('diaper', candidates, expected)


def test_detects_two_anagrams():
    candidates = ['stream', 'pigeon', 'maters']
    expected = ['stream', 'maters']

    assert_test_with_same_items('master', candidates, expected)


def test_does_not_detect_anagram_subsets():
    candidates = ['dog', 'goody']
    expected = []

    assert_test_with_same_items('good', candidates, expected)


def test_detects_anagram():
    candidates = ['enlists', 'google', 'inlets', 'banana']
    expected = ['inlets']

    assert_test_with_same_items('listen', candidates, expected)


def test_detects_three_anagrams():
    candidates = [
        'gallery',
        'ballerina',
        'regally',
        'clergy',
        'largely',
        'leading',
    ]
    expected = ['gallery', 'regally', 'largely']

    assert_test_with_same_items('allergy', candidates, expected)


def test_detects_multiple_anagrams_with_different_case():
    candidates = ['Eons', 'ONES']
    expected = ['Eons', 'ONES']

    assert_test_with_same_items('nose', candidates, expected)


def test_does_not_detect_non_anagrams_with_identical_checksum():
    candidates = ['last']
    expected = []

    assert_test_with_same_items('mass', candidates, expected)


def test_detects_anagrams_case_insensitively():
    candidates = ['cashregister', 'Carthorse', 'radishes']
    expected = ['Carthorse']

    assert_test_with_same_items('Orchestra', candidates, expected)


def test_detects_anagrams_using_case_insensitive_subject():
    candidates = ['cashregister', 'carthorse', 'radishes']
    expected = ['carthorse']

    assert_test_with_same_items('Orchestra', candidates, expected)


def test_detects_anagrams_using_case_insensitive_possible_matches():
    candidates = ['cashregister', 'Carthorse', 'radishes']
    expected = ['Carthorse']

    assert_test_with_same_items('orchestra', candidates, expected)


def test_does_not_detect_an_anagram_if_the_original_word_is_repeated():
    candidates = ['go Go GO']
    expected = []

    assert_test_with_same_items('go', candidates, expected)


def test_anagrams_must_use_all_letters_exactly_once():
    candidates = ['patter']
    expected = []

    assert_test_with_same_items('tapper', candidates, expected)


def test_words_are_not_anagrams_of_themselves_case_insensitive():
    candidates = ['BANANA', 'Banana', 'banana']
    expected = []

    assert_test_with_same_items('BANANA', candidates, expected)


def test_words_other_than_themselves_can_be_anagrams():
    candidates = ['Listen', 'Silent', 'LISTEN']
    expected = ['Silent']

    assert_test_with_same_items('LISTEN', candidates, expected)
