### The closed form of the recurrence relation

In this code, we use the closed form of the recurrence relation of the question to find the N-th value of the relation.

[Reference Link](http://discrete.openmathbooks.org/dmoi3/sec_recurrence.html "Reference Link")

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