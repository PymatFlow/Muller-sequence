# -*- coding: utf-8 -*-
"""
@author: Kazem Gheysari

"""

from fractions import Fraction

def a_iter():
    """
    In this generator, we use the Miller's algorithm for finding the N-th value of the relation.    
    The original recurrence relation in unstable but reverse relation in stable , or     
    Using the same recurrence relation to go backwards, from high orders to low orders, is stable. 

    Parameters
    ----------
    No input parameter

    Returns
    -------
    y : float
        The n-th value of the sequence
    
    Example
    -----
    y = round(list(islice(a_iter(), 100))[-1], 5)
    
    """       
    an_1 = Fraction(2)
    an = Fraction(-4)
        
    while(True):        
        an_1, an = an, Fraction(111-(1130/an)+(3000/(an_1*an)))
        # print(float(an)) 
        yield float(an)    
        



if __name__ == '__main__':       
    from itertools import islice
    for n in [3, 4, 5, 6, 7, 8, 20, 30, 50, 100]:
        print("{:4d} ---> {}".format(n, list(islice(a_iter(), n))[-1]))
        
    y = round(list(islice(a_iter(), 100))[-1], 5)

    print(y)
        
     