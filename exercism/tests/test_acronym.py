from ..acronym import abbreviate


def test_basic():
    assert abbreviate('Portable Network Graphics') == 'PNG'


def test_lowercase_words():
    assert abbreviate('Ruby on Rails') == 'ROR'


def test_punctuation():
    assert abbreviate('First In, First Out') == 'FIFO'


def test_all_caps_word():
    assert abbreviate('GNU Image Manipulation Program') == 'GIMP'


def test_punctuation_without_whitespace():
    assert abbreviate('Complementary metal-oxide semiconductor') == 'CMOS'


def test_very_long_abbreviation():
    assert (
        abbreviate(
            'Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me'
        )
        == 'ROTFLSHTMDCOALM'
    )


def test_consecutive_delimiters():
    assert abbreviate('Something - I made up from thin air') == 'SIMUFTA'


def test_apostrophes():
    assert abbreviate("Halley's Comet") == 'HC'


def test_underscore_emphasis():
    assert abbreviate('The Road _Not_ Taken') == 'TRNT'
