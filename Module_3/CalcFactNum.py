def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return n

val = factorial(5)

print('Factorial is : ', val)