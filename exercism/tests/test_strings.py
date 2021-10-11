from pytest import mark

from ..strings import (
    add_prefix_un,
    make_word_groups,
    noun_to_verb,
    remove_suffix_ness,
)


@mark.parametrize(
    ('word', 'result'),
    {
        ('happy', 'unhappy'),
        ('manageable', 'unmanageable'),
        ('fold', 'unfold'),
        ('eaten', 'uneaten'),
        ('avoidable', 'unavoidable'),
        ('usual', 'unusual'),
    },
)
def test_add_prefix_un(word: str, result: str):
    assert add_prefix_un(word) == result


@mark.parametrize(
    ['vocab_words', 'result'],
    {
        (
            'en,circle,fold,close,joy,lighten,tangle,able,code,culture',
            'en :: encircle :: enfold :: enclose :: enjoy :: enlighten :: '
            'entangle :: enable :: encode :: enculture',
        ),
        (
            'pre,serve,dispose,position,requisite,digest,natal,addressed,'
            'adolescent,assumption,mature,compute',
            'pre :: preserve :: predispose :: preposition :: prerequisite :: '
            'predigest :: prenatal :: preaddressed :: preadolescent :: '
            'preassumption :: premature :: precompute',
        ),
        (
            'auto,didactic,graph,mate,chrome,centric,complete,echolalia,'
            'encoder,biography',
            'auto :: autodidactic :: autograph :: automate :: autochrome :: '
            'autocentric :: autocomplete :: autoecholalia :: autoencoder :: '
            'autobiography',
        ),
        (
            'inter,twine,connected,dependent,galactic,action,stellar,cellular,'
            'continental,axial,operative,disciplinary',
            'inter :: intertwine :: interconnected :: interdependent :: '
            'intergalactic :: interaction :: interstellar :: intercellular :: '
            'intercontinental :: interaxial :: interoperative :: '
            'interdisciplinary',
        ),
    },
)
def test_make_word_groups(vocab_words: str, result: str):
    assert make_word_groups(vocab_words.split(',')) == result


@mark.parametrize(
    ('word', 'result'),
    {
        ('heaviness', 'heavy'),
        ('sadness', 'sad'),
        ('softness', 'soft'),
        ('crabbiness', 'crabby'),
        ('lightness', 'light'),
        ('artiness', 'arty'),
        ('edginess', 'edgy'),
    },
)
def test_remove_suffix_ness(word: str, result: str):
    assert remove_suffix_ness(word) == result


@mark.parametrize(
    ('sentence', 'index', 'result'),
    {
        ('Look at the bright sky.', -2, 'brighten'),
        ('His expression went dark.', -1, 'darken'),
        ('The bread got hard after sitting out.', 3, 'harden'),
        ('The butter got soft in the sun.', 3, 'soften'),
        ('Her face was filled with light.', -1, 'lighten'),
        ('The morning fog made everything damp with mist.', -3, 'dampen'),
        ('He cut the fence pickets short by mistake.', 5, 'shorten'),
        ('Charles made weak crying noises.', 2, 'weaken'),
        ('The black oil got on the white dog.', 1, 'blacken'),
    },
)
def test_noun_to_verb(sentence: str, index: int, result: str):
    assert noun_to_verb(sentence, index) == result
