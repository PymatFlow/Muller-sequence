# -*- coding: utf-8 -*-
"""
@author: Kazem Gheysari

"""

def a(n): 
    """
    In this code, we use the closed form of the recurrence relation of the question
    to find the N-th value of the relation

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
    
    y1 = (4*5**(n+1) - 3*6**(n+1))
    y2 = (4*5**n - 3*6**n)
    return y1/y2

if __name__ == '__main__':
    y = round(a(100), 5)

    print("result = ", y)
        