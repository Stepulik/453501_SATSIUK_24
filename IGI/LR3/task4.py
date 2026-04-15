"""
LR 3: Standard data types, collections, functions, modules
Task 4: Get words with spicifical parametrs
Version: 1.0
Developer: Satsiuk S.V.
Variant: 24
Date: 05.04.2026
"""


TEXT = ("So she was considering in her own mind, as well as she could, "
        "for the hot day made her feel very sleepy and stupid, whether "
        "the pleasure of making a daisy-chain would be worth the trouble "
        "of getting up and picking the daisies, when suddenly a White "
        "Rabbit with pink eyes ran close by her.")


def get_words(text):
    """
    Split text into words, removing punctuation (commas, periods, hyphens).

    Args:
        text (str): input text

    Returns:
        list of str: clean words in original order
    """
    words = text.replace(',',' ').split()
    words[-1] = words[-1].rstrip('.')
    return words


def count_short_words(words, max_len=6):
    """
    Count words with fewer than max_len characters (case-insensitive).

    Args:
        words (list): list of words
        max_len (int): length threshold (exclusive)

    Returns:
        int: count of words shorter than max_len
    """
    return sum(1 for w in words if len(w) < max_len)


def shortest_ending_with(words, letter):
    """
    Find the shortest word (case-insensitive) ending with given letter.

    Args:
        words (list): list of words
        letter (str): target ending letter

    Returns:
        str or None: shortest matching word, or None if not found
    """
    matches = [w for w in words if w.lower().endswith(letter.lower())]
    if not matches:
        return None
    return min(matches, key=len)


def words_by_length_asc(words):
    """
    Return words sorted by length ascending (stable sort preserves order).

    Args:
        words (list): list of words

    Returns:
        list of str: sorted words
    """
    return sorted(words, key=len)


def task4_run():
    """Run Task 4: analyse the predefined text string."""

    words = get_words(TEXT)

    print(words)
    # a) number of words shorter than 6
    short = count_short_words(words, 6)
    print(f"  a) Words with fewer than 6 characters: {short}")

    # b) shortest word ending with 'w'
    sw = shortest_ending_with(words, "w")
    if sw:
        print(f"  b) Shortest word ending with 'w': \"{sw}\"")
    else:
        print("  b) No words ending with 'w' found.")

    # c) all words sorted by length ascending
    sorted_words = words_by_length_asc(words)
    print(f"  c) Words sorted by length (ascending):")
    print("     " + ", ".join(sorted_words))

#task4_run()