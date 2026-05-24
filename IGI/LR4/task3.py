"""
Lab Work #4 - Task 3: Series Expansion ln(1-x) — Main
Version: 1.0
Developer: Variant 24
Date: 2024
Description:
    Computes the Taylor series for ln(1-x), prints a table of values,
    displays statistics, and draws a matplotlib plot saved to file.
"""

import sys
import os
import math
import matplotlib.pyplot as plt


def mydecor(func):
    """ This function is decorator for func in task 1"""
    def in_mydecor(*args, **kwargs):
        print(f"{'x':^12}\t{'n':^3}\t{'F(x)':^18}\t{'Math F(x)':^18}\t{'eps':^18}")
        result = func(*args, **kwargs)
        return result
    return in_mydecor

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
    


class ValidationMixin:
    """Mixin class providing basic validation methods."""
    def validate_nonempty(self, value, field_name):
        if not value or not str(value).strip():
            raise ValueError(f"{field_name} cannot be empty")
        return str(value).strip()
    def validate_x(self, x):
        if x >= 1 or x <= -1:
            raise ValueError(f"|x| must be < 1, x is {x}")
    def validate_eps(self, eps):
        if eps >= 0.1 or eps <= 0:
            raise ValueError(f"eps must be < 0.1 and eps > 0, eps is {eps}")

class SumLnManager(ValidationMixin):
    
    def __init__(self, x, eps):
        self.validate_x(x)
        self.validate_eps(eps)
        self.x = x
        self.eps = eps
        
        
        sred_arif = 0
        #calc all parametrs
        real_sum = math.log(1 - x)
        #print(real_sum, " <---- REAL SUM")
        results = []
        ns = []
        res = 0
        n = 1
        while n==1 or abs(real_sum - res) > abs(eps):
            ns.append(n)
            res -= x ** n / n
            results.append(res) 
            #ui.print_table_row(x, n, res, real_sum, eps)      
            n += 1
            if n == 500:
                break
        else:
            print("n <= 500")
        
        self.__res = res
        self.__ns = ns.copy()
        self.__results = results.copy()
        self.__realres = real_sum
        #srednee arifmetichescoe
        for item in results:
            sred_arif += item
        self.__sred_arif = sred_arif / len(results)
        
        #mediana
        results.sort()
        if len(results) % 2 == 0:
            mediana = results[len(results)//2-1]
        else:
            mediana = results[len(results)//2]
        self.__mediana = mediana
        
        #moda
        self.__moda = None
        
        #disperion
        dispersia = 0
        for item in results:
            dispersia += float(item - sred_arif)**2
        self.__dispersia = dispersia / len(results)
        
        #SKO
        self.__sko = abs(dispersia)**(1/2)
        
    @property
    def res(self):
        return self.__res
    
    @property
    def realres(self):
        return self.__realres
    
    @property
    def sred_arif(self):
        return self.__sred_arif
    
    @property
    def mediana(self):
        return self.__mediana
    
    @property
    def moda(self):
        return self.__moda
    
    @property
    def dispersia(self):
        return self.__dispersia
    
    @property
    def sko(self):
        return self.__sko

    def plot(self):
        """
        Construct plot using matplotlib
        """
        
        fig, ax= plt.subplots()
        
        
        ax.set_title("Results of ln(1-x) function", fontsize=20, fontweight="bold")
        ax.set_xlabel("Iterations", fontsize=14)
        ax.set_ylabel("Values", fontsize=14)
        ax.grid(True, linestyle=":", alpha=0.6)
        
        
        ax.plot(self.__ns, self.__results, color="blue", marker="o", markersize="3", linewidth=2, label="My Function value")
        
        
        ax.axhline(y=self.__realres, color="green", linestyle="--", linewidth=1, label="Correct value")
        
        
        ax.legend(fontsize=10)
        
        ax.annotate("Last iteration",
                    xy=(self.__ns[-1], self.__results[-1]), 
                    xytext=(self.__ns[-1] - self.__ns[-1]/3, self.__sred_arif),
                    arrowprops=dict(facecolor="black", linewidth=0.5)
                    )
        #print(f"sred - {self.__sred_arif}, all - {self.__results[-1] - self.__sred_arif}")
        plt.savefig("MyPlot.png", dpi=300, bbox_inches="tight")
        plt.show()
        
       
    
    @mydecor   
    def print_all_data(self):
        for i in range(len(self.__ns)):
            print_table_row(self.x, self.__ns[i], self.__results[i], self.__realres, self.eps)
        print(f"Sred arif: {self.__sred_arif}")
        print(f"Mediana: {self.__mediana}")
        print(f"Moda: {self.__moda}")
        print(f"Dispersia: {self.__dispersia}")
        print(f"Sko: {self.__sko}")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


def task3_run():
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
            print("EPS is an float number lower than 0.1!\nPlease, try again!")
        finally:
            if i != 1:
                print(f"Its your {i} try")
            i += 1
            
            
    manager = SumLnManager(x, eps)
    
    manager.print_all_data()
    manager.plot()
    
    
#task3_run()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\