"""
LR 3: Standard data types, collections, functions, modules
Task 3: Count of whitespace and apostrophes
Version: 1.0
Developer: Satsiuk S.V.
Variant: 24
Date: 05.04.2026
"""

TEXT = (
    "So she was considering in her own mind, as well as she could, "
    "for the hot day made her feel very sleepy and stupid, whether "
    "the pleasure of making a daisy-chain would be worth the trouble "
    "of getting up and picking the daisies, when suddenly a White "
    "Rabbit with pink eyes ran close by her."
)



def count_whitespace_and_apostrophes(str1):
    """
    Count whitespace characters and apostrophes in string str1.

    Args:
        str1: input string

    Returns:
        tuple: (whitespace_count, apostrophe_count)
    """
    ws = sum(1 for c in str1 if c == " ")
    ap = sum(1 for c in str1 if c == "'")
    return ws, ap


def task3_run():
    """Run Task 3: count whitespace chars and apostrophes in user input."""
    print("TASK 3: Count whitespace chars and apostrophes\n")

    text = input("Enter your string:")
    ws, ap = count_whitespace_and_apostrophes(text)
    print(f"\n  Whitespace characters: {ws}")
    print(f"  Apostrophes ('): {ap}")

#task3_run()
