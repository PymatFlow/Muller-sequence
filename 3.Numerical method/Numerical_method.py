# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:18:34 2020

@author: Kazem Gheysari
"""


from fractions import Fraction
import numpy as np


def a(n):
    """
    In this code, we use the for Miller's mehtod for finding the N-th value of the relation    
    The original recurrence relation in unstable but reverse relation in stable , or     
    Using the same recurrence relation to go backwards, from high orders to low orders, is stable. 

    Parameters
    ----------
    n : scalar
        Input sequence.

    Returns
    -------
    y : float
        The value of the sequence for n
    Notes
    -----
    n>0
    n must be bigger than zero
    """        
    
    y = np.zeros(n) 
    
    an_1 = Fraction(2)
    an = Fraction(-4)
    
    for k in range(n-1, -1, -1):
        an_1, an = an, Fraction(111-(1130/an)+(3000/(an_1*an)))
        y[k] = an  
        
    return y[0]        


if __name__ == '__main__':
    for n in [3, 4, 5, 6, 7, 8, 20, 30, 50, 100]:
        print("{:4d} ---> {}".format(n, a(n)))
            
    y = round(a(100), 5)
    
    print(y)
        
     