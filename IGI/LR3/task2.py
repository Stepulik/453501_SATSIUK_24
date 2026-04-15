"""
LR 3: Standard data types, collections, functions, modules
Task 2: Count int numbers in range [5, 25] until 0 
Version: 1.0
Developer: Satsiuk S.V.
Variant: 24
Date: 05.04.2026
"""


def task2_run():
    """
    Run Task 2: read integers until 0 is entered,
    count how many of them are in range [5, 25].
    """
    print("TASK 2: Count numbers in range [5, 25]"
          "(enter 0 to stop)")

    count = 0
    total = 0

    while True:
        try:
            num = int(input("Enter 0 to stop: "))
        except ValueError:
            print("Error - please enter an integer number!-_-")
            continue

        if num == 0:
            break

        total += 1
        if 5 <= num <= 25:
            count += 1

    print(f"\n --> Numbers entered: {total}")
    print(f" --> Numbers in [5, 25]: {count}")

#task2_run()