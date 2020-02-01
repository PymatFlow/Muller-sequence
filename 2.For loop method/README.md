### Implementation on the sequence with *For Loop*

In this code, we use the **for loop** for finding the N-th value of the relation.


It is not the best solution, but it is one of the solution



`a(n):` 
```
a(1) = 2 
a(2) = -4 
a(n) = 111 - 1130/a(n-1) + 3000/(a(n-1) * a(n-2))
```




### Parameters    

>     n : scalar
        Input sequence.

### Returns
>     y : float
        The value of the sequence for n

###     Notes
>     n>0
    n must be bigger than zero


###     Output
   3 -> 9.378378378378379<br/>
   4 -> 7.801152737752162<br/>
   5 -> 7.154414480975249<br/>
   6 -> 6.806784736923633<br/>
   7 -> 6.592632768704439<br/>
   8 -> 6.449465933790288<br/>
  20 -> 6.036031881081857<br/>
  30 -> 6.00564868877142<br/>
  50 -> 6.000146534561388<br/>
 100 -> 6.000000016099565<br/>
