import re


def abbreviate(words):
    clean_words = re.sub(r"[^A-Za-z0-9\s\-]", "", words).upper()
    words_list = re.findall(r"\w+", clean_words)
    abbr = [word[0] for word in words_list]
    return "".join(abbr)
