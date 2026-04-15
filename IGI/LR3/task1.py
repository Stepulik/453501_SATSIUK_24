"""
LR 3: Standard data types, collections, functions, modules
Task 1: Series expansion of ln(1-x)
Version: 1.0
Developer: Satsiuk S.V.
Variant: 24
Date: 05.04.2026
"""

import ui
import math

@ui.mydecor
def sum_ln(x, eps):
    """
    Computes ln(1 - x) using power series with given precision eps.
    Prints convergence table each iteration.
    Max 500 iterations.
    """
    real_sum = math.log(1 - x)
    #print(real_sum, " <---- REAL SUM")
    res = 0
    n = 1
    while abs(real_sum - res) > abs(eps):
        res -= x ** n / n 
        ui.print_table_row(x, n, res, real_sum, eps)      
        n += 1
        if n == 500:
            break
    else:
        print("n <= 500")
    return res

def task1_run():
    """
    Interactive interface for Task 1.
    Reads x (-1 < x < 1) and eps, then calls sum_ln.
    """
    i = 1
    x = 0
    eps = 0
    while(True):
        try:
            x = float(input("Enter x: "))
            if not(-1 < x < 1):
                raise ValueError("X must be in interval (-1, 1)!")
            break
        except ValueError:
            print("X is a number in (-1, 1)!\nPlease, try again!")
        finally:
            if i != 1:
                print(f"Its your {i} try")
            i += 1
    i = 1
    while(True):
        try:
            eps = float(input("Enter eps: "))
            if not(eps <= 0.1):
                raise ValueError("Eps must lower than 0.1!")
            break
        except ValueError:
            print("X is an float number lower than 0.1!\nPlease, try again!")
        finally:
            if i != 1:
                print(f"Its your {i} try")
            i += 1
    sum_ln(x, eps)

#task1_run()
                
        
