from typing import List


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    results = []
    sorted_word = sorted(word.upper())

    for candidate in candidates:
        # Skip if the candidate is the same as the word
        if word.upper() == candidate.upper():
            continue

        # Check if the candidate has the same letters as the word
        if sorted_word == sorted(candidate.upper()):
            results.append(candidate)

    return results
