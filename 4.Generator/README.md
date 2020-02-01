### Implementation of the sequence as a generator

In this code, we use [Miller's method](https://en.wikipedia.org/wiki/Miller%27s_recurrence_algorithm "Miller's method") for finding the Nth value of the relation. Miller's algorithm provides a numerically stable procedure to obtain the decreasing solution.
The original recurrence relation in unstable but reverse relation in stable, in other words, using the same recurrence relation to go backwards, from high orders to low orders, is stable.



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
   3 ---> 7.801152737752162<br/>
   4 ---> 7.154414480975249<br/>
   5 ---> 6.806784736923633<br/>
   6 ---> 6.592632768704439<br/>
   7 ---> 6.449465933790288<br/>
   8 ---> 6.348452056654357<br/>
  20 ---> 6.029847325023902<br/>
  30 ---> 6.0047028131881754<br/>
  50 ---> 6.000122109152288<br/>
 100 ---> 6.000000013416304<br/>
