import sys

def fib(n):
    
    sys.setrecursionlimit(10000)
    
    if n == 0 :
        return 0
    elif n ==1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

if len(sys.argv) >= 2:
    n = int(sys.argv[-1])
    print(str(fib(n)))
