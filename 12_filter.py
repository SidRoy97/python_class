import functools
a = [11, 22, 33, 44]
print(functools.reduce(int.__add__, a))

n = 15
print(functools.reduce(int.__mul__, range(1, n + 1)))


a = [11, 22, 33, 44]
print(functools.reduce(int.__add__, a, 100))

