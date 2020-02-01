### Implementation of the sequence

```
a(1) = 2 
a(2) = -4 
a(n) = 111 - 1130/a(n-1) + 3000/(a(n-1) * a(n-2))
```


Three-term recurrence relations become significant and useful in numerical mathematics, especially for the calculation of orthogonal polynomials such as Tschebyscheff, Jacobi, Laguerre, Hermite and Legendre polynomials.
There are known several algorithms calculating numerically stable a minimal solution for a three-term recurrence relation, e.g. Miller backward algorithm, Olver algorithm and Gautschi continued fraction algorithm.

In this project, Miller Backward Algorithm is used.
To get a better condition for calculating a minimal solution of a three-term recurrence relation, Miller suggests to compute the values backward by using the property of a minimal solutions, that they converge to zero.


The most challenging part of this assigment is **floating point calculations**.
If we implement the sequence normally with 'For loop', it will give us 100 for 100th value.

2<br/>
-4<br/>
18.5<br/>
9.378378<br/>
7.801153<br/>
7.154414<br/>
6.806785<br/>
6.592633<br/>
6.449466<br/>
6.348452<br/>
6.274439<br/>
6.218696<br/>
6.175845<br/>
6.142491<br/>
6.118039<br/>
6.129993<br/>
6.652921<br/>
14.71101<br/>
64.83933<br/>
96.71745<br/>
99.79487<br/>
99.98759<br/>
99.99925<br/>
99.99995<br/>
100<br/>
<br/>

But this answer is **wrong**.


If the relation is implemented recurrently, It will not converge for more than 50 and the system is **unstable**.


The reason for the discrepancy is due to rounding in **floating point calculations**.
The fact that floating-point numbers cannot precisely represent all real numbers, and that floating-point operations cannot precisely represent true arithmetic operations, leads to many surprising situations.
The system is doing some rounding when you do arithmetic.
And all that rounding can cause problems, as we have seen.




#### Notes
Please go to each folder to find more information about each implementation. 

