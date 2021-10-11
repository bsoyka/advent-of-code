from string import ascii_lowercase


def is_pangram(sentence: str) -> bool:
    return all(letter in sentence.lower() for letter in ascii_lowercase)
