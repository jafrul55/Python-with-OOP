# Fibonacchi Number:
def fibonachi(n):
    if n == 0:
       return 0
    elif n == 1:
        return 1
    else:
     return fibonachi(n-1) + fibonachi(n-2)

for i in range(10):
    print(fibonachi(i),end=" ")

""" 
The function fibonacci() is defined to take a single argument, n, 
which is the index of the term in the series that we want to find. 
If n is 0 or 1, then the function returns 0 or 1 respectively, 
since these are the first two terms of the series.
Otherwise, the function calls itself with the n-1 and n-2 indices,
and returns the sum of the two resulting values. 
This recursive approach allows us to generate the entire series 
by calling the function repeatedly with different values of n.

 """