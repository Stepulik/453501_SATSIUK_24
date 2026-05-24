"""
LR 4: Main script file 
Version: 1.0
Developer: Satsiuk S.V.
Variant: 24
Date: 05.04.2026
"""


import task1
import task2
import task3
import task4
import task5
import task6

def main():
    """
    Main entry point of the program.
    Provides menu to choose tasks 1-6 or exit.
    Handles invalid input with ValueError.
    """
    while(True):
        try:
            chose = int(input("Choose your task(1-6) or 0 to stop: "))
            if chose == 0:
                print("exit...")
                break
            elif chose == 1:
                task1.task1_run()
            elif chose == 2:
                task2.task2_run()
            elif chose == 3:
                task3.task3_run()
            elif chose == 4:
                task4.task4_run()
            elif chose == 5:
                task5.task5_run()
            elif chose == 6:
                task6.task6_run()
            else:
                raise ValueError("Incorrect task!")
        except ValueError:
           print("Incorrect task number!")

if __name__ == "__main__":
    main()
           