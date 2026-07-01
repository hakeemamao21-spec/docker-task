#def myFactorial(n):
    #if n==1:
    #return 1
    #else:
        #return n*myFactorial(n-1)    
#print(myFactorial(5))

##def myfactorial2(n):
    ##result = 1
    #for i in range (1, n+1):
        #result = result * i
    #return result
#print (myfactorial2(5))


#def fib(x):
    #if x == 0 or x == 1:
        #return 1
    #else:
        #return fib(x - 1) + fib(x - 2)

#print(fib(5))


def fib(x):
    a = 1 
    b = 1
    for i in range(2, x+1):
        a, b = b, a + b
    return b

print(fib(40))
