"""
LR 3: Standard data types, collections, functions, modules
Task 5: 
Version: 1.0
Developer: Satsiuk S.V.
Variant: 24
Date: 05.04.2026
"""

import ui

def product_of_negatives(lst):
    """
    Compute product of all negative elements.

    Args:
        lst (list): input list of numbers

    Returns:
        float or None: product, or None if no negatives
    """
    negs = [x for x in lst if x < 0]
    if not negs:
        return None
    result = 1.0
    for x in negs:
        result *= x
    return result

def sum_positives_before_max_abs(lst):
    """
    Compute sum of positive elements located BEFORE the element
    with the maximum absolute value.

    Args:
        lst (list): input list of numbers

    Returns:
        float or None: sum, or None if max_abs element not found or
                       no positives before it
    """
    
    max1 = max(lst)
    print("max1 - ", max1)
    min1 = min(lst)
    print("min1 - ", min1)
    if min1 >= 0:
        min1 = max1
    
    res = 0
    for item in lst:
        if item == min1 or item == max1:
            break
        if item > 0:
           res += item
        
    return res  
    
    
def task5_run():
    """
    Run Task 5: find product of negative elements and sum of
    positive elements before the max-abs element.
    """
    

    print("Initialisation method:")
    print("1 - my generator")
    print("2 - manual input")

    lst = []
    while True:
        choice = input("Your choice (1/2):").strip()
        if choice == "1":
            min1, max1 = ui.init_by_gen()
            for i in ui.mygen(min1, max1): 
                lst.append(i)
            break
        elif choice == "2":
            n = ui.get_valid_size()
            ui.init_by_user(lst, n)
            break
        else:
            print("  Error: enter 1 or 2.")

    ui.display_list(lst)

    prod = product_of_negatives(lst)
    if prod is None:
        print("\n  Product of negatives: no negative elements")
    else:
        print(f"\n  Product of negatives: {prod:.4f}")

    s = sum_positives_before_max_abs(lst)
    max_abs_val = max(lst, key=abs)
    max_abs_idx = lst.index(max_abs_val)
    print(f"  Max |element|: {max_abs_val} at index {max_abs_idx}")
    if s is None:
        print("  Sum of positives before max|x|: no such elements")
    else:
        print(f"  Sum of positives before max|x|: {s:.4f}")

#task5_run()