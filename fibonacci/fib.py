""" 

Fibonacci implementation using 3 approaches
---
1. Recursion
2. Memoize approach
3. Bottom-up approach

"""


import datetime


def fib_recursion(n):
    """ Fibonacci recursive implementation """

    if n == 0 or n == 1:
        return n
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)


# Dynamic programming

def fibonacci(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        result = n
    else:
        result = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = result
    return result


def fib_memo(n):
    """ Fibonacci memoized implementation """

    memo = [None] * (n + 1)
    return fibonacci(n, memo)


def fib_bottom_up(n):
    """ Fibonacci bottom up implementation """

    if n == 0 or n == 1:
        return n
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[n]


def visual_test():
    print("\nFibonacci of 35 using Recursion\n---")
    one = datetime.datetime.now()
    print(fib_recursion(35))
    diff = datetime.datetime.now() - one
    print("time[s]: " + str(diff.seconds))
    print("time[ms]: " + str(diff.microseconds))

    print("\nFibonacci of 75 using Memoize\n---")
    one = datetime.datetime.now()
    print(fib_memo(75))
    diff = datetime.datetime.now() - one
    print("time[s]: " + str(diff.seconds))
    print("time[ms]: " + str(diff.microseconds))

    print("\nFibonacci of 100 using Bottom up\n---")
    one = datetime.datetime.now()
    print(fib_bottom_up(100))
    diff = datetime.datetime.now() - one
    print("time[s]: " + str(diff.seconds))
    print("time[ms]: " + str(diff.microseconds))


if __name__ == "__main__":
    visual_test()
