# Naive Fib Implimentation

def fib(n: int):
    if n <= 1:
        return 1
    return fib(n - 2) + fib(n - 1)


# Improve Implimentation With Memorization

def fib(n: int, memo = {}):

    if n in memo: return memo[n]

    if n <= 1:
        return 1
    memo[n] = fib(n - 2, memo) + fib(n - 1, memo)

    return memo[n]



print(fib(41))