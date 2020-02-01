# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:30:41 2020

@author: Kz
"""

from fractions import Fraction

def a(int n):
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
    Run the code in the following way:
        
    1) build the extension :        
        $ python setup.py build_ext --inplace
    
    2) in python :
        >>> import main_cython 
    
    """        
    cdef float y[1000]
    
    an_1 = Fraction(2)
    an = Fraction(-4)
    
    for k in range(n-1, -1, -1):
        an_1, an = an, Fraction(111-(1130/an)+(3000/(an_1*an)))
        y[k] = an  
        
    return y[0]        


for n in [3, 4, 5, 6, 7, 8, 20, 30, 50, 100]:
    print("{:4d} ---> {}".format(n, a(n)))
        
y = round(a(100), 5)

print(y)