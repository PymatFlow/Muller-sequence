# -*- coding: utf-8 -*-
"""
@author: Kazem Gheysari

"""
import decimal
decimal.getcontext().prec = 1000
 
def a(n):   
    """
    In this code, we use the for loop for finding the N-th value of the relation

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
    y=[decimal.Decimal(2),decimal.Decimal(-4)]
    for i in range(2, n+1):
        y.append(decimal.Decimal(111 - 1130/y[i-1] + 3000/(y[i-1]*y[i-2])))
    return float(y[n])



if __name__ == '__main__': 
    for n in [3, 4, 5, 6, 7, 8, 20, 30, 50, 100]:
        print("{:4d} -> {}".format(n, a(n)))
    
    
    y = round(a(100), 5)
    
    print(y)