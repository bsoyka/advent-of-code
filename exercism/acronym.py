from re import findall, sub


def abbreviate(words: str) -> str:
    clean_words = sub(r'[^A-Za-z0-9\s\-]', '', words).upper()
    words_list = findall(r'\w+', clean_words)
    return ''.join(word[0] for word in words_list)
