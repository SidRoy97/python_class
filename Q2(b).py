import functools

n = int(input("Enter a no. : "))

def factorial(x):
    return(functools.reduce(int.__mul__,range(1,x+1)))

print(factorial(n))
