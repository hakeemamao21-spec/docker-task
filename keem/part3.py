def fib_iterative(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2

    a, b = 1, 2  
    for _ in range(3, n+1):
        c = a + b
        a, b = b, c  
    return b

print(fib_iterative(1))  
print(fib_iterative(2))  
print(fib_iterative(5))  
print(fib_iterative(10)) 







