"""
import functools
n = input("enter a number : ")
print(functools.reduce(int.__add__, map(int, n)))
"""

n = input("enter a number : ")
# list of str
#print(list(map(str, n)))
#print(list(n))
#print(" + ".join(list(n)))
print(eval(" + ".join(list(n))))





