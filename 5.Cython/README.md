### Cython Implementation of the sequence

In this code, we use [Miller's method](https://en.wikipedia.org/wiki/Miller%27s_recurrence_algorithm "Miller's method") for finding the Nth value of the relation. Miller's algorithm provides a numerically stable procedure to obtain the decreasing solution.
The original recurrence relation in unstable but reverse relation in stable, in other words, using the same recurrence relation to go backwards, from high orders to low orders, is stable.


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

###     How to run the code 
    Run the code in the following way:
        
    1) build the extension :        
        $ python setup.py build_ext --inplace
    
    2) in python :
        >>> import main_cython 


###     Output
   3 ---> 7.80115270614624<br/>
   4 ---> 7.154414653778076<br/>
   5 ---> 6.806784629821777<br/>
   6 ---> 6.59263277053833<br/>
   7 ---> 6.449465751647949<br/>
   8 ---> 6.348452091217041<br/>
  20 ---> 6.029847145080566<br/>
  30 ---> 6.004703044891357<br/>
  50 ---> 6.0001220703125<br/>
 100 ---> 6.0<br/>
