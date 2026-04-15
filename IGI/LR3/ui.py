"""
LR 3: Standard data types, collections, functions, modules
UI: Intarface for console output 
Version: 1.0
Developer: Satsiuk S.V.
Variant: 24
Date: 05.04.2026
"""


import random

def print_table_row(x, n, res, real_sum, eps):
    """ 
    This function exist for beautiful table for task1 table 
     
    Args:
        x (float): selected x 
        n (int): current number of iterations
        res (float): current result 
        real_sum (float): real sum with math module
        eps (float): selected epsilon
    """
    print(f"{x:^12}\t{n:^3}\t{res:^18}\t{real_sum:^18}\t{eps:^18}")


def mydecor(func):
    """ This function is decorator for func in task 1"""
    def in_mydecor(*args, **kwargs):
        print(f"{"x":^12}\t{"n":^3}\t{"F(x)":^18}\t{"Math F(x)":^18}\t{"eps":^18}")
        result = func(*args, **kwargs)
        
        return result
    return in_mydecor

def mygen(min=0, max=100):
    """
    Generator that yields numbers from min (inclusive) to max (exclusive),
    incrementing by 1 each step. Used in task5 to auto‑generate a list.

    Args:
        min (float): lower bound (inclusive)
        max (float): upper bound (exclusive)

    Yields:
        float: next number in the sequence
    """
    while min < max:
        yield min
        min += 1
        
    
def get_valid_size():
    """Prompt user for a positive integer list size."""
    while True:
        try:
            n = int(input("  Enter list size (> 0): "))
            if n > 0:
                return n
            print("  Error: size must be positive.")
        except ValueError:
            print("  Error: please enter an integer.")
    
    
def display_list(lst):
    """
    Prints the given list to the console.

    Args:
        lst (list): list to display
    """
    print(lst)
        
def init_by_user(lst, n):
    """
    Prompts the user for minimum and maximum bounds for the generator.
    Returns them as a tuple.

    Returns:
        tuple (float, float): (min_bound, max_bound)
    """
    lst.clear()
    for i in range(n):
        while True:
            try:
                val = float(input(f"Enter element [{i}]: "))
                lst.append(val)
                break
            except ValueError:
                print("Error: please enter a valid number.")

def init_by_gen():
    """ Inicialization function for my generator"""
    while True:
        try:
            val1 = float(input(f"Enter min border: "))
            val2 = float(input(f"Enter max border: "))
            return val1, val2
            break
        except ValueError:
            print("Error: please enter a valid number.")