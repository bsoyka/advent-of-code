from typing import List
from re import sub


def add_prefix_un(word: str) -> str:
    return 'un' + word


def make_word_groups(vocab_words: List[str]) -> str:
    prefix, *words = vocab_words

    results = [prefix]

    for word in words:
        results.append(prefix + word)

    return ' :: '.join(results)


def remove_suffix_ness(word: str) -> str:
    result = word[:-4]

    if result[-1] == 'i':
        return result[:-1] + 'y'

    return result


def noun_to_verb(sentence: str, index: int) -> str:
    words = sentence.split()

    # Get the word, removing all non-alpha characters
    word = sub(r'[^a-z]', '', words[index].lower())

    return word + 'en'
