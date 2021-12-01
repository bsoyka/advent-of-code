from string import ascii_lowercase


def bad_substrings(string: str) -> bool:
    """Check if a string contains any bad substrings

    Args:
        string (str): The string to check

    Returns:
        bool: Whether the string contains any bad substrings
    """

    return any(string.count(sub) for sub in ["ab", "cd", "pq", "xy"])


def doubles(string: str) -> int:
    """Count the number of double letters in a string

    Args:
        string (str): The string to count double letters in

    Returns:
        int: The number of double letters in the string
    """

    return sum(string.count(pair * 2) for pair in ascii_lowercase)


def vowels(string: str) -> int:
    """Count the number of vowels in a string

    Args:
        string (str): The string to count vowels in

    Returns:
        int: The number of vowels in the string
    """

    return sum(string.count(vowel) for vowel in ["a", "e", "i", "o", "u"])
