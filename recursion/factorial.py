#Get the factorial of a non-negative integer.
def factorial(n):
    if n < 1:
        return 1
    return n * factorial (n-1)

print (factorial(2))